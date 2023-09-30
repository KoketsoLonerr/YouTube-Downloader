import yt_dlp
import tkinter as tk
from tkinter import filedialog

# Create a function to handle the download
def download_video():
    url = url_entry.get()
    download_location = filedialog.askdirectory()  # Opens a directory selection dialog
    ydl_opts = {
        'outtmpl': f"{download_location}/%(title)s.%(ext)s",
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("Download Completed")

# Create a GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create an input field for the video URL
url_label = tk.Label(window, text="Enter the video URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a download button
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Run the GUI application
window.mainloop()
