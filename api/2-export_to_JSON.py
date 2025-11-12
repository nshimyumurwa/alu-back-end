#!/usr/bin/python3
"""
Script that exports employee TODO list data to JSON format
"""
import json
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
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if (user_response.status_code != 200 or
            todos_response.status_code != 200):
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    tasks_list = []
    for task in todos_data:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = username
        tasks_list.append(task_dict)

    json_data = {str(employee_id): tasks_list}
    filename = "{}.json".format(employee_id)

    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)
