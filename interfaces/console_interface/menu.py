from consolemenu import *
from consolemenu.items import *

import consts.general
import helper.authenticator
import helper.rand_str_generator
import objects.playlist
import objects.user
import search
from consts import general


class Menu:
    current_user: objects.user.User

    def __init__(self):
        main_menu_name = f"SpotiPY - v{general.APP_VERSION}"
        main_menu_description = f"Your app for... hmm... IDK! but its cool here, check out the options!"
        main_menu = ConsoleMenu(main_menu_name, main_menu_description)

        main_menu_login_item = FunctionItem("Login", self.login)
        main_menu_info_item = FunctionItem("Read Info on SpotiPY", self.spotipy_info)
        main_menu.append_item(main_menu_login_item)
        main_menu.append_item(main_menu_info_item)

        user_menu_name = f"Menu for user: {self.current_user.name}"
        user_menu = ConsoleMenu(user_menu_name)

        user_menu_user_details = FunctionItem("My info", print, [self.current_user.__dict__])
        user_menu_add_playlist = FunctionItem("Add playlist", self.add_new_playlist())
        user_menu_add_song_to_playlist = FunctionItem("Add song to playlist",
                                                      self.add_song_to_playlist())
        user_menu.append_item(user_menu_add_playlist)
        user_menu.append_item(user_menu_add_song_to_playlist)

        searcher = search.Searcher()
        search_menu = ConsoleMenu(f"Search Data as: {self.current_user.name}")
        search_menu_get_artists = FunctionItem(
            "Get all artists", print, [self.current_user.search(searcher, "artists")])
        search_menu_get_artist_albums = FunctionItem(
            "Get albums of artist", print,
            [self.current_user.search(searcher, "artist_albums", artist_id=input("Enter artist id: "))])
        search_menu_get_artist_top_songs = FunctionItem(
            "Get most popular songs of artist!", print,
            [self.current_user.search(searcher, "artist_top_songs", artist_id=input("Enter artist id: "))])
        search_menu_get_album_songs = FunctionItem(
            "Get every song in album!", print,
            [self.current_user.search(searcher, "album_songs", album_id=input("Enter album id: "))])
        search_menu.append_item(search_menu_get_artists)
        search_menu.append_item(search_menu_get_artist_albums)
        search_menu.append_item(search_menu_get_artist_top_songs)
        search_menu.append_item(search_menu_get_album_songs)

        user_menu_search_submenu = SubmenuItem("search data", search_menu)
        user_menu.append_item(user_menu_search_submenu)

        user_menu_logout = FunctionItem("logout", self.logout)
        user_menu.append_item(user_menu_search_submenu)

    def logout(self):
        self.current_user = None


    def login(self):
        username = input("Enter user name: ")
        try:
            self.current_user = helper.authenticator.login(username)
            if self.current_user is not None:
                return
            raise Exception("LOL")
        except Exception as e:
            print("shouldn't happened, but: " + e.__repr__())

    @staticmethod
    def spotipy_info():
        print(f"""
Hello there
im not complited yet
sorry for the bugs
(⌯˃̶᷄ ﹏ ˂̶᷄⌯)ﾟ
""")

    def add_new_playlist(self):
        p_name = input("Enter playlist name: ")
        playlist = objects.playlist.Playlist(
            helper.rand_str_generator.generate(consts.general.ID_LENGTH), p_name, [])
        self.current_user.add_playlist(playlist)

    def add_song_to_playlist(self):
        p_name = input("Enter playlist name: ")
        song_id = input("Enter song id: ")
        self.current_user.add_song_to_playlist(song_id, p_name)


# Create the menu
menu = ConsoleMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command", "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
