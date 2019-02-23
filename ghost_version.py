import requests

latest_release = requests.get('https://api.github.com/repos/TryGhost/Ghost/releases/latest').json()
latest_version = latest_release['tag_name']

print(latest_version)
