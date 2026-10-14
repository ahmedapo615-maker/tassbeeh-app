[app]

# (str) Title of your application
title = Tasbeeh App

# (str) Package name
package.name = tasbeehapp

# (str) Package domain (needed for android packaging)
package.domain = org.mohamed

# (str) Version of the application
version = 0.1

# (str) Source directory where the app lives
source.dir = .

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
