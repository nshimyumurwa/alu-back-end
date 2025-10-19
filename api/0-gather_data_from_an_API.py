#!/usr/bin/python3
"""Script to get todos for a user from API"""
import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    
    response = requests.get(todo_url)
    total_tasks = 0
    completed = []
    
    for todo in response.json():
        if todo['userId'] == user_id:
            total_tasks += 1
            if todo['completed']:
                completed.append(todo['title'])
    
    user_response = requests.get(user_url).json()
    employee_name = user_response['name']
    
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), total_tasks))
    
    for task in completed:
        print("\t {}".format(task))


if __name__ == '__main__':
    main()
