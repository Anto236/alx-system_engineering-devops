#!/usr/bin/python3
"""
Uses a REST API, fetching data about a given employee
(identified by their id passed to the script as an argument) and
exports the data (of all tasks owned by the user) in the CSV format.
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    if len(sys.argv) > 1:
        api = 'https://jsonplaceholder.typicode.com/'
        user = requests.get(api + 'users/{}'.format(sys.argv[1]))
        todos = requests.get(api + 'todos')
        user_todos = []
        for todo in todos.json():
            if todo.get('userId') == int(sys.argv[1]):
                user_todos.append(todo)

        file_name = '{}.csv'.format(sys.argv[1])
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for todo in user_todos:
                row = [sys.argv[1], user.json().get('username'),
                       todo.get('completed'), todo.get('title')]
                writer.writerow(row)
    else:
        pass
