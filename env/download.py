from pytube import YouTube
import os
from tkinter import messagebox
import progress
import re

def Download_video(entry_url, resolution_var, progressLabel, status_label, resolution_combobox, merge_video_and_audio, Download_button):
    url = entry_url.get()
    resolution = resolution_var.get()

    progressLabel.grid(row=4, column=0, padx=50, pady=20)
    status_label.grid(row=5, column=0, padx=50, pady=20)

    # Check if the URL is empty or contains invalid characters
    if not is_valid_youtube_url(url):
        status_label.configure(text="Invalid YouTube URL", fg="red")
        messagebox.showwarning("Error", "Please enter a valid YouTube URL.")
        return

    try:
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: progress.on_progress(stream, chunk, bytes_remaining, progressLabel))
        video_stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the video in a specific directory
        if video_stream is not None and audio_stream is not None:
            video_filename = f"{yt.video_id}_video.mp4"
            audio_filename = f"{yt.video_id}_audio.mp4"

            video_path = os.path.join("video", video_filename)
            audio_path = os.path.join("audio", audio_filename)
            output_folder = os.path.join("Final_video")
            os.makedirs(output_folder, exist_ok=True)

            yt_title_cleaned = ''.join(char if char.isalnum() or char in (' ', '_') else '_' for char in yt.title)
            output_path = os.path.join(output_folder, f'{yt_title_cleaned}_merged.mp4')

            video_stream.download(output_path="video", filename=video_filename)
            audio_stream.download(output_path="audio", filename=audio_filename)

            merge_video_and_audio(audio_path, video_path, output_path)

            status_label.configure(text="Downloaded!", font=("Georgia", 10, "bold"), fg="green")
            messagebox.showinfo("Success", "Video downloaded successfully!")
        else:
            status_label.configure(text=f"No suitable stream found with resolution {resolution}", fg="red")
            messagebox.showwarning("Error", f"No suitable stream found with resolution {resolution}")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", fg="red")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def is_valid_youtube_url(url):
    # Regular expression for a valid YouTube video URL
    youtube_url_pattern = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    match = re.match(youtube_url_pattern, url)
    return match is not None
