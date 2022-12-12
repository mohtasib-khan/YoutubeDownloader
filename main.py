from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("ERROR 404")
  print("Download Complete Buddy!")

link = input("Paste your link here! URL: ")
Download(link)