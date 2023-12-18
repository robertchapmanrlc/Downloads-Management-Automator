# Downloads-Management-Automator
Keeping a file system nice and organized can be a difficult, especially after downloading files that go to your downloads folder. Fortunately, the task of organizing your filesystem can be progrommatically automated with python. 

Using the watchdog API library, along with the os and os.path modueles, you can tailor this script to your specific needs. Change the ```source_folder``` variable to your Downloads folder on your filesystem and the respective ```destination_folder``` variables to where images, videos, audio files, and other miscellaneous files should be placed.

## Getting Started
To run the project, you need to have Python and pip installed on your system.

### Installation
1. Clone or download the repository to your local machine.
```
git clone https://github.com/robertchapmanrlc/Downloads-Management-Automator/
```
2. Enter the working directory.
```
cd Downloads-Management-Automator/
```
3. Use pip to install watchdog
```
pip install watchdog
```

### Usage
1. Open the ```automation.py``` in a file editor

2. Change the ```source_folder``` variable to the full path of your downloads folder:
```
/Users/username/Downloads (for MacOS)
C:\Users\(Your Account)\Downloads (for Windows)
```
3. Change the ```destinaton_folder``` variables to the full paths of where you want different types of files to go:

4. Save the changes to the file and run the following command:
```
python automation.py
```
5. As the script is running, you are free to download files from the internet as the script logs files being downloaded
```
2023-12-18 07:37:31 - Moved image file: cat-instagram-captions-64ff2dfa47e9a
2023-12-18 07:37:39 - Moved image file: cute-cat-photos-1593441022
2023-12-18 07:37:55 - Moved image file: National-Dog-Day--scaled
```
6. When finished, stop the program with ```Ctrl + C``` or ```Control (or Ctrl) ⌃ + C``` for MacOS

### Note
Please keep in mind that you may also have to include more file extensions in the supported ```extensions``` lists if an extension is not recognized.

### Built With
* [Python](https://www.python.org/) - The programming language used.
* [watchdog](https://pypi.org/project/watchdog/) - API Library used to observe changes in a filesystem.

