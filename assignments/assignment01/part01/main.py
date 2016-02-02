import socket


def raw_html(host, get, port):
    """Get HTML using a raw HTTP request

    Parameters
    ----------
    host : str
        host name

    get : str
        the resource name

    port : int
        port number

    Returns
    -------
    response : str
        HTML representation of the resource
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("GET %s HTTP/1.0\n\n" % get)
    r = s.recv(1024)
    response = ""
    while len(r):
        response = response + r
        r = s.recv(1024)
    s.close()
    return response
