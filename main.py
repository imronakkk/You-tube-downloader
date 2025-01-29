from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget,QHBoxLayout,QComboBox
import os
from pytube import YouTube

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YTDownload")

        self.inp= QLineEdit()
        self.inp.setPlaceholderText("Enter Youtube Link")
        self.inp.textChanged.connect(self.on_btn)
        
        self.type = QComboBox()
        self.type.addItems( ["Mp3","Mp4 360p","Mp4 480p","Mp4 720p"])
        
        self.btn = QPushButton("Download!")
        self.btn.setEnabled(False)
        self.btn.clicked.connect(self.btn_fire)

        

        self.label=QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setText("Welcome!!\n")

        self.box1=QHBoxLayout()
        self.box1.addWidget(self.inp)
        self.box1.addWidget(self.type)
        
        box = QVBoxLayout()





        box.addWidget(self.label)
        box.addLayout(self.box1)
        box.addWidget(self.btn)
        
        container = QWidget()
        container.setLayout(box)

        self.setFixedSize(QSize(450, 100))
	
        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def on_btn(self):
        self.btn.setEnabled(True)
        self.btn.setText("Download")
        pass
    def btn_fire(self):
        self.btn.setEnabled(False)
        d=[140,18,397,22]
        t=self.inp.text()
        f=self.type.currentIndex()
        print(t,d[f],f)
        down=self.download(t,d[f])
        
        if down==100:
                self.changebtn("Download Complete")
                self.type.currentIndexChanged.connect(self.on_btn)
    
    def changebtn(self,t):
        self.btn.setText(t)
        return 0
    
    def download(self,link,f):
        yt=YouTube(link)
        name=(yt.title).replace('|','').replace(",",'').replace("/",'').replace(":",'').replace(".","")

        #'Dil Lutiya  Jazzy B  Ft. Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'
        #'Dil Lutiya  Jazzy B  Ft Apache Indian  Sukshinder  Romeo  Jihne Mera Dil Luteya  Punjabi Hits.mp4'

        print("\n"+name)
        assert yt.streams.get_by_itag(f) is not None, "Not available in this format try again with another"

        print("Downloading in process...")
        
        self.changebtn("Downloading in process...")
        
        yt.streams.get_by_itag(f).download()
        
        print("File Downloaded...")
        self.changebtn("Downloaded. Converting now...")

        if f==140:
            cmd1='MOVE "%s.mp4" "%s.m4a"'%(name,name)
            cmd2='ffmpeg -v 5 -y -i "%s.m4a" -acodec libmp3lame -ac 2 -ab 192k "%s.mp3"'%(name,name)
            cmd3='MOVE "%s.mp3" /home/ronne/Music/'%name
            cmd4='del /f "%s.m4a"'%name
            os.system(cmd1)
            print("Conversion part 1 completed.\n Proceeding to further conversion...")
            
            os.system(cmd2)
            print("Conversion completed!!!\n Moving the audio...")
            
            os.system(cmd3)
            print("Song ready to play!!!\n Cleaning the spattered shit now...")
            self.changebtn("Process Completed!!!")
            os.system(cmd4)
            return 100
        
        cmd='MOVE "%s.mp4" /home/ronne/Videos/'%name
        print("Conversion completed!!!\n Moving the Video...")
        os.system(cmd)
        self.changebtn("Process Completed!!!")
        return 100
            


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
