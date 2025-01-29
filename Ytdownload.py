import os
try:
	from pytube import YouTube
except:
	try:
		os.system('pip3 install pytube')
	except:
		os.system('sudo apt install pip')

def getFormat():
	d=[140,18,397,22]
	print('''	0 or emtpy --> mp3
			1 --> mp4 360
			2 --> mp4 480
			3 --> mp4 720''')
	n=input("Enter the choice:")
	if n=='':
		return 140
	n=int(n)
	return d[n]
	

def downloadmp3(link):

    
    yt=YouTube(link)
    print("To download in specific format\nEnter the number in following way:")
    f=getFormat()
    '''
    18--> mp4 360p
    397--> mp4 480p
    22--> mp4 720p
    140--> mp3'''
    name=(yt.title).replace('|','').replace(",",'').replace("/",'').replace(":",'').replace(".","")

    #'Dil Lutiya  Jazzy B  Ft. Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'
    #'Dil Lutiya  Jazzy B  Ft Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'

    print("\n"+name)
    while yt.streams.get_by_itag(f) is None:
    	print("Not available in this format try again with another")
    	f=getFormat()
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
    	return 
    
    cmd='mv "%s.mp4" /home/$USERNAME/Videos/'%name
    print("Conversion completed!!!\n Moving the Video...")
    os.system(cmd)

link=input("Enter the Link: $ ")
downloadmp3(link)
