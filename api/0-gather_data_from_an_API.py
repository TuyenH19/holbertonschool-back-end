#!/usr/bin/python3
import sys
import requests


def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    # Get user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        return f"Error fetching user data: {user_response.status_code}"
    user = user_response.json()

    # Get todo list for the user
    todos_response = requests.get(f"{base_url}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        return f"Error fetching todos data: {todos_response.status_code}"
    todos = todos_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    # Prepare output
    all_tasks = len(todos)  # total number of task
    n_cp_tasks = len(completed_tasks)  # number of completed tasks
    e_name = user['name']  # employee name

    # Print the progress
    print(f"Employee {e_name} is done with tasks({n_cp_tasks}/{all_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
