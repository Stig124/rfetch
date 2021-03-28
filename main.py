import ctypes
import os
import random
import fire
import praw
import requests as curl
import validators
import yaml
import platform


conf = yaml.safe_load(open('settings.yaml'))
cid = str(conf['app']['client_id'])
secret = str(conf['app']['client_secret'])
user = str(conf['user']['rname'])
uagent = "python:rfetch:v0.0.3b (by " + user
delete = bool(conf['user']['delete'])
randompost = int(conf['user']['random'])

reddit = praw.Reddit(client_id=cid, client_secret=secret, user_agent=uagent, )  # Declare the Reddit instance
subname = str(conf['user']['subname'])  # Get the requested subreddit from the config file
subreddit = reddit.subreddit(subname)  # Declare the requested subreddit


def preconf():
    if platform.system() == 'Windows':
        return "Win"
    elif platform.system() == 'Darwin':
        print('Not supported on MacOS (yet)')
        exit(25)
    else:
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None:  # easier to match if we doesn't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["kde", "kubuntu", "plasma", "neon"]:
                return "kde"


def conf(clisubname=subname, clidelete=delete, clirandom=randompost):
    """
    Alter the .yaml configured settings (if nothing given, the defaults are in the yaml file)
    :param clisubname: Name of the subreddit, without the r/
    :param clidelete: If you want to delete the file after the wallpaper is changed enter True
    :param clirandom: Select the upper bound of the randomisation, if no random enter 1 or 0
    """
    global subname
    subname = clisubname
    global subreddit
    subreddit = reddit.subreddit(clisubname)
    global delete
    delete = clidelete
    global randompost
    randompost = int(clirandom)


def grab():
    lim = int(random.randint(1, randompost))
    e = 1
    for submission in subreddit.top("day"):  # Get the top daily submission ID
        print(submission-)
        if e == random.randint(1, lim):
            post = reddit.submission(id=submission)
            print(submission)
            uri = post.url  # Extract the image URL
            print(uri)
            if validators.url(str(uri)) is True:  # Checks the validity of the URL
                if (uri.endswith(".jpg") is True) or (uri.endswith(".png") is True):  # Checks if is an image URL
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
        else:
            e = e + 1


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
            print(str(r.status_code) + "  " + curl.status_codes._codes[r.status_code][0])
    return local_filename


def setbackground(image, imgtype, de):
    if de == 'Win':
        from wand.image import Image
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
        return image, savename
    elif de == 'kde':
        print("You're running kde")
        import dbus
        filepath = os.getcwd()
        filepath = filepath + "/" + image
        plugin = 'org.kde.image'
        jscript = """
        var allDesktops = desktops();
        print (allDesktops);
        for (i=0;i<allDesktops.length;i++) {
            d = allDesktops[i];
            d.wallpaperPlugin = "%s";
            d.currentConfigGroup = Array("Wallpaper", "%s", "General");
            d.writeConfig("Image", "file://%s")
        }
        """
        bus = dbus.SessionBus()
        plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde'
                                                                                                      '.PlasmaShell') 
        plasma.evaluateScript(jscript % (plugin, plugin, filepath))
        print("Wallpaper set")


def delete(image, savename):
    print("Deleting the images")
    args = [image, savename]
    for x in args:
        if os.path.exists(x):
            os.remove(x)
        else:
            print("Already deleted")
    print("Done!")


if __name__ == "__main__":
    osr = preconf()
    fire.Fire(conf)
    url, imgtype = grab()
    img = dl(url, imgtype)
    setbackground(img, imgtype, osr)

else:
    exit(0)
