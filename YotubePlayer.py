import webbrowser
from pytube import YouTube, Playlist, Search

# .Input youtube url 
url = input("Paste your youtube URL!: " )
pl = False

####################################################
# .Search youtube url instead
#watch = ("hello kitty")
#s = Search(watch)
#x = 1
#for choice in s.results: 
#  print(choice.title, ' [', x, ']')
#  x += 1
#q = input("Which index of search is your choice?: ")
#qF = int(q)
#selection = s.results[qF]
#print(selection.video_id)
####################################################

# .Youtube links tend to have "list" in their link when addressed as a playlist
if 'list' in url:  
    Video = Playlist(url)
    pl = True
else:
    Video = YouTube(url)

# .Obtain Video Title
Title = Video.title

# .if playlist, for each link in the playlist, play playlist and print video title 
if pl:

    print("This is a playlist!")
    print("We're watching:", Title)

    webbrowser.open(url)

    # .set each youtube link as a Youtube Object to use pytube API in order to identify the youtube title
    print("Youtube Videos Included: ")
    for link in Video.video_urls:

        vid = YouTube(link)
        print(vid.title)
    
# .Not a playlist, just play the video and print video title
else: 
    print("We're Watching:", Title)
    webbrowser.open(url)