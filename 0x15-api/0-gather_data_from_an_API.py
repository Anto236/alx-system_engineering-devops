#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    #  get args
    userId = int(argv[1])

    #  Fetch todos and user
    todos = get('https://jsonplaceholder.typicode.com/todos').json()
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
               userId)).json()

    #  Extract user specific todos
    user_todos = []
    for todo in todos:
        if todo['userId'] == userId:
            user_todos.append(todo)

    #  get todos analytics
    todos_total = len(user_todos)
    todos_completed = sum(todo['completed'] for todo in user_todos)

    print('Employee {} is done with tasks({}/{}):'.format(
          user['name'], todos_completed, todos_total))
    for todo in [todo for todo in user_todos if todo['completed']]:
        print('\t {}'.format(todo['title']))
