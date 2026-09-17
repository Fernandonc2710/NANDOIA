[app]
title = Nando
package.name = nando
package.domain = org.fernando
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,reportlab,python-docx,pillow
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk_path = /usr/local/lib/android/sdk
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
