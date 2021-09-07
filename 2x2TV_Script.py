import time
import subprocess
import sys

print(int(time.time()) + 3000)
href = "https://bl.zxz.su/live/317805/HLS/4614144_3,2883584_2,1153024_1/" + str(int(time.time()) + 3000) + "/9ffdf74b4268d28648f06f10aa5e4aa5/playlist.m3u8"

with open('2x2.ts', 'w') as ouf:
    ouf.write(
'''#EXTM3U
#EXTINF:28,playlist.m3u8
#EXTVLCOPT:network-caching=1000
''' + href)

opener = "open" if sys.platform == "darwin" else "xdg-open"

subprocess.call([opener, '2x2.ts'])