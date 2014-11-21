import youtube_dl
def download(src):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
        #ydl.download(['https://www.youtube.com/watch?v=S7GjduKOils'])
        ydl.download([src])
