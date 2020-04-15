#!/usr/bin/python3
# Fetches https://intranet.hbtn.io/status

if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
          format(type(html), html, html.decode('utf-8')))
