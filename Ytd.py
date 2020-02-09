
"""

	Jayson Manlapaz Tiongco
	Project reopened February 9, 2020

	- Python   :  3.8.1
	- PyQt5    :  5.14.1
	- pytube3  :  9.6.0
	
	Architecture : MVP

"""


from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QTextEdit, 
	QLineEdit, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel, QFileDialog, QDialog,
	QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot

from Utils import values, extensions
import YtdC
import os
import sys

test_url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'


# Allow scaling on different dpi monitors
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class YtdUi(QWidget):

	def __init__(self):

		super().__init__()
		self.controller = YtdC.YtdController(self)
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
		self.edit_url = QLineEdit(test_url)
		self.edit_url.setPlaceholderText(values.str_url)
		self.edit_url.returnPressed.connect(self.on_click_download)
		# Download button
		self.btn_download = QPushButton(values.str_download)
		self.btn_download.clicked.connect(self.on_click_download)
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

		# Download info box
		# self.text_info = QTextEdit()
		# self.text_info.setReadOnly(True)
		# self.text_info.resize(1, 1)
		# self.text_info_layout = QHBoxLayout()
		# self.text_info_layout.addWidget(self.text_info)


		# Download choices box layout
		self.info_layout = QVBoxLayout()


		# Vertical orientation layout
		self.vbox = QVBoxLayout()
		self.vbox.setAlignment(Qt.AlignTop)
		self.vbox.addLayout(self.url_layout)
		self.vbox.addLayout(self.path_layout)
		# self.vbox.addLayout(self.text_info_layout)
		self.vbox.addLayout(self.info_layout)


	def center(self):
		frameGeo = self.frameGeometry()
		center = QDesktopWidget().availableGeometry().center()
		frameGeo.moveCenter(center)
		self.move(frameGeo.topLeft())


	##### OnClick Functions #####

	@pyqtSlot()
	def open_file_dialog(self, directory=values.default_save_path, callback=None):
		self.dialog = QFileDialog()
		self.dialog.setFileMode(QFileDialog.DirectoryOnly)
		self.dialog.setAcceptMode(QFileDialog.AcceptOpen)
		self.dialog.setDirectory(directory)

		if self.dialog.exec_() == QDialog.Accepted:
			self.edit_save_path.setText(self.dialog.selectedFiles()[0])


	@pyqtSlot()
	def on_click_download(self):
		url = self.edit_url.text()
		path = self.edit_save_path.text()
		self.controller.get_streams(url)


	# @pyqtSlot()
	# def download_stream(self, stream):


	#### Download Info Functions ####

	def show_streams(self, streams):
		for stream in streams:
			self.stream_data = QLabel(str(stream))

			self.btn_download_stream = QPushButton(values.str_download)
			self.btn_download_stream.clicked.connect(
				lambda onClick, stream=stream: self.controller.download(stream))
			
			self.stream_data_layout = QHBoxLayout()
			self.stream_data_layout.addWidget(self.stream_data)
			self.stream_data_layout.addWidget(self.btn_download_stream)

			self.info_layout.addLayout(self.stream_data_layout)


	def show_video_info(self, title: str, length: str, size: str, thumbnail_url: str):
		dl_info = f"Downloading\n"
		dl_info += f"Title: {title}\n"
		dl_info += f"Length: {length}\n" 
		dl_info += f"Download Size: {size}\n" 
		dl_info += f"Image Url: {thumbnail_url}\n"

		self.dl_info.setText(dl_info)


	def on_download_progress(self, stream, chunk, file_handle, bytes_remaining):
		total_size = stream.filesize
		downloaded_size = total_size - bytes_remaining
		progress = downloaded_size / total_size * 100
		print('{:.3f}%'.format(progress), end='\r')


	def on_download_complete(self, stream, file_handle):
		print("DOWNLOAD FINISHED.\n", end='\r')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	runapp = YtdUi()
	sys.exit(app.exec_())
