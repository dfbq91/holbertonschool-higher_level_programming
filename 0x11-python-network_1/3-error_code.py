#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and displays
# the body of the response (decoded in utf-8).

if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            html = response.read()
            decoded_html = html.decode('utf-8')
            print(decoded_html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
