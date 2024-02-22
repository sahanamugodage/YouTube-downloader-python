import tkinter
import customtkinter
from pytube import YouTube



def start_download():
    try:
        yt_link = download_box.get()
        yt_object = YouTube(yt_link,on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        # video = yt_object.streams.get_audio_only()
        download_lbl.configure(text=yt_object.title,text_color="white")
        finish_download_lbl.configure(text="")
        finish_download_lbl.configure(text="Download Successfully")
        video.download()
    except:
        finish_download_lbl.configure(text="Invalid YouTube Link..!",text_color="red")

def mp3():
    try:
        yt_link = download_box.get()
        yt_object = YouTube(yt_link,on_progress_callback=on_progress)
        mp_3 = yt_object.streams.get_audio_only()
        download_lbl.configure(text=yt_object.title,text_color="white")
        finish_download_lbl.configure(text="")
        finish_download_lbl.configure(text="Download Successfully")
        mp_3.download()
    except:
        finish_download_lbl.configure(text="Invalid YouTube Link..!",text_color="red")
 

def on_progress(streams,chunk,bytes_remaining):
    total_size = streams.filesize
    bytes_downloaded = total_size - bytes_remaining
    precentage_of_compeletation = bytes_downloaded / total_size * 100
    pre = str(int(precentage_of_compeletation))
    progress_presentage_lbl.configure(text=pre + "%")
    progress_presentage_lbl.update()
    
    # update pragress bar
    progress_bar.set(float(precentage_of_compeletation)/100)
    

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# app frame
window = customtkinter.CTk()
window.geometry("720x480")
window.title("Youtube Video Downloader")


# add UI elements
download_lbl = customtkinter.CTkLabel(window,text="Insert A YouTube Link",font=('Comic Sans MS', 35),text_color="#66e0ff")
download_lbl.pack(padx=10,pady=10)

url_var = tkinter.StringVar()
download_box = customtkinter.CTkEntry(window,width=350,height=40,font=('Comic Sans MS',15),textvariable=url_var,text_color="#0052cc")
download_box.pack()

# finish download
finish_download_lbl = customtkinter.CTkLabel(window,text="",font=('Comic Sans MS',15)) 
finish_download_lbl.pack()

# prgress presentage
progress_presentage_lbl =customtkinter.CTkLabel(window,text="0%") 
progress_presentage_lbl.pack()

progress_bar = customtkinter.CTkProgressBar(window,width=400)
progress_bar.set(0)
progress_bar.pack(padx=10,pady=10)

download_btn = customtkinter.CTkButton(window,text="Download",command=start_download)
download_btn.pack(padx=10,pady=10)

download_mp3_btn = customtkinter.CTkButton(window,text="Download Mp3",command=mp3)
download_mp3_btn.pack(padx=10,pady=10)

window.mainloop() 