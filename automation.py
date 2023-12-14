# Libraries needed for the script
import os
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to observe
source_folder = ""

# Destination folders for images, videos, audio files, and other files
images_destination_folder = ""
audio_destination_folder = ""
video_destination_folder = ""
misc_destination_folder = ""

# Extensions for images
images_extensions = [".png", ".jpg", ".jpeg", ".gif", ".webp"]

# Extensions for audio files
audio_extensions = [".mp3", ".wav"]

# Extension for video files
videos_extensions = [".mp4", ".mov"]

# Extensions for various other types of files
misc_extensions = [".pdf", ".pptx", ".docx", ".zip", ".txt", ".doc", ".csv"]

# Class that handles FileSystem events
class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_folder) as files:
            for file in files:
                print(file.name)

# Use the watchdog library to detect changes in the file system and move files
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_folder
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()