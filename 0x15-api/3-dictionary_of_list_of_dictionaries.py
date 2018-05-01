#!/usr/bin/python3
"""
   A script which retrieves all employee data from the JSONPlaceholder Rest API
   and converts it to the JSON format.
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    to_json = {}
    for i in range(1, 11):
        id = i
        url = "https://jsonplaceholder.typicode.com/users/" + str(id)

        req_name = requests.get(url)
        req_todos = requests.get(url + "/todos")
        name = req_name.json().get("username")

        JSON = req_todos.json()
        print(JSON)
        json_list = [[] for x in range(len(JSON))]

        for i in range(len(JSON)):
            json_list[i] = {"task": JSON[i].get("title"),
                            "completed": JSON[i].get("completed"),
                            "username": name}

        to_json.update({str(id): json_list})

    with open("todo_all_employees.json".format(id), "w",
              encoding="utf-8") as fp:
        json.dump(to_json, fp)
