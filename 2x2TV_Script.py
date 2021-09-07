import time
import subprocess
import sys
import os

print(int(time.time()) + 3000)
href = "https://bl.zxz.su/live/317805/HLS/4614144_3,2883584_2,1153024_1/" + str(int(time.time()) + 3000) + "/9ffdf74b4268d28648f06f10aa5e4aa5/playlist.m3u8"

with open('2x2.ts', 'w') as ouf:
    ouf.write(
'''#EXTM3U
#EXTINF:28,playlist.m3u8
#EXTVLCOPT:network-caching=1000
''' + href)

if sys.platform == 'linux':
    subprocess.call(["xdg-open", '2x2.ts'])
elif sys.platform == 'win32':
    os.startfile('2x2.ts')
else:
    subprocess.call(["open", '2x2.ts'])