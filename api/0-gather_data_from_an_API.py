#!/usr/bin/python3
"""Script that uses a REST API to get employee TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    num_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")