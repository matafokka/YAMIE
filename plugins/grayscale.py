# For creating class
from PyQt5.QtWidgets import QPushButton
# For converting
from PyQt5.QtGui import QPixmap, QColor

# Create our custom QPushButton widget class called main (necessary)
class main(QPushButton):

    # Initialize widget
    # Parent is application main window
    def __init__(self, parent):
        
        # Make our module super awesome
        super().__init__()
        # Set width of this widget (self)
        self.setMinimumWidth(70)
        # Set text on button
        self.setText('Grayscale')
        
        # Make a connection to click event
        self.clicked.connect(lambda: self.action(parent))
    
    # Action for click event
    def action(self, parent):
        
        # Try to convert image to pixmap or return None if no image has been loaded
        try:
            image = parent.Image.pixmap().toImage()
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
        
        # Show the new image
        parent.Image.setPixmap(QPixmap.fromImage(image))
