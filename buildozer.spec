[app]
title = GST App
package.name = gstapp
package.domain = org.example.gst
source.dir = .
source.include_exts = py,xlsx
version = 1.0
requirements = python3,kivy,openpyxl
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
