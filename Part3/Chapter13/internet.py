"""Internet"""
import urllib.request as urlrequest 

# URL to GET
url = "https://www.python.org"

# Get the page content
req = urlrequest.Request(url)
with urlrequest.urlopen(req) as response:
    page_content = response.read()

print(f"Done with {url}")

from urllib.request import urlopen
import re 
from html import unescape

# URL to GET
url = "https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&format=json&page=Mount_Tambora"

# Request the page
response = urlopen(url)

# Get the page content
page_content = str(response.read())

# Use this regex to find the elevation of Mt. Tambora
regex = r"elevation\_m\s=\s(\d*)"

# Performs the search
result = re.search(regex, page_content)
print(f"{result}")
# Fetch the second element of the match (which is the elevation)
elevation = result[1]

# Print the elevation
print(f"The elevation of Mt. Tambora is {elevation}.")
