import PyInstaller.__main__

PyInstaller.__main__.run([
    '飞机大战.py',  # 主游戏文件的名称（假设为 game.py）
    '--onefile',  # 打包为单个可执行文件
    '--noconsole'  # 不显示控制台窗口
])