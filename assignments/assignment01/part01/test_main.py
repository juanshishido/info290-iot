from main import raw_http


def test_http_ok_content_type():
    response_html = raw_http('128.32.78.37', '/posts', 8084)
    assert ('HTTP/1.1 200 OK' in response_html and
            'Content-Type: text/html' in response_html)
    response_json = raw_http('128.32.78.37', '/posts', 8084, as_json=True)
    assert ('HTTP/1.1 200 OK' in response_json and
            'Content-Type: application/json' in response_json)
