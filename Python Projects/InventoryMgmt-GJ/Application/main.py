#importing everythng we need
from PySide6.QtWidgets import QApplication, QWidget

#importing sys module
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()



# Start the app
app.exec()