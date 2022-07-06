# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Chat_Espaco_de_Tuplas.py'],
             pathex=[],
             binaries=[],
             datas=[('recursos/icone.ico','recursos'),('recursos/gifs/chat_bubble_GIF.gif','recursos/gifs'),('recursos/botao_Entrar.png','recursos'),('recursos/botao_Conversar.png','recursos'),('recursos/botao_mandar_msg.png','recursos'),('recursos/bg_usuario_lobby.png','recursos'),('recursos/bg_usuario_Chat.png','recursos'),('recursos/bg_configurar_Usuario.png','recursos'),('recursos/botao_Conversar_privado.png','recursos'),('recursos/bg_Gera_Usuario.png','recursos'),('recursos/botao_gerar_Usuario.png','recursos'),('recursos/bg_nome_repetido_warning.png','recursos'),('recursos/bg_nome_repetido_sala_warning.png','recursos'),('recursos/botao_Ok.png','recursos'),('recursos/chat_bubble_ICON.png','recursos')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Chat_Espaco_de_Tuplas',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
