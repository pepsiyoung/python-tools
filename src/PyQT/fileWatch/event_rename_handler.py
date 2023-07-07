from watchdog.events import FileSystemEventHandler
import global_var


class EventRenameHandler(FileSystemEventHandler):
    def on_created(self, event):
        q = global_var.get_queue()
        q.put(event.src_path)
