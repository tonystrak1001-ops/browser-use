# -*- mode: python ; coding: utf-8 -*-
import os
import glob
from PyInstaller.utils.hooks import collect_all, collect_submodules

block_cipher = None

datas = []
binaries = []
hiddenimports = []

for pkg in ['browser_use', 'cdp_use', 'bubus', 'browser_use_sdk']:
    try:
        pkg_datas, pkg_binaries, pkg_hiddenimports = collect_all(pkg)
        datas.extend(pkg_datas)
        binaries.extend(pkg_binaries)
        hiddenimports.extend(pkg_hiddenimports)
    except Exception:
        pass

hiddenimports += collect_submodules('browser_use')
hiddenimports += collect_submodules('google.genai')
hiddenimports += collect_submodules('google.api_core')

system_prompts_dir = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'browser_use', 'agent', 'system_prompts')
if os.path.isdir(system_prompts_dir):
    datas.append((system_prompts_dir, 'browser_use/agent/system_prompts'))

a = Analysis(
    ['browser_use/skill_cli/main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='browser-use',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
