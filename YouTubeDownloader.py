# https://pytube.io/en/latest/
from pytube import YouTube
import os 


link = input("Add YouTube Link: ")
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd = yt.streams.get_by_itag(22)
print(yt.title)
print(yd)
folderName = 'videos'

if not os.path.exists(folderName):
    os.mkdir(folderName)
    # ADD FOLDER HERE
    yd.download(folderName)
else:
    # ADD FOLDER HERE
    yd.download(folderName)