@echo off
rem =============================================================================
rem  rebuild-index.bat  -  the updater (Windows).
rem  Double-click this file to rescan the folder and rebuild the catalogue.
rem  A console window opens, it does its work, then waits for a key so you can
rem  read the log before closing.
rem
rem  To preview without writing anything, run from a command prompt:
rem      rebuild-index.bat -Dry
rem =============================================================================
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0rebuild-index.ps1" %*
echo.
pause
