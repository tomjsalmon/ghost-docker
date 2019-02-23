"""
Tests my Docker build of Ghost.
"""
import requests

# Test environment defaults
IS_HTTPS = False
HOST = '127.0.0.1'
PORT = 80

# Reuse the same requests Session
SESSION = requests.Session()

def request(path='/',
            is_https=IS_HTTPS,
            host=HOST,
            port=PORT):
    """
    Return a HTTP response for the given path, from a predefined host.
    Keyword arguments:
    path -- the resource to get. Starts with a '/'
    is_https -- is the server running HTTPS True/False
    host -- the web server host
    port -- the web server port
    """
    if is_https:
        host_part = 'https://%s:%s' % (host, str(port))
    else:
        host_part = 'http://%s:%s' % (host, str(port))
    url = '%s%s' % (host_part, path)
    return SESSION.get(url, timeout=2, allow_redirects=False)

def test_root():
    """Tests on the root of Ghost '/' """
    root_page = request('/')
    assert root_page.status_code == 200

def test_admin():
    """Tests on the Ghost admin panel"""
    admin = request('/ghost/')
    assert admin.status_code == 200
