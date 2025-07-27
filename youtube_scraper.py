import yt_dlp

video_url = input("Enter the YouTube video URL: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=False)
    
    print("\n🎬 Video Information:")
    print("Title      :", info.get('title'))
    print("Views      :", info.get('view_count'))
    print("Duration   :", info.get('duration'), "seconds")
    print("Description:", info.get('description')[:300], "...")
    print("Uploader   :", info.get('uploader'))
