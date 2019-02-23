"""
Wait for Ghost to start
"""
import time
import requests

# Test environment defaults
IS_HTTPS = False
HOST = '127.0.0.1'
PORT = 80

SESSION = requests.Session()    # Reuse the same requests Session

if IS_HTTPS:
    host_part = 'https://%s:%s' % (HOST, str(PORT))
else:
    host_part = 'http://%s:%s' % (HOST, str(PORT))
url = '%s%s' % (host_part, '/')

success = False

for _ in range(0, 15):
    try:
        response = SESSION.get(url, timeout=2)
    except requests.exceptions.ConnectionError as err:
        time.sleep(1)
    else:
        if response.content:
            break
