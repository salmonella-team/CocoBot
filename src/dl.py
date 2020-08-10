import youtube_dl

def dlYoutube(url):
    OPTS = {
        "outtmpl": "{VIDEO_DIR}%(id)s".format(VIDEO_DIR="./tmp/"),
    }
    youtube = youtube_dl.YoutubeDL(OPTS)
    info = youtube.extract_info(url)
    print(info)
    filename = info["id"]
    filename = filename.replace('/', '_')
    return filename