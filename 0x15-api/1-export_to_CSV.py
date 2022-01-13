#!/usr/bin/python3
"""
Queries information from the JSON placeholder API.
Exports response data to a file in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, params=params).json()

    with open("{}.csv".format(sys.argv[1]), "w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            csv_writer.writerow([sys.argv[1], user.get("username"),
                                todo.get("completed"),
                                todo.get("title")])
