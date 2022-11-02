import os
import sys

current_dir = os.getcwd()
models_dir = os.path.join(current_dir, 'Lab7', 'models')
path = os.path.join(models_dir, 'Dodecahedron.stl')

with open(path, "r") as f:
    print(f.read())