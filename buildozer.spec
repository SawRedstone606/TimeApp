[app]
title = TimeApp
package.name = timeapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# ใช้ API 33 หรือ 34 เพื่อเลี่ยงการดึง Build-Tools 37
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
