import os
try:
	from pytube import YouTube
except:
	try:
		os.system('pip3 install pytube')
	except:
		os.system('sudo apt install pip')


'''
    18--> mp4 360p
    397--> mp4 480p
    22--> mp4 720p
    140--> mp3'''
def download(link,f):

    
    yt=YouTube(link)
    name=(yt.title).replace('|','').replace(",",'').replace("/",'').replace(":",'').replace(".","")

    #'Dil Lutiya  Jazzy B  Ft. Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'
    #'Dil Lutiya  Jazzy B  Ft Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'

    print("\n"+name)
    assert yt.streams.get_by_itag(f) is not None, "Not available in this format try again with another"

    print("Downloading in process...")
    yt.streams.get_by_itag(f).download()
    
    print("File Downloaded...")

    if f==140:
        cmd1='mv "%s.mp4" "%s.m4a"'%(name,name)
        cmd2='ffmpeg -v 5 -y -i "%s.m4a" -acodec libmp3lame -ac 2 -ab 192k "%s.mp3"'%(name,name)
        cmd3='mv "%s.mp3" /home/$USERNAME/Music/'%name
        cmd4='rm -f "%s.m4a"'%name
        os.system(cmd1)
        print("Conversion part 1 completed.\n Proceeding to further conversion...")
        
        os.system(cmd2)
        print("Conversion completed!!!\n Moving the audio...")
        
        os.system(cmd3)
        print("Song ready to play!!!\n Cleaning the spattered shit now...")
        os.system(cmd4)
        return 100
    
    cmd='mv "%s.mp4" /home/$USERNAME/Videos/'%name
    print("Conversion completed!!!\n Moving the Video...")
    os.system(cmd)
    
    
    return 100
