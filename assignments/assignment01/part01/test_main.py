from main import raw_http


def test_simpleforum_title():
    assert 'SimpleForum Posts Resource' in raw_http('128.32.78.37', '/posts', 8084)
