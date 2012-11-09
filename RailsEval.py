import sublime, sublime_plugin

class RailsEvalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            ruby_code = self.view.substr(region)

        self.panel = self.view.window().get_output_panel('exec')
        settings = sublime.load_settings("RailsEval.sublime-settings")
        ruby_path = settings.get("ruby_path")
        rails_path = settings.get("rails_path")
        command = "%(ruby_path)s script/runner '%(ruby_code)s'" % locals()

        self.view.window().run_command("exec", {
            "cmd": [command],
            "shell": True,
            "working_dir": rails_path
        })
        self.view.window().run_command("show_panel", {"panel": "output.test_panel"})