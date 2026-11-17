# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['labelImg.py'],
    pathex=['libs', './'],
    binaries=[],
    datas=[
        ('data/predefined_classes.txt', 'data'),
        ('resources/icons', 'resources/icons'),
        ('resources/strings', 'resources/strings'),
    ],
    hiddenimports=['xml', 'xml.etree', 'xml.etree.ElementTree', 'lxml.etree'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='labelImg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources/icons/app.ico'] if False else [],
)
