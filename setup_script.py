import sys
from cx_Freeze import setup, Executable


"""Copyright (c) 2023 Kennart Tech"""

# ---------------------------------------------------------------------
build_exe_options = {
    "packages": ['customtkinter', 'tkinter', 'datetime', 'plyer','hashlib', 
                 'PIL', 'json', 'sqlite3', 'os', 'sys','CTkMessagebox', 'threading'],  
                 # List of packages to include
    "excludes": ['flask', 'ttkthemes', 'requests', 'qrcode', 'pymongo', 'flaskwebgui',
                 'CTkColorPicker', 'CustomTkinterTitlebar', 'Custom-Tooltip', 'WinToaster',
                 'simplidb', 'Eel', 'CTkTable', 'CTkToolTip', 'Flask-RESTful', 'qrcode'],  # List of packages to exclude
    "include_files": ['icons/','config/', 
    'C:/Users/Kennart Tech/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter/assets'],  # List of files to include
    "include_msvcr": True,  # This include Microsoft Visual C++ runtime
    "optimize": 1, #These increase the speed of the software in terms of the perfomance                      
    "zip_include_packages": ['icons/tools'],
    "zip_exclude_packages": [],
    # "zip_exclude_dlls": [],
}
# ----------------------------------------------------------------------

# ------------------------------------------------------------------
shortcut_table = [#This defines the shorcut to be created for the frozen executable
    ("DesktopShortcut",             # Shortcut
     "DesktopFolder",               # Directory_
     "SwiftSell",                   # Desktop icon Name
     "TARGETDIR",                   # Component_
     "[TARGETDIR]startup.exe",   # Target
     None,                          # Arguments
     None,                          # Description
     None,                          # Hotkey
     None,                          # Icon
     None,                          # IconIndex
     None,                          # ShowCmd
     "TARGETDIR",                   # WkDir
     ),
]


msi_data = {"Shortcut": shortcut_table}
# ------------------------------------------------------------------

# -----------------------------------------------------------------
base = None  #this will set the base of the application to a GUI application on Windows.
if sys.platform == "win32":
    base = "Win32GUI"
# ------------------------------------------------------------------

# ------------------------------------------------------------------------
script_path = "startup.py"  # Replace with the path to your Python script
# ------------------------------------------------------------------------

# -----------------------------------------------------------------------
setup(
    name="SwiftSell",
    version="2.0.0",
    description="SwiftSell",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": {"data": msi_data},
    },
    executables=[Executable(script_path, base=base, icon="icons/logo.ico", shortcut_name="SwiftSell")],
    author="Kennart Tech",
)
# ----------------------------------------------------------------------------
