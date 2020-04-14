#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and
# displays the value of the variable X-Request-Id
# in the response header

if __name__ == "__main__":
    '''argv[1] is the passed url and argv[2] the email'''
    import requests
    from sys import argv

    email = {"email": argv[2]}
    r = requests.post(argv[1], email)
    print(r.text)
