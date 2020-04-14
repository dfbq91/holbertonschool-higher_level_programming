#!/usr/bin/python3
# Takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id variable
# found in the header of the response.

if __name__ == "__main__":
    from sys import argv
    from urllib import request
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
