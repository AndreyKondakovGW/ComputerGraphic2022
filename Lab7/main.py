import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Lab6.ui3D import UI3D

if __name__ == '__main__':
    ui = UI3D()
    ui.run()