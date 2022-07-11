import os
import shutil

folder = r"E:\Gurov_SSD_256\My_docs\Miscellanea_private\Pictures"
subfolders = [f.path for f in os.scandir("E:\Gurov_SSD_256\My_docs\Miscellanea_private\Pictures") if f.is_dir()]

for sub in subfolders:
    for f in os.listdir(sub):
        src = os.path.join(sub, f)
        dst = os.path.join(folder, f)
        shutil.move(src, dst)