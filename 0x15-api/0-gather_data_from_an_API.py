#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = [todo for todo in todo_result
                     if (todo.get("completed") and
                         (todo.get("userId") == int(argv[1])))]
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todo_complete), todo_num))
    for todo in todo_complete:
        print("\t {}".format(todo.get("title")))
