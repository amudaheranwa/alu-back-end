#!/usr/bin/python3
"""Export all employees' TODO list data to a JSON file using a REST API."""
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    users = requests.get("{}/users".format(BASE_URL)).json()
    todos = requests.get("{}/todos".format(BASE_URL)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos
            if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
