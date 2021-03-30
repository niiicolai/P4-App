# Dependencies
from config import ORIGINAL_NAMES, MANIPULATED_NAMES
from gui import Application

if __name__ == '__main__':
    # Create an application object
    app = Application(ORIGINAL_NAMES, MANIPULATED_NAMES, None)
    # Activate the main loop
    app.mainloop()
