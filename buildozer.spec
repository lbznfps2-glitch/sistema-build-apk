[app]
title = SistemaUpdate
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,android,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a
p4a.branch = master
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
