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
        self.setMinimumWidth(60)
        self.setText('Sepia')
        
        # Make a connection to click event
        self.clicked.connect(lambda: self.action(parent))
    
    # Action for click event
    def action(self, parent):
        
        # Try to convert image to pixmap or return None if no image has been loaded
        try:
            image = parent.Image.pixmap().toImage()
        except:
            return None
        
        # Now make sepia
        for i in range(image.width()):
            for j in range(image.height()):
                # Create a temporary variables
                # Color
                color = image.pixelColor(i, j).getRgb()
                # Alpha
                alpha = color[3]
                # sepia will be arithmetic mean of red and green
                # and applied to these color respectively
                # It's like a grayscale but for two colors
                sepia = int((color[0] + color[1]) / 2)
                # This is for blue color. If it's less than other colors
                # pixel will be with yellow shade.
                # If it's more then set it equal to sepia.
                # After that there will be only yellow and gray pixels.
                blue = int((color[0] + color[1] + color[2]) / 3)
                if blue > sepia:
                    blue = sepia
                # Apply new color to current pixel
                image.setPixel(i, j, QColor(sepia, sepia, blue, alpha).rgba())
        
        # Show the new image
        parent.Image.setPixmap(QPixmap.fromImage(image))
