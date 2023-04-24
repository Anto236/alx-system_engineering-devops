import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 todo.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = sys.argv[1]

main_url = 'https://jsonplaceholder.typicode.com'
response_user = requests.get(main_url + '/users/' + employee_id)
response_todo = requests.get(main_url + '/todos?userId=' + employee_id)

if response_user.status_code != 200 or response_todo.status_code != 200:
    print("Error: API request unsuccessful.")
    sys.exit(1)

user_data = response_user.json()
tasks_data = response_todo.json()

employee_name = user_data['name']

total_tasks = len(tasks_data)
completed_tasks = 0
completed_task_titles = []

for task in tasks_data:
    if task['completed']:
        completed_tasks += 1
        completed_task_titles.append(task['title'])

print("Employee {} is done with tasks({}/{}):"
      .format(employee_name, completed_tasks, total_tasks))
for title in completed_task_titles:
    print("\t {}".format(title))
