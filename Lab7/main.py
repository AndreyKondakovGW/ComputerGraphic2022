import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Lab7.ui import UI7

if __name__ == '__main__':
    ui = UI7()
    ui.run()