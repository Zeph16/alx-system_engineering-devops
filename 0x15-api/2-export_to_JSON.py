#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def todojson():
    """ function that gets todo tasks and exports data to json file """
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    new = r.json()
    name = new.get('username')
    userid = new.get('id')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    new = r.json()
    size = len(new)
    stat = []
    titles = []
    for i in range(0, size):
        if new[i].get('completed'):
            stat.append("true")
        else:
            stat.append("false")
        titles.append(new[i].get('title'))
    with open("{}.json".format(userid), 'w') as f:
        f.write('{' + '"{}"'.format(userid)+': [')
        for i in range(0, size - 1):
            f.write('{{"task": "{}", "completed": {}, "username": "{}"}}, '
                    .format(titles[i], stat[i], name))
        f.write('{{"task": "{}", "completed": {}, "username": "{}"}}'
                .format(titles[-1], stat[-1], name))
        f.write(''']}''')


if __name__ == "__main__":
    todojson()
