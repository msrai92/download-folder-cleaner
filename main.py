from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os 
import json
import time 

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
            print("file modified: "+filename)
    def on_created(self, event):
        print("hey, {event.src_path} has been created!")
        for filename in os.listdir(folder_to_track):
            print("file created: "+filename)

folder_to_track = "C:/Users/msing/Documents/file_move_test_A"
folder_destination = "C:/Users/msing/Documents/file_move_test_B"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try: 
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

    