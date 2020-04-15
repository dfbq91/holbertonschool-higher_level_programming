#!/usr/bin/python3
# list 10 commits (from the most recent to oldest)
# of the repository “rails” by the user “rails”

if __name__ == "__main__":
    '''Github api'''
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]

    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(owner, repo), params={'per_page': 10})
    jsoned = r.json()
    for i in jsoned:
        print("{}: {}".format(i.get('sha'),
                                  i.get('commit').get('author').get('name')))
