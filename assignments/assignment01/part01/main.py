from __future__ import print_function

import json
import socket

import requests


def http_raw(host, get, port, as_json=False):
    """Get data using a raw HTTP request

    Parameters
    ----------
    host : str
        host name (IP address)

    get : str
        the resource name

    port : int
        port number

    Returns
    -------
    response : str
        text representation of the resource
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    if as_json:
        s.send("GET %s HTTP/1.1\nHost: %s\nAccept: application/json\n\n" %
               (get, host))
    else:
        s.send("GET %s HTTP/1.1\nHost: %s\n\n" % (get, host))
    r = s.recv(1024)
    response = ""
    while len(r):
        response = response + r
        r = s.recv(1024)
    s.close()
    return response

def http_req(host, get, port):
    """Get JSON using `requests`

    Parameters
    ----------
    host : str
        host name (IP address)

    get : str
        the resource name

    port : int
        port number

    Returns
    -------
    r : requests.models.Response
        a Response object
    """
    url = "http://"+host+":"+str(port)+get
    r = requests.get(url, headers={'Accept': 'application/json'})
    print(r.text)
    return r

def post_message(host, get, port, author, message):
    url = "http://"+host+":"+str(port)+get
    payload = {'author' : author, 'message' : message}
    r = requests.post(url, headers={'Content-Type' : 'application/json'},
                      data=json.dumps(payload))
    return r
