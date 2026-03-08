import requests
import urllib.parse
from configapi import htmltopdfkey as cfg

# This code retrieves a webpage and converts it to a PDF file using the html2pdf API.
target_url = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

# The API endpoint for the html2pdf service is defined, and the API key is retrieved from the configuration file.
apiurl = "https://api.html2pdf.app/v1/generate"

apikey = cfg["html_topdfkey"]

# The parameters for the API request include the target URL to be converted and the API key for authentication.
parametrs = {'html': target_url,'apiKey': apikey}

# The parameters are encoded into a query string format, and a GET request is sent to the API endpoint with the parameters included in the URL.
parsed_url = urllib.parse.urlencode(parametrs)
response = requests.get(apiurl +"?" + parsed_url)

print(response.status_code)

# "wb" means write binary (non-text file), which is necessary for writing PDF files
with open("output.pdf", "wb") as f:
    f.write(response.content)