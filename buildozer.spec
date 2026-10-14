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

android.api = 33
android.minapi = 21
android.sdk = 33

# (str) Indicate whether the build should accept Android SDK licenses
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
