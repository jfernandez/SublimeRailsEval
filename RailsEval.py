import sublime, sublime_plugin
import tempfile, os

class RailsEvalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            ruby_code = self.view.substr(region)

        # Copy the Ruby code to a temp file
        fd, path = tempfile.mkstemp()
        os.write(fd, ruby_code)
        os.close(fd)

        # Fetch the settings
        settings      = sublime.load_settings("RailsEval.sublime-settings")
        ruby_path     = settings.get("ruby_path")
        rails_path    = settings.get("rails_path")
        script_runner = settings.get("script_runner")

        # Build the shell command
        command = "%(ruby_path)s %(script_runner)s %(path)s" % locals()

        # Use Sublime's API to run a shell command
        self.view.window().run_command("exec", {
            "cmd": [command],
            "shell": True,
            "working_dir": rails_path
        })
