from __future__ import absolute_import, unicode_literals
from celery import shared_task
from file_sharing.celery import app


@app.task
def print_message(name, *args, **kwargs):
    f = open("demo.txt", "a")
    f.write("Now the file has more content!")
    f.close()

@app.task
def add(x, y):
    f = open("demo.txt", "a")
    f.write("Now the file has more content!" + str(x) + str(y))
    f.close()

