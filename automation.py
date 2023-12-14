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
    # This method will be ran whenever a file is moved into the "source_folder"
    def on_modified(self, event):
        with os.scandir(source_folder) as files:
            for file in files:
                self.handle_image_files(file.name)
    
    # This method detects and move images files
    def handle_image_files(self, name):
        for extension in images_extensions:
            if name.endswith(extension):
                print(f"moving image file: {name}")

    # This method detects and move audio files
    def handle_audio_files(self, name):
        for extension in audio_extensions:
            if name.endswith(extension):
                print(f"moving audio file: {name}")

    # This method detects and move video files
    def handle_video_files(self, name):
        for extension in videos_extensions:
            if name.endswith(extension):
                print(f"moving video file: {name}")

    # This method detects and move various miscellaneous files
    def handle_misc_files(self, name):
        for extension in misc_extensions:
            if name.endswith(extension):
                print(f"moving file: {name}")

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