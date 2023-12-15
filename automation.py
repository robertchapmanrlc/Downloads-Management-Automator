# Libraries needed for the script
from os import scandir, rename
from os.path import exists, join, splitext
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to observe (Use absolute path)
source_folder = ""

# Destination folders for images, videos, audio files, and other files (Use absolute path)
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

# This function creates a unique name for a file that already exists
def make_unique_name(name, dest):
    # Parse the filename and extension
    filename, extension = splitext(name)
    counter = 1

    # Keep incrementing counter until the name with the nth copy doesn't already exists
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

# This function determines the type of a file depending on the extension
def file_type(extension):
    if extension in images_extensions:
        return "image"
    elif extension in audio_extensions:
        return "audio"
    elif extension in videos_extensions:
        return "video"
    elif extension in misc_extensions:
        return "misc"
    return None

# This function moves the file with the given name to the destination
def move_file(name, file, dest):
    # If the file already exists, then rename it
    if exists(f"{dest}/{name}"):
        unique_name = make_unique_name(name, dest)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)

    shutil.move(file, dest)

# Class that handles FileSystem events
class MoveHandler(FileSystemEventHandler):
    # This method will be ran whenever a file is moved into the "source_folder"
    def on_modified(self, event):
        with scandir(source_folder) as files:
            for file in files:
                # Call the appropriate function based on the extension
                filename, extension = splitext(file.name)
                match file_type(extension):
                    case 'image':
                        self.handle_image_files(file, filename)
                    case 'audio':
                        self.handle_audio_files(file, filename)
                    case 'video':
                        self.handle_video_files(file, filename)
                    case 'misc':
                        self.handle_misc_files(file, filename)
                    case _:
                        print(f"{extension} file type not supported for {filename}")
    
    # This method detects and move images files
    def handle_image_files(self, file, name):
        move_file(name, file, images_destination_folder)
        logging.info(f"Moved image file: {name}")

    # This method detects and move audio files
    def handle_audio_files(self, file, name):
        move_file(name, file, audio_destination_folder)
        logging.info(f"Moved audio file: {name}")

    # This method detects and move video files
    def handle_video_files(self, file, name):
        move_file(name, file, video_destination_folder)
        logging.info(f"Moved video file: {name}")

    # This method detects and move various miscellaneous files
    def handle_misc_files(self, file, name):
        move_file(name, file, misc_destination_folder)
        logging.info(f"Moved file: {name}")

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