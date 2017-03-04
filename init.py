#coding=utf-8

from datetime import datetime

from conf import TASK_BEAT, TASK_WORKER
from schedulers import Task
from models import *

def init_task_db():
    # init beat
    task = Task(type='beat',interval=TASK_BEAT,last_run_at=datetime.now())
    task.save()
    worker = Task(type='worker', interval=TASK_WORKER, last_run_at=datetime.now())
    worker.save()

def db_test():
    #artist = Artist(nameid=1234, name='baby', song=['I believe', 'La La Land'])
    #artist.save()

    songcomment1 = SongComment(userid=1,user='zph',userpic='hh', content='it is a good song ,i love it')
    songcomment2 = SongComment(userid=2,user='dyc',userpic='dd', content='boring!!!I can not get it!')
    songs = Songs(songid=2233, comment=[songcomment1,songcomment2])
    songs.save()
    #songcomment = SongComment()
    #songcomment.save()
    #songs = Songs(songid = '', songcomment = '')
    #songs.save()


def main():
    #init_task_db()
    #db_test()
    comment = Songs.comment
    for song in Songs.objects:
        print(song.songid)

    comments = Songs.comment
    for comment in comments:
        print(comment.content)

if __name__ == '__main__':
    main()