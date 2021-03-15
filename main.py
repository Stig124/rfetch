import yaml
from wand.image import Image
import requests as curl
import praw
import validators
import ctypes
import os

conf = yaml.safe_load(open('settings.yaml'))
cid = str(conf['app']['client_id'])
secret = str(conf['app']['client_secret'])
user = str(conf['user']['rname'])
uagent = "python:rfetch:v0.0.1a (by " + user

reddit = praw.Reddit(client_id=cid, client_secret=secret, user_agent=uagent, )
subname = str(conf['user']['subname'])
subreddit = reddit.subreddit(subname)


def grab():
    for submission in subreddit.top("day", limit=1):
        post = reddit.submission(id=submission)
        uri = post.url
        print(uri)
        if validators.url(str(uri)) is True:
            if (uri.endswith(".jpg") is True) or (uri.endswith(".png") is True):
                if uri.endswith(".jpg") is True:
                    imgtype = ".jpg"
                else:
                    imgtype = ".png"
                return uri, imgtype
            else:
                print("This link isn't an image")
                exit(1)
        else:
            print("This link isn't an image")
            exit(12)
        print(uri)


def dl(uri, imgtype):
    print('Downloading the top image from the choosen subreddit')
    if imgtype == ".jpg":
        local_filename = str(subname) + ".jpg"
    else:
        local_filename = str(subname) + ".png"
    with curl.get(uri) as r:
        if r.status_code == 200:
            with open(local_filename, "wb") as file:
                file.write(r.content)
                file.close()
        else:
            # TODO: HTTP STATUS CODES DESCRIPTION
            print(r.status_code)
    return local_filename


def setbackground(image, imgtype):
    with Image(filename=image) as wall:
        savename = str(image).replace(imgtype, ".bmp")
        wall.format = 'bmp'
        wall.save(filename=savename)
        image = str(str(image)+".bmp")
    SPI_SETDESKTOPWALLPAPER = 20
    path = os.getcwd()
    path = path + "\\" + image
    path = "The wallpaper is located at : " + path
    print(path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, path, 3)


if __name__ == "__main__":
    url, imgtype = grab()
    img = dl(url, imgtype)
    setbackground(img, imgtype)

else:
    exit(0)
