import tkinter as tk
from tkinter import ttk
import button
import download
import merge

def on_download_button_click():
    download.Download_video(entry_url, resolution_var, progressLabel, status_label, resolution_combobox, merge.merge_video_and_audio, Download_button)

# Create a root window
root = tk.Tk()

# Title of the window
root.title("YouTube Downloader!")
root.iconbitmap(r'YT.ico')

# Set min and max width and the height
root.geometry("800x500")
root.resizable(0,0)

left_color= "#230100"
right_color= "#CDC5BF"

# Create a left frame
left_frame = tk.Frame(master=root,width="400",bg=left_color)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Load the image
image_path = r"G:\Python\Projects\YT_Downloader\env\YT_logo.png"
try:
    width = 400
    height = 500
    image = tk.PhotoImage(file=image_path,width=width, height=height)
    image_label = tk.Label(left_frame, image=image,bg=left_color)
    image_label.grid(pady=100)

except Exception as e:
    print(f"Error loading image: {e}")

# Create a right frame
right_frame = tk.Frame(master=root, bg=right_color, width="400")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

# Create a label and entry widget for the video url in the right frame
url_label = tk.Label(right_frame, text="Enter the youtube url here:-", fg="black",font=("", 16, "bold"), padx=20, pady=10,bg=right_color)
entry_url = tk.Entry(right_frame, width=40, borderwidth=2)
url_label.grid(row=0, column=0, padx=40, pady=20)
entry_url.grid(row=1, column=0, padx=50, pady=20)

# Style the entry widget
entry_url.configure(font=("Helvetica", 11,"bold"), relief="solid", bd=2)
 
# Create a label and entry widget for the video url in the left frame
url_label_left = tk.Label(left_frame, text="Downloader!", fg="White",font=("Times New Roman", 20), padx=20, pady=0,bg=left_color)
url_label_left.grid(row=0, column=0, padx=100, pady=0)

# Create a style for the Combobox
combobox_style = ttk.Style()
combobox_style.theme_create("combostyle", parent="alt",settings={"TCombobox": {"configure":{"padding": 3, "width": 15}}})
combobox_style.theme_use("combostyle")

# Create a resolution button
resolutions                     = ["1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_var                 = tk.StringVar()
resolution_combobox = ttk.Combobox(right_frame, values=resolutions, textvariable=resolution_var, style="combostyle.TCombobox")
resolution_combobox.grid(row=2, column=0, padx=50, pady=20)
resolution_combobox.set("720p")

# Create Download button
Download_button = tk.Button(right_frame, text="Download", font=("Georgia", 12, "bold"), bg="purple", command=on_download_button_click, borderwidth=0, fg="white")
Download_button.grid(row=3, column=0, padx=50, pady=20)


# Bind events for hover and leave
Download_button.bind("<Enter>", lambda event: button.on_button_hover(event, Download_button))
Download_button.bind("<Leave>", lambda event: button.on_button_leave(event, Download_button))

# Create a label and the progress bar to display the download progress
progressLabel = tk.Label(right_frame, text="0%",bg=right_color, font=("Helvetica", 12, "bold"))

# Create the status label
status_label = tk.Label(right_frame, text=" ",bg=right_color)

# To start the app
root.mainloop()   
