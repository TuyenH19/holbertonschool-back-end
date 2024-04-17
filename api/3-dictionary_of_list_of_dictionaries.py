#!/usr/bin/python3
"""Script to export dictionary of list of dictionary in the JSON format"""

import json
import requests


base_URL = 'https://jsonplaceholder.typicode.com'


def export_all_tasks_to_json():
    """Fetch user data"""
    user_response = requests.get(f'{base_URL}/users')
    if user_response.status_code != 200:
        print("Error fetching user data")
        return
    users = user_response.json()

    """Dictionary to hold all tasks ny user ID"""
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['name']

        """Fetch task data for each user"""
        todos_response = requests.get(f'{base_URL}/todos',
                                      params={'userId': user_id})
        if todos_response.status_code != 200:
            print(f"Error fetching tasks data for user {user_id}")
            continue
        todos = todos_response.json()

        """Create a list of tasks for current user"""
        task_list = [{
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
            } for todo in todos]

        """Add this list to the dictionary with the user ID as the key"""
        all_tasks[user_id] = task_list

    """Create json file"""
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == '__main__':
    export_all_tasks_to_json()
