# Libraries needed for the script
import os
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Extensions for images
images_extensions = [".png", ".jpg", ".jpeg", ".gif", ".webp"]

# Extensions for audio files
audio_extensions = [".mp3", ".wav"]

# Extension for video files
videos_extensions = [".mp4", ".mov"]

# Extensions for various other types of files
misc_extensions = [".pdf", ".pptx", ".docx", ".zip", ".txt", ".doc", ".csv"]
