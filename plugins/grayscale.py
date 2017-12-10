from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QColor

# Create our custom QPushButton widget class called main (necessary)
class main(QPushButton):

    # Initialize widget
    # Stuff is QLabel from main window
    def __init__(self, stuff):
        
        super().__init__()
        # Set width
        self.setMinimumWidth(70)
        self.setText('Grayscale')
        
        # Make a connection to click event
        self.clicked.connect(lambda: self.action(stuff))
    
    # Action for click event
    def action(self, stuff):
        
        # Try to convert image to pixmap or ignore if there is no image
        try:
            image = stuff.pixmap().toImage()
        except:
            return None
        
        # Now make it all gray
        for i in range(image.width()):
            for j in range(image.height()):
                # Create a temporary variables
                # Color
                color = image.pixelColor(i, j).getRgb()
                # Alpha
                alpha = color[3]
                # Gray color will be arithmetic mean of all colors in pixel
                gray = int((color[0] + color[1] + color[2]) / 3)
                # Apply new color to current pixel
                image.setPixel(i, j, QColor(gray, gray, gray, alpha).rgba())
        
        # Show new image
        stuff.setPixmap(QPixmap.fromImage(image))