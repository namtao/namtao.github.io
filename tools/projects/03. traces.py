import logging
import time
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

class Event(LoggingEventHandler):
    def dispatch(self, event):
        print("Foobar")

def traces_of_changes(folder_path):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    event_handler = LoggingEventHandler()
    # event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

traces_of_changes(r"E:\PM")