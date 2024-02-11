def on_progress(stream, chunk, bytes_remaining,progressLabel):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100
    per = str(int(percentage_completed))
    progressLabel.configure(text=per + "%")
    progressLabel.update()
