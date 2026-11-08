#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file using a REST API."""
import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(BASE_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(BASE_URL), params={"userId": employee_id}
    ).json()

    username = user.get("username")

    data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in todos
        ]
    }

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data, json_file)
