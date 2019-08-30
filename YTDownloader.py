
# WORK IN PROGRESS...
# planning to use QtPy or tkinter to make gui

from pytube import YouTube
import os


def humanbytes(B):
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


def progress_callback(stream, chunk, file_handle, bytes_remaining):
    # this function is called by download process... do not call directly!
    total_size = stream.filesize
    downloaded_size = total_size - bytes_remaining
    progress = downloaded_size / total_size * 100
    print('{:.3f}%'.format(progress), end='\r')


def complete_callback(stream, file_handle):
    # this function is called by download process... do not call directly!
    # do nothing but print newline
	print("DOWNLOAD FINISHED.\n", end='\r')
	os.system('pause')


print("\n=================== nablet's YoutubeDownloader (saves in desktop) ===================")
while True:
   url = input("Enter video url: ")

   try:
           yt = YouTube(url, on_progress_callback=progress_callback, on_complete_callback=complete_callback)
           print("\nTitle: " + str(yt.title), end='\n')
   except:
           print("Invalid link. Restart program...")
           os.system('pause')
           exit()

   stream = yt.streams.all()

   for i in range(1, len(stream)):
           print(str(i)+". "+str(stream[i - 1]))

   try:
           choice = int(input("\nEnter number: "))
   except:
           print("\nInvalid input. Restart program...")

   if choice:
           size = stream[choice - 1].filesize
           mins = int(yt.length) // 60
           seconds = int(yt.length) % 60

           print("\n")
           print("Thumbnail URL: " + yt.thumbnail_url)
           print(str(stream[choice-1]))
           print("Downloading: " + str(yt.title))
           print("Length: " + str(mins) + ":" + str(seconds))
           print("File size: " + str(humanbytes(size)))
           print("\n")

           stream[choice - 1].download(os.path.expanduser("~/Desktop"))

