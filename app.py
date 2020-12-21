import os, platform, json
from models.bookmark import BookMark
from pathlib import Path

user_home = str(Path.home())
currentOS = platform.system()
bookMarkFolders = {
    'windows': [
        os.path.join(user_home, 'AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks')
    ],
    'linux': [
    ]
}
# Search for all bookmarks for all supported browsers
def get_all_bookmarks():
    all_bookmarks = []
    if currentOS == 'Windows':
        for dir in bookMarkFolders['windows']:
            print("Loading bookmarks from directory: %s" % dir)
            with open(dir, 'rb') as bm_json:
                all_bookmarks.append(json.load(bm_json))
            bm_json.close()
            print(len(all_bookmarks[0]["roots"]["bookmark_bar"]["children"]))

if __name__ == '__main__':
    get_all_bookmarks()