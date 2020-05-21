import os, sys

import subprocess
import time

# réalise simplement ls quand on lance le programme
# subprocess.call('ls')

# pour faire une commande avec argument
# subprocess.call(['ls','-l'])
# input_choice = '0'

# if (len(sys.argv)) == 2:
#     input_choice = sys.argv[1]

# if input_choice == '1':
#     wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/andromeda_galaxy.jpg'
# elif input_choice == '2':
#     wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/353.jpg'
# elif input_choice == '0':
#     wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/128.jpg.png'
# else:
#     print("choisis 1 ou 2")

# subprocess.call(['wal', '-i', wallpaper_path])
input_choice = '0'

if (len(sys.argv)) > 1:
    print("Trop d'arguments")
    sys.exit(1)

seconds = time.time()

local_time = time.localtime(seconds)
# print(local_time)
#  structure de local_time
# time.struct_time(tm_year=2020, tm_mon=5, tm_mday=21, tm_hour=12, tm_min=12, tm_sec=42, tm_wday=3, tm_yday=142, tm_isdst=1)

print("")
local_hour = local_time.tm_hour
print(local_hour)



if (len(sys.argv)) == 1:
    if local_hour <= 6 or local_hour >= 20:
        wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/andromeda_galaxy.jpg'

    elif (local_hour >= 7 and local_hour <=9 ) or (local_hour >=17 and local_hour <= 19):
        wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/128.jpg.png'

    else :
        wallpaper_path = '/mnt/hdd/hhers/Pictures/Wallpapers/353.jpg'

subprocess.call(['wal', '-i', wallpaper_path])

# test