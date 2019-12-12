from pprint import pprint


import os
import json
from collections import namedtuple

def get(file,as_object=True):
    """
    Load a JSON file and return the contents as an object or array
    @param file: The path to the file to load
    @param as_object: Return as an object (can be accessed via object.property). Otherwise object['property'].
    @return object
    """

    with open(file, 'r') as data:
        if as_object:
            return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        else:
            return json.load(data)

def get_lang(guild_id):
    """
    Check which language file the guild is using
    @param guild_id: The guild ID
    @return string: The language code
    """
    # TODO: Look up guild language in DB
    return 'en'

def get_string(str, guild_id):
    """
    Load a language string
    @param str: The language string code
    @param guild_id: The guild ID
    @return string: The full string in the correct language
    """

    lang = get_lang(guild_id)
    path = f'./data/lang/{lang}.json'
    strings = get(path, False)
    return strings[str] if str in strings else f'[[{str}]]'