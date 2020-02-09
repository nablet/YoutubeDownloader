
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QTextEdit, 
	QLineEdit, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup, QDesktopWidget,
	QComboBox, QMessageBox, QLabel, QFileDialog, QDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QDir, QStandardPaths, pyqtSlot
from pytube import YouTube
import os
import sys

from utils import values, extensions


# Allow scaling on different dpi monitors
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class YtdUi(QWidget):

	def __init__(self):

		super().__init__()
		self.initUi()

		# Set layout for the window
		self.setLayout(self.vbox)

		# Set app window positioning
		self.setGeometry(values.left, values.top, values.width, values.height)
		self.setWindowTitle(values.app_name)
		self.setWindowIcon(QIcon(values.app_icon))
		self.center()
		self.show()


	def initUi(self):

		# Url textbox
		self.edit_url = QLineEdit()
		self.edit_url.setPlaceholderText(values.str_url)
		self.edit_url.returnPressed.connect(self.download)
		# Download button
		self.btn_download = QPushButton(values.str_download)
		self.btn_download.clicked.connect(self.download)
		# Url box + Download button layout
		self.url_layout = QHBoxLayout()
		self.url_layout.addWidget(self.edit_url)
		self.url_layout.addWidget(self.btn_download)


		# Save location text
		self.text_url = QLabel(values.str_path)
		# Shown path
		self.edit_save_path = QLineEdit()
		self.edit_save_path.setText(extensions.set_path())
		# Path dialog
		self.btn_open_finder = QPushButton(values.str_folders)
		self.btn_open_finder.clicked.connect(self.open_file_dialog)
		# Save location layout
		self.path_layout = QHBoxLayout()
		self.path_layout.addWidget(self.text_url)
		self.path_layout.addWidget(self.edit_save_path)
		self.path_layout.addWidget(self.btn_open_finder)


		# Download choices box
		self.dl_choices = QTextEdit(self)
		self.dl_choices.resize(580, 80)
		self.dl_choices.setReadOnly(True)
		# Download choices box layout
		self.dl_choices_layout = QHBoxLayout()
		self.dl_choices_layout.addWidget(self.dl_choices)


		# Vertical orientation layout
		self.vbox = QVBoxLayout()
		self.vbox.addLayout(self.url_layout)
		self.vbox.addLayout(self.path_layout)
		self.vbox.addLayout(self.dl_choices_layout)


	def center(self):
		frameGeo = self.frameGeometry()
		center = QDesktopWidget().availableGeometry().center()
		frameGeo.moveCenter(center)
		self.move(frameGeo.topLeft())


	@pyqtSlot()
	def open_file_dialog(self, directory=values.default_save_path, callback=None):
		self.dialog = QFileDialog()
		self.dialog.setFileMode(QFileDialog.DirectoryOnly)
		self.dialog.setAcceptMode(QFileDialog.AcceptOpen)
		self.dialog.setDirectory(directory)

		if self.dialog.exec_() == QDialog.Accepted:
			self.edit_save_path.setText(self.dialog.selectedFiles()[0])


	@pyqtSlot()
	def download(self):
		print("On Click download")



if __name__ == '__main__':
	app = QApplication(sys.argv)
	runapp = YtdUi()
	sys.exit(app.exec_())
