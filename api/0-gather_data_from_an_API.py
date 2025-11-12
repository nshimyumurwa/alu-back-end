#!/usr/bin/python3
"""
Script that fetches TODO list progress for a given employee ID from an API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get("{}/users/{}".format(base_url,
                                                      employee_id))
    todos_response = requests.get("{}/todos?userId={}".format(base_url,
                                                              employee_id))

    if (user_response.status_code != 200 or
        todos_response.status_code != 200):
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
