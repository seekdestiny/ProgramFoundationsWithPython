import webbrowser
import time

print("This program started on " + time.ctime())
for index in range(3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
