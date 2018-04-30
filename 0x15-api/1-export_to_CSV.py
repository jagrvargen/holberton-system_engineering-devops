#!/usr/bin/python3
"""
   A script which retrieves employee data from the JSONPlaceholder Rest API and
   converts it to the CSV format.
"""


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + id

    req_name = requests.get(url)
    req_todos = requests.get(url + "/todos")
    name = req_name.json()["username"]

    JSON = req_todos.json()
    task_list = [[] for i in range(len(JSON))]

    for i in range(len(JSON)):
        task_list[i].append(str(id))
        task_list[i].append(name)
        task_list[i].append(str(JSON[i]["completed"]))
        task_list[i].append(JSON[i]["title"])
        ",".join(task_list[i])

    with open("{}.csv".format(id), "w") as csv_file:
        writer = csv.writer(csv_file)
        for item in task_list:
            writer.writerow(item)
