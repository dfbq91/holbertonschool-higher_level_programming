#!/usr/bin/python3
# Takes your Github credentials (username and password)
# and uses the Github API to display your id

if __name__ == "__main__":
    '''Get id from github api'''
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    jsoned = r.json()
    print(jsoned['id'])
