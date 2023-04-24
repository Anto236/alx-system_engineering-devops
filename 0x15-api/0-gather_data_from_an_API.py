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
    if len(sys.argv) != 2:
        print('Usage: {} EMPLOYEE_ID'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    if response.status_code != 200:
        print('Error: could not fetch user data')
        sys.exit(1)
    employee_name = response.json()['name']

    # Fetch TODO list data
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))
    if response.status_code != 200:
        print('Error: could not fetch TODO list data')
        sys.exit(1)
    todo_data = response.json()

    # Compute TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(todo['completed'] for todo in todo_data)

    # Print progress report
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          completed_tasks, total_tasks))
    for todo in todo_data:
        if todo['completed']:
            print('\t', todo['title'])
