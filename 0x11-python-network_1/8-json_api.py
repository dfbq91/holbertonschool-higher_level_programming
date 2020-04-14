#!/usr/bin/python3
# Takes in a URL, sends a request to the URL and
# displays the value of the variable X-Request-Id
# in the response header

if __name__ == "__main__":
    '''argv[1] is the passed url and argv[2] the email'''
    import requests
    from sys import argv

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    result = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

    try:
        jsoned = result.json()
        if jsoned == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsoned['id'], jsoned['name']))
    except ValueError:
        print("Not a valid JSON")
