#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and
# displays the value of the variable X-Request-Id
# in the response header

if __name__ == "__main__":
    '''argv[1] is the passed url and argv[2] the email'''
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
