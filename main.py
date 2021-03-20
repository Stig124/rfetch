import ctypes
import os
import fire
import praw
import requests as curl
import validators
import yaml
from wand.image import Image

conf = yaml.safe_load(open('settings.yaml'))
cid = str(conf['app']['client_id'])
secret = str(conf['app']['client_secret'])
user = str(conf['user']['rname'])
uagent = "python:rfetch:v0.0.3b (by " + user
delete = bool(conf['user']['delete'])

reddit = praw.Reddit(client_id=cid, client_secret=secret, user_agent=uagent, )  # Declare the Reddit instance
subname = str(conf['user']['subname'])  # Get the requested subreddit from the config file
subreddit = reddit.subreddit(subname)  # Declare the requested subreddit


def conf(clisubname=subname, clidelete=delete):
    """
    Alter the .yaml configured settings (if nothing given, the defaults are in the yaml file)
    :param clisubname: Name of the subreddit, without the r/
    :param clidelete: If you want to delete the file after the wallpaper is changed enter True
    """
    global subname
    subname = clisubname
    global subreddit
    subreddit = reddit.subreddit(clisubname)
    global delete
    delete = clidelete


def grab():
    for submission in subreddit.top("day", limit=1):  # Get the top daily submission ID
        post = reddit.submission(id=submission)
        uri = post.url  # Extract the image URL
        print(uri)
        if validators.url(str(uri)) is True:  # Checks the validity of the URL
            if (uri.endswith(".jpg") is True) or (uri.endswith(".png") is True):  # Checks if the URL is an image URL
                if uri.endswith(".jpg") is True:
                    imgtype = ".jpg"
                else:
                    imgtype = ".png"
                return uri, imgtype
            else:
                print("This link isn't an image")
                exit(1)
        else:
            print("This link isn't valid")
            exit(12)


def dl(uri, imgtype):
    print('Downloading the top daily image from r/' + subname)
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
            print(str(r.status_code) + " " + curl.status_codes._codes[r.status_code][0])
    return local_filename


def setbackground(image, imgtype):
    with Image(filename=image) as wall:
        savename = str(image).replace(imgtype, ".bmp")
        wall.format = 'bmp'
        wall.save(filename=savename)
        image = str(image)
    path = os.getcwd()
    path = path + "\\" + image
    pathh = "The wallpaper is located at : " + path
    print(pathh)
    SPI_SETDESKTOPWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, path, 3)
    if delete == 1:
        print("Deleting the images")
        args = [image, savename]
        for x in args:
            if os.path.exists(x):
                os.remove(x)
            else:
                print("Already deleted")
        print("Done!")


if __name__ == "__main__":
    fire.Fire(conf)
    url, imgtype = grab()
    img = dl(url, imgtype)
    setbackground(img, imgtype)

else:
    exit(0)
