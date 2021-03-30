# Dependencies
from config import ORIGINAL_NAMES, MANIPULATED_NAMES
from gui import Application

# THE WAVE GRAPH DISPLAY CAN BE
# ACTIVATED FOR DEBUGGING PURPOSE
GRAPH_AUDIO = False

if __name__ == '__main__':
    # Create an application object
    app = Application(ORIGINAL_NAMES, MANIPULATED_NAMES, GRAPH_AUDIO)
    # Activate the main loop
    app.mainloop()
