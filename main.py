from pytube import YouTube

filesize = []

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    filesize.append(youtubeObject.filesize_mb)
    try:
        print("downloading: ", youtubeObject.title, ", size: ", youtubeObject.filesize_mb, "MB")
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download was completed successfully")


links = []
for l in links: 
    Download(l)

print("Total size downloaded: ", sum(filesize), "MB")
filesize.clear()
