import yt_dlp

filesize = []

def Download(link):

    def progress_hook(d):
        if d['status'] == 'finished':
            print(f"Downloading: {d['filename']}, size: {d['total_bytes']} bytes")
            filesize.append(d['total_bytes'] / 1024 / 1024)

    ydl_opts = {
        'quiet': True,
        'progress_hooks': [progress_hook]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            print(f"Download was completed successfully for: {info_dict['title']}")
    except Exception as e:
        print("An error has occurred:", e)

links = [
    "https://www.youtube.com/watch?v=7Eeo-82Eac8"
]

for l in links: 
    Download(l)

total_size = sum(filesize)
print(f"Total size downloaded: {total_size:.2f} MB")