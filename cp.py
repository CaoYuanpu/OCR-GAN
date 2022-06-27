import os
import shutil

root = './lib/data/metal_nut/test'

# bad_paths = [os.path.join(root, p) for p in os.listdir(root) if p != 'good' and p != '.DS_Store']

bad_paths = ['./lib/data/metal_nut/test/color', './lib/data/metal_nut/test/flip', './lib/data/metal_nut/test/scratch', './lib/data/metal_nut/test/bent']

cp_path = './lib/data/metal_nut/test/bad'

i = 0
for p in bad_paths:
    num = len(os.listdir(p))
    for j in range(num):
        src = os.path.join(p, f"{str(j).rjust(3, '0')}.png")
        des = os.path.join(cp_path, f"{str(i).rjust(3, '0')}.png")
        shutil.copy(src, des)
        i += 1
        
