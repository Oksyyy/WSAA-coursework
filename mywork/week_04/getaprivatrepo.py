import requests
import json
from configapi import git_authkey as cfg

# This code retrieves information about a private GitHub repository and saves it to a JSON file.
filename = "aprivateone.json"

# The URL for the GitHub API endpoint to access the repository information.
url = "https://api.github.com/repos/Oksyyy/aprivateone"

apikey = cfg["git_authkey"]

# The API request includes authentication using a personal access token (PAT) to access the private repository.
response = requests.get(url, auth=('token', apikey))
print(response.status_code)

# The response from the API is expected to be in JSON format, which is parsed and saved to a file named "aprivateone.json".
json_response = response.json()

with open(filename, "w") as f:
    json.dump(json_response, f, indent=4)