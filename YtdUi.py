
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QTextEdit, 
	QLineEdit, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup, QDesktopWidget,
	QComboBox, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pytube import YouTube
import os
import sys
import values, extensions


# Allow scaling on different dpi monitors
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class YtdUi(QWidget):

	def __init__(self):
		super().__init__()
		self.initUi()


	def initUi(self):

		# Url textbox
		self.edit_url = QLineEdit()
		self.edit_url.setPlaceholderText(values.str_url)
		# Download button
		self.btn_download = QPushButton(values.str_download)
		self.btn_download.clicked.connect(self.download)
		# Url box + Download button
		self.url_layout = QHBoxLayout()
		self.url_layout.addWidget(self.edit_url)
		self.url_layout.addWidget(self.btn_download)


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
		self.vbox.addLayout(self.dl_choices_layout)


		# Set layout for the window
		self.setLayout(self.vbox)


		# Set app window positioning
		edge = values.edge_len
		self.setGeometry(edge, edge, edge, edge)
		self.setWindowTitle(values.app_name)
		self.setWindowIcon(QIcon(values.app_icon))
		self.center()

		self.show()


	def center(self):
		frameGeo = self.frameGeometry()
		center = QDesktopWidget().availableGeometry().center()
		frameGeo.moveCenter(center)
		self.move(frameGeo.topLeft())


	def download(self):
		pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	runapp = YtdUi()
	sys.exit(app.exec_())
