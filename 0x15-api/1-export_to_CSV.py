#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def todocsv():
    """ function that gets todo tasks and exports data to csv file """
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
        stat.append(new[i].get('completed'))
        titles.append(new[i].get('title'))
    with open("{}.csv".format(userid), 'w') as f:
        for i in range(0, size):
            f.write('"{}","{}","{}","{}"\n'.format(userid, name,
                                                   stat[i], titles[i]))

if __name__ == "__main__":
    todocsv()
