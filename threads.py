import threading
import time

def walk_dog():
    time.sleep(8)
    print("you finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("you finish taking out the trash")

def get_mail():
    time.sleep(4)
    print("you finish getting mail")

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

print("Checking")