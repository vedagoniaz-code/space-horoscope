[app]

# Название приложения

title = Космос знает ответ

# Имя Android-пакета

package.name = spacehoroscope

# Уникальный идентификатор приложения

package.domain = org.ezra

# Где находится программа

source.dir = .

# Главный файл программы

source.main = space.py

# Файлы, которые нужно включить в APK

source.include_exts = py,png,jpg,jpeg

# Версия приложения

version = 1.0

# Зависимости

requirements = python3,kivy

# Ориентация экрана

orientation = portrait

# Не запускать в полноэкранном режиме

fullscreen = 0

# -------------------------------------------------

# Android

# -------------------------------------------------

# Минимальная версия Android

android.minapi = 23

# Автоматически принять лицензии Android SDK

android.accept_sdk_license = True

# Разрешение на работу с интернетом не требуется

# android.permissions = INTERNET

# -------------------------------------------------

# Buildozer

# -------------------------------------------------

# Предупреждения Buildozer

warn_on_root = 1
