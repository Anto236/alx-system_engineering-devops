#!/usr/bin/python3
"""
    Using REST API, for a given employee ID, returns
    information about his/her TODO list progress.
    And saves data to a CSV file.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(argv[0]))
        exit(1)

    # Endpoint URLs
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'

    # Get employee information
    employee_id = int(argv[1])
    user = requests.get(user_url.format(employee_id)).json()
    todos = requests.get(todos_url.format(employee_id)).json()

    # Generate CSV file
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow(
                ([user['id'], user['username'],
                 todo['completed'], todo['title']]))
