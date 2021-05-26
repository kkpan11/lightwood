from enum import Enum

class dtype(Enum):
    binary = 'binary'
    integer = 'integer'
    float = 'float'
    date = 'date'
    datetime = 'datetime'
    categorical = 'categorical'
    tags = 'tags'
    image = 'image'
    audio = 'audio'
    video = 'video'
    array = 'array'
    short_text = 'short_text'
    rich_text = 'rich_text'
    empty = 'empty'
    invalid = 'invalid'
