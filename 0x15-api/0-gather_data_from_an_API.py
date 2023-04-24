#!/usr/bin/python3
""" Uses a REST API, fetching data about a given employee
    (identified by their id passed in as an arg).
    Returns:
            information about thir TODO list progress
    Requirements:
            must use urllib or requests module
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide an employee ID as a parameter")
        sys.exit(1)

    employee_id = sys.argv[1]
    api = 'https://jsonplaceholder.typicode.com/'

    # Fetch user details
    user = requests.get(api + 'users/{}'.format(employee_id)).json()
    employee_name = user['name']

    # Fetch user's TODO list
    todos = requests.get(api + 'todos', params={'userId': employee_id}).json()

    # Count number of completed and total tasks
    num_completed = 0
    total_tasks = len(todos)
    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            num_completed += 1
            completed_tasks.append(todo['title'])

    # Print output in the required format
    print("Employee {} is done with tasks({}/{})".format(employee_name,
          num_completed, total_tasks))
    for task in completed_tasks:
        print("\t {} {}".format("\t", task))
