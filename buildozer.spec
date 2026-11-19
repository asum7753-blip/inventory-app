[app]

title = Inventory App
package.name = inventoryapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db,sqlite

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
