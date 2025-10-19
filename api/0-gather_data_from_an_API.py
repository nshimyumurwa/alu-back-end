#!/usr/bin/python3
"""Script that, using a REST API, returns information about an employee's TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"

        # Get user info
        user = requests.get(f"{base_url}/users/{user_id}").json()
        employee_name = user.get("name")

        # Get todos
        todos = requests.get(f"{base_url}/todos?userId={user_id}").json()
        done_tasks = [task for task in todos if task.get("completed")]

        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todos)}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")