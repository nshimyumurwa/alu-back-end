#!/usr/bin/python3
"""Example script for Web Infrastructure task"""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    todos = response.json()

    done_tasks = [t for t in todos if t.get("completed")]
    print(f"Employee {user_id} is done with tasks({len(done_tasks)}/{len(todos)}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")