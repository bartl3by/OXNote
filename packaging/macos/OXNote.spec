# -*- mode: python -*-

block_cipher = None


a = Analysis(['oxnote/oxnote.py'],
             pathex=['oxnote'],
             binaries=[],
             datas=[('resources/fonts/*', 'fonts'), ('resources/designs/default/*', 'designs/default'), ('configuration/*', 'configuration'), ('LICENSE', '.')],
             hiddenimports=['user_interface.embedded_mime_text_edit'],
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
          exclude_binaries=True,
          name='OXNote',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='resources/designs/default/OXNote.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='OXNote')
app = BUNDLE(coll,
             name='OXNote.app',
             icon='resources/designs/default/OXNote.icns',
             bundle_identifier='de.bartl3by.OXNote',
             version='0.1.2')
