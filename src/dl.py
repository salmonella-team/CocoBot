import subprocess
import youtube_dl

def dlYoutube(url):
    # subprocess.run(args=["youtube-dl", "-o", "./src/%(title)s", "-f", "bestvideo+bestaudio", "--merge-output-format", "mkv", url])
    subprocess.run(args=["youtube-dl", "-o", "./src/%(title)s", "-f", "bestvideo+bestaudio", "--recode-video", "mp4", url])
    # OPTS = {
    #     "outtmpl": "{VIDEO_DIR}%(title)s".format(VIDEO_DIR="./src/"),
    #     "format": "bestvideo+bestaudio",
    #     "merge-output-format": "mkv"
    # }
    youtube = youtube_dl.YoutubeDL()
    info = youtube.extract_info(url)
    filename = info["title"] + "." + "mp4"
    return filename