# pwdgrab
Grab and exfiltrate "important" files.

## Building Executables

Use [PyInstaller](https://pyinstaller.org/en/stable/installation.html) to build executables for target systems. Install with:

```bash
python3 -m pip install pyinstaller
```

With src directory as the root folder, build the executable (on linux-based or windows hosts) with:
```bash
pyinstaller --onefile grabber.py
```
or with:
```bash
python3 -m PyInstaller --onefile ./grabber.py
```

Specifically on windows hosts you can force the command prompt to stay in the background with:

```powershell
python -m PyInstaller --onefile .\grabber.py
```
