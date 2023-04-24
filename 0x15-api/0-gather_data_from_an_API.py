#!/usr/bin/python3
"""This script returns information about his/her
todo list progress"""
import requests as rq
from sys import argv


def tasks_done(todos, mode='count'):
    """Return the number of completed tasks or print the titles"""
    done = 0
    for todo in todos:
        if todo.get('completed', False):
            if mode == 'title':
                print("\t " + todo['title'])
            else:
                done += 1
    return done


user_id = argv[1] if argv[1:] else 1
url = 'https://jsonplaceholder.typicode.com/'
user = rq.get(url + 'users/{}'.format(user_id)).json()
todos = rq.get(url + 'users/{}/todos'.format(user_id)).json()
print('Employee {} is done with tasks({}/{}):'.
      format(user.get('name'), tasks_done(todos), len(todos)))
tasks_done(todos, 'title')
