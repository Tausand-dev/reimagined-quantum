# -*- mode: python -*-

block_cipher = None


a = Analysis(['installer.py'],
             pathex=['D:\\Tausand\\ReimaginedQuantum\\Software'],
             binaries=[],
             #datas=[('C:\\Users\\Rutherford\\Documents\\ReimaginedQuantum\\Software\\Quantum.zip', '.')],
             datas=[('D:\\Tausand\\ReimaginedQuantum\\Software\\Quantum.zip', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='QuantumInstaller',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='GUI/Program/icon.ico' )