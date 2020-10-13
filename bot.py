from __future__ import unicode_literals
from gtts import gTTS 
import os
import youtube_dl
import urllib
import shutil
import urllib
import youtube_dl
import random
import platform
import speedtest
from tkinter import *
import calendar
import pyaudio
from playsound import playsound
import speech_recognition as sr
root=Tk()
root.configure(bg='#4b7fa4')
def send():
    def voice(text):
        language = 'en'
        
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        playsound('text.mp3')
        os.remove("text.mp3")

    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        a.delete(0,END)
        text.insert(END,"\n"+ "Bot: Hello")
        text1="Hello"
        voice(text1)
        text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")

    elif(a.get()=='hello'):
        a.delete(0,END)
        text.insert(END,"\n"+ "Bot: Hi")
        text2="Hi"
        voice(text2)
        text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")


    elif(a.get()=='how are you'):
        a.delete(0,END)
        text.insert(END,"\n"+ "Bot:I am fine. How are you ?")
        text3="I am fine. How are you"
        voice(text3)
        text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")


    elif(a.get()=='I am fine'):
        a.delete(0,END)
        text.insert(END,"\n"+ "Bot:Nice to hear that.")
        text4="Nice to hear that"
        voice(text4)
        
    elif(a.get()=='what can you do'or a.get()=='?'):
        a.delete(0,END)
        text.insert(END,"\n"+"Bot:\n1.Generate Password\n2.Get system information\n3.To check your internet speed\n4.Calender of a given year\n5.Download youtube video\n6.Play guess the number game\n7.Google Search(for ex:- book store near me, car shop near me)\n8.Open Browser(for ex:- google.com)\n9.Song/Music")
        text5="Here's what I can do"
        voice(text5)
        text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")


    elif(a.get()=='generate password'or a.get()=='password'or a.get()=='1'):
        a.delete(0,END)
        words='''abcdefghijk!@$%^&*)*><??-=lmnopqrstubgh:/,=+vwxyz012345@#$%
        ^&*()?67890ABCDEFGHIJKLMNOPQRSTUVW%^^%%#:"><';XYZ!@#$%^&*()?"'''
        text6="Enter the Length of Password and click on the Generate button"
        voice(text6)
        text.insert(END,"\n"+ "Bot:"+text6)
        def pas():
            current=a.get()
            fnum=int(current)
            a.delete(0,END)
            password = "".join(random.sample(words,fnum))
            text.insert(END,"\n"+ "Bot:"+password)
            text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")

            mybutton.destroy()
            
        mybutton=Button(root,text="GENERATE",width=20,command=pas,border=3,fg="white",bg="#cb464e",font=("Arial Bold",11))
        mybutton.grid(row=2,column=1)   
    elif(a.get()=='open calendar'or a.get()=='calendar'or a.get()=='4'):
        a.delete(0,END)
        text7="Enter the Year and click on the display button"
        voice(text7)
        text.insert(END,"\n"+ "Bot:"+text7)
        def printcalendar(): 
            curr=a.get()
            a.delete(0,END)
            year=int(curr)
            text.insert(END,"\n"+ "Bot:"+calendar.calendar(year))
            text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")

            mybutton.destroy()
            
        mybutton=Button(root,text="DISPLAY",width=20,command=printcalendar,border=3,fg="white",bg="#cb464e",font=("Arial Bold",11))
        mybutton.grid(row=2,column=1)   
    elif(a.get()=='download video'or a.get()=='download youtube'or a.get()=='5'): 
        a.delete(0,END)
        text8="Enter the Link of Video and click on the download button"
        voice(text8)
        text.insert(END,"\n"+ "Bot:"+text8)
        def down():
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                link=a.get()
                ydl.download([link])
                text9="Downloaded the video"
                voice(text9)
                text.insert(END,"\n"+ "Bot: Downloaded the above video ")
                a.delete(0,END)
                text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")

                mybutton.destroy()

        mybutton=Button(root,text="DOWNLOAD",width=20,command=down,border=3,fg="white",bg="#cb464e",font=("Arial Bold",11))
        mybutton.grid(row=2,column=1)      
    elif(a.get()=='system information'or a.get()=='info'or a.get()=='2'):
        text10="click on the get info button to information of this device"
        voice(text10)
        text.insert(END,"\n"+ "Bot:"+text10)
        def info():            
            a.delete(0,END)
            text.insert(END,"\n"+ "Bot: System Os"+platform.system())
            text.insert(END,"\n"+ "Bot: Laptop/Computer Network Name :- "+platform.node())
            text.insert(END,"\n"+ "Bot: System Os Version :- "+platform.platform())
            text.insert(END,"\n"+ "Bot: Processor Name :- "+platform.processor())
            text.insert(END,"\n"+ "Bot: Machine Type :- "+platform.machine())
            text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")            
            mybutton.destroy()

        mybutton=Button(root,text="GET INFO",width=20,command=info,border=3,fg="white",bg="#cb464e",font=("Arial Bold",11))
        mybutton.grid(row=2,column=1) 
    elif(a.get()=='internet speed'or a.get()=='speedtest'or a.get()=='3'):
        text11="click on the get test speed button to get the internet speed"
        voice(text11)
        text.insert(END,"\n"+ "Bot:"+text11)
        def speed():
            a.delete(0,END)
            text.insert(END,"\n"+ "Bot:"+text11)
            st = speedtest.Speedtest()
            text.insert(END,"\n"+ "Bot: Upload Speeed :- "+str(st.upload())+"m/s")
            text.insert(END,"\n"+ "Bot: Download Speeed :- "+str(st.download())+"m/s")
            text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")
            mybutton.destroy()

        mybutton=Button(root,text="TEST SPEED",width=20,command=speed,border=3,fg="white",bg="#cb464e",font=("Arial Bold",11))
        mybutton.grid(row=2,column=1)           
    else:
        a.delete(0,END)
        text12="Sorry I did not get that"
        voice(text12)
        text.insert(END,"\n"+ "Bot:I didn't get it ")
        text.insert(END,"\n"+ "------------------------------------------------------------------------------------------------------------------------------------------")
  
    
def speak():
    r=sr.Recognizer()
    r.energy_threshold=4000
    with sr.Microphone() as source:
        audio=r.listen(source)
        texto=r.recognize(audio)
    try:
        a.insert(END,texto)
        #text.insert(END,"\n"+send)
    except LookupError:
        text.insert(END,"Try again")

speak=Button(root,text='SAY'+''+''+'>>>',fg="white",bg="#cb464e",width=20,command=speak,font=("Arial Bold",11),border=3)
speak.grid(row=1,column=0)
text=Text(root,bg='#fcfcec',fg='Black',font=("Arial Bold",10))
text.grid(row=0,column=0,columnspan=3)
a=Entry(root,width=70)
send=Button(root,text='SEND'+''+'>>>',fg="white",bg="#cb464e",width=20,command=send,font=("Arial Bold",11),border=3).grid(row=1,column=2)
a.grid(row=1,column=1)
root.title('Universal Chat Bot')
root.mainloop()
        
