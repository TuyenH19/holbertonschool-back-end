#!/usr/bin/python3
"""Script to export data in the CSV format"""

import csv
import requests
import sys


base_URL = 'https://jsonplaceholder.typicode.com'


def export_to_csv(employee_id):
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

    """Create CSV file"""
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        """Write each task to csv"""
        for task in todos:
            writer.writerow([employee_id, user['username'],
                             task['completed'], task['title']])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)
