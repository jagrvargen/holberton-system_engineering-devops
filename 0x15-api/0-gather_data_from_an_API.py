#!/usr/bin/python3
"""
   A script which retrieves employee data from the JSONPlaceholder Rest API.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id

    req_name = requests.get(url)
    req_todos = requests.get(url + "/todos")

    name = req_name.json().get("name")
    JSON = req_todos.json()
    total_tasks = len(JSON)
    done_tasks = 0

    for dic in JSON:
        for key, value in dic.items():
            if key == "completed" and value is True:
                done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks,
                                                          total_tasks))
    for task in JSON:
        if task.get("completed") is True:
            print("\t{}".format(task.get("title")))
