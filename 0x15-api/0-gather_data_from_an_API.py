#!/usr/bin/python3
"""get data from jsonplaceholder"""
import requests
import sys

if __name__ == '__main__':
    """REST API manipulations"""
    if len(sys.argv) > 1 and isinstance(eval(sys.argv[1]), int):
        pass
    else:
        sys.exit(0)

    BASE_API = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_response_url = BASE_API + "users/{}".format(employee_id)
    todo_response_url = BASE_API + "users/{}/todos".format(employee_id)

    user_response = requests.get(user_response_url).json()
    todo_response = requests.get(todo_response_url).json()

    employee_name = user_response.get('name')

    num_tasks_done = 0
    for todo in todo_response:
        if todo.get("completed"):
            num_tasks_done += 1

    total_num_tasks = 0
    for todo in todo_response:
        total_num_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_tasks_done, total_num_tasks))

    for todo in todo_response:
        task_title = todo.get("title")
        if (todo.get("completed")):
            print("\t {}".format(task_title))
