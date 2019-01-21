@echo off

python -m PyInstaller pynssmkiller.py -F --paths "c:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x86"
pause