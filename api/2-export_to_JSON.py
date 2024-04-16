#!/usr/bin/python3
"""Script to export data in the JSON format"""

import json
import requests
import sys


base_URL = 'https://jsonplaceholder.typicode.com'


def export_to_json(employee_id):
    """Fetch user data"""
    user_response = requests.get(f'{base_URL}/users/{employee_id}')
    if user_response.status_code != 200:
        print("Error fetching user data")
        return
    user = user_response.json()

    """Fetch task data"""
    todos_response = requests.get(f'{base_URL}/todos',
                                  params={'userId': employee_id})
    if todos_response.status_code != 200:
        print("Error fetching tasks data")
        return
    todos = todos_response.json()

    """Prepare data for JSON output"""
    task_list = [
        {"task": task["title"], "completed": task["completed"],
         "username": user["username"]} for task in todos
    ]

    """Create a dictionary with user ID as key"""
    tasks_by_user = {str(employee_id): task_list}

    """Create json file"""
    file_name = f"{employee_id}.json"
    with open(file_name, mode='w') as jsonfile:
        writer = json.dump(tasks_by_user, jsonfile)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_json(employee_id)
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)
