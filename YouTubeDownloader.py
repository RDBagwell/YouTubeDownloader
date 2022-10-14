# https://pytube.io/en/latest/
from pytube import YouTube

link = input("Add YouTube Link: ")
yt = YouTube(link)

# yd = yt.streams.get_highest_resolution()
yd = yt.streams.get_by_itag(22)
print(yt.title)
print(yd)

# ADD FOLDER HERE
yd.download('./')
