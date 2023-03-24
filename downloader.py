from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()
    except:
        print("An Error has occurred")
    
    print("Downloaded Successfully!")

link = input("Enter the YouTube video URL: ")
Download(link)