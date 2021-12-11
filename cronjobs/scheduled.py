import threading
import time

from countdown.models import Countdown

def create_thread():
    thread = threading.Thread(target=date_checker, args=(), kwargs={})
    thread.setDaemon(True)
    thread.start()

def date_checker():
    while True:
        countdown = Countdown.objects.first()
        time.sleep(60)

def change_day():
    pass

def assign_wishlists():
    pass
