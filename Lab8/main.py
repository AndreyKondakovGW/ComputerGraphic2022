import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from Lab8.ui import UI8

if __name__ == '__main__':
    ui = UI8()
    ui.run()