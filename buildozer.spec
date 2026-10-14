[app]
title = Tasbeeh App
package.name = tasbeehapp
package.domain = org.mohamed
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

[buildozer]
log_level = 2
warn_on_root = 1
