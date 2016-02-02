from main import raw_html


def test_simpleforum_title():
    assert 'SimpleForum Posts Resource' in raw_html('128.32.78.37', '/posts', 8084)
