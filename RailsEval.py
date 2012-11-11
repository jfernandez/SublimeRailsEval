import sublime, sublime_plugin
import tempfile, os

class RailsEvalCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        # Load the settings
        settings           = sublime.load_settings("RailsEval.sublime-settings")
        self.ruby_path     = settings.get("ruby_path")
        self.rails_path    = settings.get("rails_path")
        self.script_runner = settings.get("script_runner")

        ruby_code = self.get_selection()
        file_path = self.copy_to_file(ruby_code)
        command   = self.build_command(file_path)

        # Use Sublime's API to run a shell command
        self.view.window().run_command("exec", {
            "cmd": [command],
            "shell": True,
            "working_dir": self.rails_path
        })

    def get_selection(self):
        for region in self.view.sel():
            selection = self.view.substr(region)
        return selection

    def copy_to_file(self, content):
        fd, path = tempfile.mkstemp()
        os.write(fd, content)
        os.close(fd)
        return path

    def build_command(self, file_path):
        command = self.ruby_path + ' ' + file_path + ' ' + self.script_runner
        return command