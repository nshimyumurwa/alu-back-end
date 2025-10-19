#!/usr/bin/python3
"""Script to get todos for a user from API"""
import requests
import sys


def main():
    """Main function"""
    user_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    user_name = user.get("name")
    completed = [t.get("title") for t in todos if t.get("completed")]

    print("Employee Name:", user_name)
    print(f"To Do Count: {len(todos)}")
    print(f"Number of done tasks: {len(completed)}/{len(todos)}")
    for task in completed:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()
