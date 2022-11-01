import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "enter the path of download folder"
to_dir = "enter the path of destination folder"

# event handler class

class FileMovementHandler(FileSystemEventHandler):
    def on_create(self,event):
        print(event)


# intialize event handler class

event_handler = FileMovementHandler()

# intialize observer 

observer = Observer()

# schedule the observer

observer.schedule(event_handler,from_dir,recursive = True)

# starting observer

observer.start()

try: 
    while True:
        time.sleep(2)
        print("Loading.....")
expect KeyboardInterrupt:
print("stopped")