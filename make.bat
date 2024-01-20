@echo off

if %1==ui goto ui
if %1==man goto man


:ui
pyinstaller --noconfirm --onefile qemu-manager-ui.py 
goto clean

:man
pyinstaller --noconfirm --onefile qemu-manager.py
goto clean

:clean
copy dist\*.exe .
del /f /s /q build
del /f /s /q dist
rd /s /q build
rd /s /q dist
del /f /s /q *.spec