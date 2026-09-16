[app]

# (str) Title of your application
title = TimeApp

# (str) Package name
package.name = timeapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# ==============================================================================
# Android specific
# ==============================================================================

# (int) Target Android API, should be as high as possible.
# ใช้ API 33 เพื่อความเสถียรบน GitHub Actions และเลี่ยงปัญหา Build-Tools 37
android.api = 33

# (int) Minimum API required. 21 = Android 5.0 (Lollipop)
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (str) The Android arch to build for (arm64-v8a สำหรับมือถือยุคใหม่)
android.archs = arm64-v8a

# ==============================================================================
# Buildozer options
# ==============================================================================

# (int) Log level (0 = error only, 1 = info, 2 = debug (with output of commands))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
