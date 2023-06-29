from tkinter import *
import pygame 
from tkinter import filedialog
import os

player = Tk()
player.title("Music Player")
player.geometry("500x300")

pygame.mixer.init()

#creating memubar
menubar = Menu(player)
player.config(menu=menubar)

songs=[]
current_song= ""
paused = False

def load_music():
    global current_song
    player.directory=filedialog.askdirectory()

    for song in os.listdir(player.directory):
        name, ext=os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        music_box.insert("end", song)

    music_box.selection_set(0)
    current_song = songs[music_box.curselection()[0]]

#adding songlist to memubar
song_list = Menu(menubar , tearoff=False)
song_list.add_command(label='Selet Folder',command=load_music)
menubar.add_cascade(label='SongList',menu=song_list)

def play():
   global current_song, paused
   if not paused:
        pygame.mixer.music.load(os.path.join(player.directory,current_song))
        pygame.mixer.music.play()
   else:
       pygame.mixer.music.unpause()
       paused=False

def stop():
    pygame.mixer.music.stop()
    music_box.selection_clear(ACTIVE) 

def pause():
    global paused
    pygame.mixer.music.pause()
    paused = True

music_box = Listbox(player, bg= "black", fg = "green", width=60)
music_box.pack(pady=20)

#creating control buttons
control_frame= Frame(player)
control_frame.pack()

play_btn=Button(control_frame,width=5,height=3,text="PLAY",bg="green",fg="white", borderwidth=0, command=play)
stop_btn=Button(control_frame,width=5,height=3,text="STOP",bg="red",fg="white", borderwidth=0, command=stop)
pause_btn=Button(control_frame,width=5,height=3,text="PAUSE",bg="blue",fg="white", borderwidth=0,command=pause )

play_btn.grid(row=0 , column=1 ,padx=15)
stop_btn.grid(row=0 , column=2 ,padx=15) 
pause_btn.grid(row=0 , column=0 ,padx=15)


player.mainloop()
