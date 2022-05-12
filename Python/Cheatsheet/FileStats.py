import os

# Create a reference to the file path that you want to analyze
file_path = os.path.join("Resources", "SomeCoolStuff.txt")

# Collect the stats and save it to a variable
statInfo = os.stat(file_path)

# To collect the file size in bytes...
print(statInfo.st_size)

# To collect the last time the file was accessed (opened) in unix epoch time...
timeAccessed = statInfo.st_atime

# Epoch time is annoyingly hard to read, so let's convert that into an actual datetime format


import datetime

# This takes the timeAccessed timestamp and converts it into a much more comprehensive form
timeAccessed = datetime.datetime.fromtimestamp(timeAccessed).strftime('%c')
print(timeAccessed)

# To collect the last time the file was modified (changed) in unix epoch time...
timeChanged = statInfo.st_mtime
timeChanged = datetime.datetime.fromtimestamp(timeChanged).strftime('%c')
print(timeChanged)

# If a potentially malicious file is uncovered, sometimes it is best to just remove it immediately
# This can be done using os.remove()
os.remove("Resources/BigOlWallpaper.jpg")
