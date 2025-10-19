#!/usr/bin/python3
"""
Exports data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get("username")

    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    data = {employee_id: tasks}

    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {filename} successfully!")