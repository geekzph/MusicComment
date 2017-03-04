# coding=utf-8
from datetime import datetime
from mongoengine import *  # noqa

from conf import HOST, PORT, DATABASE

connect(DATABASE, host=HOST, port=PORT)

class Artist(Document):
    artist_id = IntField(max_length=60, required=True)             # 歌手id
    artist_name = StringField(max_length=60, required=True)        # 歌手名字
    artist_pic = StringField(max_length=60, required=True)         # 歌手头像
    songs = ListField(StringField(max_length=60, required=True))   # 歌曲列表

class SongComment(EmbeddedDocument):
    user_id = IntField(max_length=60, required=True)           # 用户id
    user_nmae = StringField(max_length=60, required=True)      # 用户名
    user_pic = StringField(max_length=100)                     # 用户头像
    content = StringField(max_length=100, required=True)       # 评论内容

class Songs(Document):
    song_id = IntField(required=True)                        # 用户id
    song_nmae = StringField(max_length=60, required=True)    # 用户名字
    comment = ListField(EmbeddedDocumentField(SongComment))  # 评论内容