# -*- coding: utf-8 -*-
import sys
# For recursive module import
import importlib
# For creating instances of Qt widgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
# For creating pixmaps
from PyQt5.QtGui import QPixmap, QImage
# For loading ui file
from PyQt5 import uic

# Main window of application
class Window(QMainWindow):
    
    # Initialize application
    def __init__(self):

        # Make our app super awesome
        super().__init__()
        # Load UI from file
        uic.loadUi('ui/mainwindow.ui', self)
        # Connect events
        self.buttonOpen.clicked.connect(self.onOpen)
        self.buttonSave.clicked.connect(self.onSave)
        
        # Set default image
        self.Image.setPixmap(QPixmap('logo.png'))
        
        # Add modules
        # Open file with list of modules
        list = open('plugins/plugins.cfg', 'r')
        # Add each listed module
        for line in list:
            if line[0] != '#':
                # Remove \n from the end of the line
                # There will be no other such characters so we can use this simple method
                line = line.replace('\n', '')
                # Create an instance of module and give argument self as parent
                module = importlib.import_module('plugins.' + line).main(self)
                # Set unified height to all modules
                module.setMaximumHeight(48)
                # Put this module on the top
                self.layoutOnTop.addWidget(module)
        # Add strecth to top layout to nice look
        self.layoutOnTop.addStretch()

    # When open button has been pressed
    def onOpen(self):

        # Open file dialog and get path
        file = QFileDialog.getOpenFileName(self, 'Open image', '', 'Image files (*.jpg *.png *.bmp);;All files (*)')[0]

        # Create a pixmap from file
        img = QPixmap(file)

        # Check if it's an image
        if img.isNull() == False:
            # Set pixmap to label
            self.Image.setPixmap(img)

        elif file != "":
            # If it's not image and user didn't press 'Cancel' raise an error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Wrong file type")
            msg.setText("It's not an image. Please, open an image file.")
            msg.exec_()

    # When save button has been pressed
    def onSave(self):

        # Open file dialog and get path
        file = QFileDialog.getSaveFileName(self, 'Save image', '', '*.jpg;;*.png;;*.bmp;;Another type (*)')[0]

        # Get file type from file
        ftype = ''
        for i in range(len(file) - 1, -1, -1):
            if file[i] == '.':
                break
            else:
                ftype += file[i]
        # Reverse string and make it in uppercase for saving
        ftype = ftype[::-1].upper()

        # Finally save image
        try:
            self.Image.pixmap().save(file, ftype)
        except:
            # Or print an error message if something went wrong
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("Cannot save an image.")
            msg.exec_()

# In main thread execute app
if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Create an instance of our Window class
    window = Window()
    # Show window
    window.show()
    # Execute app and also write action for exiting
    sys.exit(app.exec_())
