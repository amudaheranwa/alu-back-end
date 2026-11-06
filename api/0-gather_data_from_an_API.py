#!/usr/bin/python3

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

    done = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
