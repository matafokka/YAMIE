# YAMIE
Yet Another Modular Image Editor -- project for article.
This application is a modular image viewer and editor written with Python 3 and Qt and used to write an article for university. It consist from core and modules. Each module is custom Qt widget placed on the top of window. It takes QLabel (widget that shows image) as parameter.

You can easily write your own module using this sample:
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
