import yt_dlp

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


print("Digite o link do vídeo: ");

video_url = input();

download_video(video_url);
