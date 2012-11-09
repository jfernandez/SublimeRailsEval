Sublime Text 2 Rails Eval
=========================

Installation
------------

Go to your Sublime Text 2 `Packages` directory

 - OS X: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
 - Windows: `%APPDATA%/Sublime Text 2/Packages/`
 - Linux: `~/.config/sublime-text-2/Packages/`

and clone the repository using the command below:

``` shell
git clone https://github.com/jfernandez/SublimeRailsEval.git RailsEval
```

Settings
--------

'Sublime Text 2' -> 'Preferences' -> 'Package Settings' -> 'RailsEval'

Make a copy of `RailsEval.sublime-settings` file to `~/Library/Application Support/Sublime Text 2/Packages/User/` and make your changes.

If you're using RVM, set use this as your ruby_path: `~/.rvm/bin/rvm-auto-ruby`

For Rails 3, set script_runner to `rails runner`


Usage
-----

Select a piece of Rails code and run: `Command-Option-r`


Settings:
---------

    {
      "ruby_path": "ruby",
      "rails_path": "/path/to/project",
      "script_runner": "script/runner"
    }