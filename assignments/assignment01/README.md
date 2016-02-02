## Internet/Web Basics

**Deliverables**: You should create a zip file containing the Python and
JavaScript code created in this assignment. You must make sure that the Python
code runs with version 2.7 of the interpreter - remember that your submitted
code must work on our machines as well, so use relative paths if you add
external libraries to your project, and include these libraries with your zip
file. Please use UTF-8 encoding for your documents and avoid special
characters.

1. REST Web Services in Python

Your task is to create a Python script that reads data from
[our test API](http://russet.ischool.berkeley.edu:8084/) and pushes data to it.
You will see different ways of how this can be done.

    1. Raw HTTP Requests

Our Web API speaks the HTTP protocol, version 1.1. In this assignment, your
first task is to fetch a piece of data from the API using a raw HTTP request,
i.e. without the use of any external library: Create a method in your Python
program that opens a TCP connection and sends an HTTP GET request to obtain the 
HTML representation of the `/posts` resource from the API. Your method should
then display the API's raw, unparsed response on the screen (i.e. including the 
returned HTTP headers).

    2. HTTP Headers and Status Codes

From the raw HTTP response of the previous exercise, find the values of each of
the following parameters. Summarize the meaning of each parameter in a short
paragraph (include your answers as comments in your Python code).

* The HTTP Status Code
* The Content-Type header
* The Cross-Origin Resource Sharing (CORS) headers

The response to your request in the previous exercise should carry the 200 OK
HTTP status code. Also have a look at the following four HTTP status codes and
look up their exact semantics - you will maybe encounter some of these when
dealing with the Activity Streams platform during the course project:

* 401 Unauthorized
* 404 Not Found
* 409 Conflict
* 415 Unsupported Media Type

    3. HTTP Content Negotiation

So far, you only received HTML responses back from the server. A REST service
can, however, offer several representations of the same resource. For instance, 
many resources also provide JSON (Links to an external site.) representations - 
JSON is a lightweight version of XML that is often used in Web mashups and REST
interfaces because it can directly be translated to JavaScript objects.

To obtain a representation of the `/posts` resource that is more appropriate
for machine-machine communication than HTML, we can make use of the HTTP
content negotiation mechanism: Set the `Accept` header of your raw HTTP request 
to ask the server for a representation of the resource in the JSON format by
specifying the appropriate media type. If successful, the Web server will now
return a JSON file that contains all forum posts. Display the raw JSON response 
on the screen.

    4. HTTP Requests using the requests Library

HTTP requests are usually not implemented by hand, but rather using one of many 
different libraries that take care of the intricacies of the HTTP protocol and
connection management. In this task, you should create a method that uses the
Python Requests library (Links to an external site.) (you'll need to install
that from the given URL) for sending the same HTTP request as you created by
hand in task 1.3. This method should also display the JSON representation of
the `/posts` resource on the screen.

    5. Switching Gears: POSTing Data

Up until now, you have only used the HTTP GET method to obtain data from the
API. For this task, first look up the exact semantics of a few other methods
that are specified in the HTTP protocol: POST, PUT, DELETE, HEAD, and OPTIONS.
Next, use an HTTP POST request to send a new forum post to the API's /posts
resource. The payload of your POST request should be in the JSON format and
have the following structure:

```
{ 'author' : 'your-name', 'message' : 'your-message' }
```

    6. Submission Instructions for this Task

You should create a single method for each of the tasks 1.1, 1.3, 1.4, and 1.5. 
Your Python script should call each of these methods in-order. The script
should be executable with the command `python main.py` from the command line.
