# Deprecated

I'm ashamed of this project. Still keeping it visible for future laughs.

# YAMIE
Yet Another Modular Image Editor – project for an article.

This application is a modular image viewer and editor written with Python 3 and Qt and used to write an article for university. It consist from core and modules. Each module is custom QWidget placed on the top of window. It takes QLabel (widget that shows image) as parameter.

Structure of program:

YAMIE.py – core

ui/mainwindow.ui – UI file for core (main window)

img/ – directory for images

plugins/ – directory for modules

plugins/plugins.cfg – file for enabling/disabling modules. Only modules listed in this file will load.


To add new modules put them in "plugins" folder and list them in plugins.cfg in a new line. To disable module just add a character "#" in the beginning. Maybe in future I'll write a GUI window to arrange and enable/disable modules.

You can easily write your own module using this sample or look up into already made modules. As listed above, module should be a custom QWidget class:
```python
# Import your stuff
from PyQt5.QtWidgets import QPushButton
# And import QPixmap so you can set a pixmap to the label
from PyQt5.QtGui import QPixmap

# Create custom QPushButton widget class called main (necessary)
class main(QPushButton):

    # Initialize widget
    # Stuff is QLabel from main window
    def __init__(self, stuff):
        
        # Use it to work with Qt objects
        super().__init__()
        # Initialize appearance of widget
        # ...
        # Make connections to your events event
        # There is clicked event that sends QLabel to it's linked method action
        self.clicked.connect(lambda: self.action(stuff))
    
    # Action for event
    def action(self, stuff):
        
        # Try to convert image to pixmap or return nothing if there is no image
        try:
            image = stuff.pixmap().toImage()
        except:
            return None
        
        # Do some stuff
        # ...
        
        # Show the new image
        stuff.setPixmap(QPixmap.fromImage(image))
        # And return None
        return None
```
