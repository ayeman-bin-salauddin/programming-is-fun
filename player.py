import pygame
import tkinter as tkr


#Create Window

player = tkr.Tk()
player.title('Audio Player')
player.geometry('205x340')

#Get Sond

files = r'C:\Users\ayema\Downloads\dance_til_we_die.mp3'

#Action Event

def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(files)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

#Register Buttons

button1 = tkr.Button(player, width = 5, height = 3, text = 'PLAY' , command = play)
button1.pack(fill = 'x')
button2 = tkr.Button(player, width = 5, height = 3, text = 'STOP' , command = stop)
button2.pack(fill = 'x')

#Song name

label1 = tkr.LabelFrame(player, text='Song Name')
label1.pack(fill= 'both', expand='yes')
contents1 = tkr.Label(
    tkr.Label(label1, text='YouTube')
)


#Activate

player.mainloop()