import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        
        ytLink = link.get()
        print("10")
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        print("13")

        title.configure(text= ytObject.title, text_color="white")
        finishLabel.configure(text = "")
        video.download()
        print("18")
        finishLabel.configure(text = "Downloaded!")
    except:
        finishLabel.configure(text = "Download Error")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    
    #convert to string removes floating point and then conv to string to use it
    per = str(int(percentage_of_completion))
    pPercentage.configure(text = per + "%")
    pPercentage.update()

    #update progress bar
    progressBar.set(float(percentage_of_completion)/100)
    

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


#Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx = 10, pady=10)

#Link input 
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()

#progress percentage
pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 400)

progressBar.set(0)
progressBar.pack(padx = 10, pady = 10)


#Download Button
download = customtkinter.CTkButton(app, text="Download", command = startDownload)
download.pack(padx = 10, pady=10)

#Run app
app.mainloop()