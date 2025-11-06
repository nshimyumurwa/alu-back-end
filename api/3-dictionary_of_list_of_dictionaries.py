#!/usr/bin/python3
"""
Script that exports all employees TODO list data to JSON format
"""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    
    users_response = requests.get("{}/users".format(base_url))
    todos_response = requests.get("{}/todos".format(base_url))
    
    if users_response.status_code != 200 or todos_response.status_code != 200:
        exit(1)
    
    users_data = users_response.json()
    todos_data = todos_response.json()
    
    all_employees_data = {}
    
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        
        user_tasks = []
        for task in todos_data:
            if task.get("userId") == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        
        all_employees_data[str(user_id)] = user_tasks
    
    filename = "todo_all_employees.json"
    
    with open(filename, mode='w') as json_file:
        json.dump(all_employees_data, json_file)
