# vintage_story.py
# A Simple Resources API Wrapper from Vintage Story
# Author: Cypherpunk Samurai
# License: MIT
import requests

def get_latest_version():
    """
        Returns the latest version of the game
    """
    # as of writing this, the latest version is 1.0.0
    return requests.get("https://api.vintagestory.at/latestunstable.txt").text

def get_versions():
    """
        Returns a list of all available versions
    """
    return requests.get("http://api.vintagestory.at/stable-unstable.json").text

def get_blocked_mods():
    """
        Returns a list of all blocked mods
    """
    # GET /api/blockedmods.json HTTP/1.1
    # Host: cdn.vintagestory.at
    return requests.get("https://cdn.vintagestory.at/api/blockedmods.json").text

def auth_validate(username, password):
    """
        Validates a username and password
    """
    # POST /clientvalidate HTTP/1.1
    # Host: auth3.vintagestory.at
    # Content-Type: application/x-www-form-urlencoded
    # Content-Length: 16

    # uid=&sessionkey=

    return requests.post("https://auth3.vintagestory.at/clientvalidate", data={"uid": username, "sessionkey": password}).text

def main():
    """
        Prints the latest version of the game
    """
    print(get_latest_version())
    # pretty print the json
    print(get_versions())
    # todo: implement download from cdn. cdn url like https://cdn.vintagestory.at/gamefiles/stable/vs_update_win-x64_1.21.0.exe
    print(get_blocked_mods())
    print(auth_validate("", ""))

if __name__ == "__main__":
    main()
