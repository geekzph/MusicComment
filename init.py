#coding=utf-8

from datetime import datetime

from conf import TASK_BEAT, TASK_WORKER
from schedulers import Task


def init_task_db():
    # init beat
    task = Task(type='beat',interval=TASK_BEAT,last_run_at=datetime.now())
    task.save()
    worker = Task(type='worker', interval=TASK_WORKER, last_run_at=datetime.now())
    worker.save()


def main():
    init_task_db()


if __name__ == '__main__':
    main()