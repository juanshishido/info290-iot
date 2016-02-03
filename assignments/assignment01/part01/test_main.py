from main import http_raw, http_req


def test_http_ok_content_type():
    response_html = http_raw('128.32.78.37', '/posts', 8084)
    assert ('HTTP/1.1 200 OK' in response_html and
            'Content-Type: text/html' in response_html)
    response_json = http_raw('128.32.78.37', '/posts', 8084, as_json=True)
    assert ('HTTP/1.1 200 OK' in response_json and
            'Content-Type: application/json' in response_json)

def test_get_json_with_requests():
    r = http_req('128.32.78.37', '/posts', 8084)
    assert r.status_code == 200 and 'application/json' in r.headers.values()
