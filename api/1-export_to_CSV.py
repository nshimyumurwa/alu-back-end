#!/usr/bin/python3
"""
Script that exports employee TODO list data to CSV format
"""
import csv
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
    
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    todos_response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    username = user_data.get("username")
    
    filename = "{}.csv".format(employee_id)
    
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        for task in todos_data:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
