#!/usr/bin/python3
"""Queries information from the JSON placeholder API.
   Exports response data to a file in json format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + "users/{}".format(sys.argv[1])
    todo_url = url + "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url=user_url).json()
    todos = requests.get(url=todo_url, params=params).json()

    with open("{}.json".format(sys.argv[1]), "w") as json_file:
        json.dump({sys.argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")} for todo in todos]}, json_file)
