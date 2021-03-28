  <!-- <a href="https://rfetch.netlify.app">Demo</a> -->
</div>

<h1 align="center">Rfetch</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/stig124/rfetch?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/stig124/rfetch?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/stig124/rfetch?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/stig124/rfetch?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/stig124/rfetch?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/stig124/rfetch?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/stig124/rfetch?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Rfetch 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/stig124" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Fetch and applies the most upvoted image in any image subreddit as a wallpaper on Windows

## :sparkles: Features ##

:heavy_check_mark: Automatic fetching and validation of grabbed URLs
:heavy_check_mark: Choosing a random post (in beta)
:heavy_check_mark: Automatic prerequirements install script (coming soon)

## :rocket: Technologies ##

The following tools were used in this project:

- [PRAW](https://github.com/adrn/pyraw)
- [Reddit API](https://www.reddit.com/dev/api)
- [Google Python-Fire](https://github.com/google/python-fire)
- You can find the python modules list in [requirements.txt](./requirements.txt)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have

- [Git](https://git-scm.com)
- [Python 3](https://python.org)
- [ImageMagick](https://imagemagick.org/script/download.php)
- a Reddit app registered as a `script`, see [Reddit API Quick Start](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) and use a dummy redirect URL like `http://localhost:8080`

## :checkered_flag: Starting ##

##### Clone this project #####

```shell
git clone https://github.com/stig124/rfetch
```

##### Access the directory #####

```shell
cd rfetch
```

##### Grab the required python packages *(NOTE : a virtualenv is highly recommanded to avoid pakcage mess)* #####

```shell
pip install -r requirements.txt
```

###### For the users of [pipenv](https://pipenv.pypa.io/en/latest/) a Pipfile is included #######

```shell
pipenv install
```

##### Modifiy the [settings.yaml.sample](./settings.yaml.sample) file with the corresponding settings then #####

```shell
cp settings.yaml.sample settings.yaml
```

##### RUN #####

```shell
python ./main.py
```

and let the magic happen :sparkles:

__NOTE__ : **There is no way to revert a wallpaper change !** *(an history of images link may come later)*

## Usage ##

Running `python ./main.py` (or `python3 ./main.py`) fetches all the settings from the `settings.yaml` files but is is possible to change those settings on the fly :

```shell
python ./main.py <SUBNAME> <DELETE> <RANDOM>
```

`Subname` :
Overrides the subreddit name defined in the config file [Syntax : subreddit name wihout `r/`]

`Delete` :
Opting in the automatic deletion of the image ater being set as a wallpaper [Syntax : `True` or `False`]

`Randomizing`
Randomize the post from which the image will be taken [Syntax: a number between `1` and `~ 200`]
##### :bangbang: Warning

Some subreddits will not work if they don't use URLs with image type ending (xxx.xxx.jpg/png)
Some tested and working subs :

- r/earthporn
- r/villageporn
- r/cityporn
- r/wallpaper
- r/Animewallpaper
- r/ComicWalls

## :memo: License ##

This project is under Mozilla Public License 2.0. For more details, see the [LICENSE](./LICENSE) file.

Made with :heart: by <a href="https://github.com/stig124" target="_blank">Stig124</a>

&#xa0;

<a href="#top">Back to top</a>