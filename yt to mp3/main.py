import os
from pathlib import Path
import yt_dlp

def get_downloads_folder():
    return str(Path.home() / "Downloads")

def baixar_e_converter(url):
    downloads = get_downloads_folder()

    ydl_opts = {
        'outtmpl': os.path.join(downloads, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'ffmpeg_location': r"C:\ffmpeg\bin\ffmpeg.exe",
        'postprocessor_args': [
            "-acodec", "libmp3lame"
        ]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Paste the URL: ")
    baixar_e_converter(url)
    print("Download complete")