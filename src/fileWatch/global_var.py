from queue import Queue

global _global_queue


def init():  # 初始化
    global _global_queue
    _global_queue = Queue()


def get_queue():
    return _global_queue
