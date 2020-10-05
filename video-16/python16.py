# pip install pytube
# pip install pytube3

import pytube
link = input('enter the link of videos...')
print('downloading....')
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
print('task  complete')

