
from Utils import extensions
from pytube import YouTube
import Ytd


class YtdController(object):

	def __init__(self, view):
		self.view = view


	def get_streams(self, url):
		streams = YouTube(url).streams.all()

		stream_list = []
		for i in range(0, len(streams) - 1):
			s = streams[i]
			stream_info = f"{i+1}. "				# count
			stream_info += f"res={s.resolution} "	# res
			stream_info += f"size={extensions.humanbytes(s.filesize)} "	# size
			stream_info += f"type={s.mime_type} "	# type
			stream_list.append(stream_info)

		self.view.show_streams(stream_list)
		

	def start_download(self, url, path):

		yt = YouTube(url, self.view.on_download_progress, self.view.on_download_complete)
		stream = yt.streams.first()
		
		title 	= yt.title
		length 	= f"{int(yt.length) // 60}:{int(yt.length) % 60}"
		size 	= extensions.humanbytes(stream.size)
		# length = "placeholder length"
		# size = "placeholder size"
		thumb 	= yt.thumbnail_url
		self.view.on_download_start(title, length, size, thumb)

		# stream.download(path)


	def download(self, stream):
		print(f"Downloading {stream}")
