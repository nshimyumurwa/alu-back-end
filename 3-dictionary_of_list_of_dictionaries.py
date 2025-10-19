#!/usr/bin/python3
"""
Exports data for all employees in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = []
        for todo in todos:
            if todo.get("userId") == user_id:
                user_tasks.append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

        all_data[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(all_data, json_file)

    print(f"All employee data exported to {filename} successfully!")
