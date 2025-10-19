#!/usr/bin/python3
"""Script to get TODO list progress for a given employee ID"""
import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}").json()

    completed_tasks = [t for t in todos if t.get("completed") is True]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    employee_name = user.get("name")

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
