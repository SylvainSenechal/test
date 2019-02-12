import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

	#############
	def __init__(self):
		print("constructeur de la class MainWindow")
		QMainWindow.__init__(self)

		bar = self.menuBar()
		fileMenu = bar.addMenu("File")

		openAction = QAction(QIcon("./new.png"), "New..", self)
		openAction.setShortcut( QKeySequence("Ctrl+N" ) )
		openAction.setToolTip("New File")
		openAction.setStatusTip("New file")
		fileMenu.addAction(openAction)
		openAction.triggered.connect( self.open )

		saveAction = QAction(QIcon("./save.png"), "Save..", self)
		saveAction.setShortcut( QKeySequence("Ctrl+S" ) )
		saveAction.setToolTip("Save File")
		saveAction.setStatusTip("Save file")
		fileMenu.addAction(saveAction)
		saveAction.triggered.connect( self.save )

		quitAction = QAction(QIcon("./quit.png"), "Quit..", self)
		quitAction.setShortcut( QKeySequence("Ctrl+Q" ) )
		quitAction.setToolTip("Quit File")
		quitAction.setStatusTip("Quit file")
		fileMenu.addAction(quitAction)
		quitAction.triggered.connect( self.quit )

		fileToolBar = QToolBar("File")
		fileToolBar.addAction(openAction)
		fileToolBar.addAction(saveAction)
		fileToolBar.addAction(quitAction)
		self.addToolBar(fileToolBar)

		statusB = QStatusBar()
		self.setStatusBar(statusB)

		self.textEdit = QTextEdit(self)
		self.setCentralWidget(self.textEdit)

	###############
	def closeEvent(self, event):
		event.ignore()
		self.quit()
	def quit(self):
		print("Quit")
		msg = QMessageBox()
		msg.setInformativeText("Do you want to quit ?")
		msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		response = msg.exec_()
		if (response == QMessageBox.Ok):
			QApplication.quit()

	###############
	def open(self):
		print("Open")
		fileName = QFileDialog.getOpenFileName(self, "open Image")
		print(fileName[0])
		txt = open(fileName[0])
		self.textEdit.setPlainText(txt.read())

	###############
	def save(self):
		print("Save")
		fileName = QFileDialog.getOpenFileName(self, "open Image")
		print(fileName)
		txt = open(fileName[0])
		self.textEdit.setPlainText(txt.read())


def main(args):
	print("Hello World")

	myApp = QApplication(args)
	window = MainWindow()
	window.show()
	myApp.exec_()
if __name__ == "__main__":
	main(sys.argv)
