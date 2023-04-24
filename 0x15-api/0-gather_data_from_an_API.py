#!/usr/bin/python3
"""Script to use REST API to gather information"""

import requests
import sys

if __name__ == "__main__":
    url_target = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url_target + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(url_target + "todos", params={
                        "userId": sys.argv[1]}).json()

    completetasks = []
    for todos in tasks:
        if todos.get("completed") is True:
            completetasks.append(todos.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
            employee.get("name"), len(completetasks), len(tasks)))
    for title in completetasks:
        print("\t {}".format(title))
