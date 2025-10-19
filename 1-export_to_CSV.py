#!/usr/bin/python3
"""Exports data in CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    username = user.get("username")

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])