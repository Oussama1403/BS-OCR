from PyQt5 import QtCore, QtGui, QtWidgets
from appui import Ui_MainWindow
import pytesseract
import PIL
import sys


class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.CurrentLang = None
        self.lang = "eng"
        self.selectimageb.clicked.connect(self.setImage)
        self.imagetotextb.clicked.connect(self.ocr_core)
        self.comboBox.activated.connect(self.language)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.quit)
    def setImage(self):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "(*.png *.jpg *jpeg *.bmp)") # Ask for file
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imagelabel.width(), self.imagelabel.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imagelabel.setPixmap(pixmap) # Set the pixmap onto the label
            self.imagelabel.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center    
    
    def ocr_core(self):
        """
        This function will handle the core OCR processing of images.
        """
          
        text = pytesseract.image_to_string(PIL.Image.open(fileName),lang=self.lang)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        self.imagetext.setText(text)
    
    def language(self):
        self.CurrentLang = self.comboBox.currentText()
        
        if self.CurrentLang == 'English':
            self.lang = 'eng'
        elif self.CurrentLang == 'Français':
            self.lang = 'fra'    
        else:
            self.lang = 'ara'          
    def quit(self):
        QtWidgets.QApplication.quit()     
    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Optical Character Recognition Application\nv1.0\nDeveloper:Oussama Ben Sassi")
        msg.setInformativeText("Optical Character Recognition involves the detection of text content on images and translation of the images to encoded text that the computer can easily understand. An image containing text is scanned and analyzed in order to identify the characters in it. Upon identification, the character is converted to machine-encoded text.")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

app = QtWidgets.QApplication(sys.argv)
win = MyWindow()
sys.exit(app.exec_())