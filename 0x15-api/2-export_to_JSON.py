#!/usr/bin/python3
"""
   A script which retrieves employee data from the JSONPlaceholder Rest API and
   converts it to the JSON format.
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id

    req_name = requests.get(url)
    req_todos = requests.get(url + "/todos")
    name = req_name.json().get("username")

    JSON = req_todos.json()
    json_list = [[] for x in range(len(JSON))]

    for i in range(len(JSON)):
        json_list[i] = {"task": JSON[i].get("title"),
                        "completed": JSON[i].get("completed"),
                        "username": name}

    to_json = {str(id): json_list}

    with open("{}.json".format(id), "w", encoding="utf-8") as fp:
        json.dump(to_json, fp)
