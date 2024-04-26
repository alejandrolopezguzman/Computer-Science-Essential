
#Mars Photo Viewer
#The following code will return photos from Mars taken from NASAs Curiosity, Opportunity, and Spirit rovers

#Visit this page for the API calls from NASA. Browse APIs, then select Mars Rover Photos
#https://api.nasa.gov/

#in the space below, create your code that reaches the desired outcome. You may use old code of yours to accomplish this task as you see fit

#YOU MAY NOT USE MORE THAN 35 LINES OF CODE. COMMENTS AND BLANK LINES DO NOT COUNT TOWARDS THIS REQUIRMENT
#YOU MUST HAVE AT LEAST 1 COMMENT LINE FOR EVERY 4 LINES OF CODE
#URL=https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=
#IMPORTS
import requests
from PIL import Image
from io import BytesIO

def fetch_apod(base_url, api_key,):
    #concatenate a url with the base_url, your api key, and the extra parameters for the desired date
    #This is the format your url request should be:
    #https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY&date=YYYY-MM-DD
    url = base_url+api_key
    print(url)
    response = requests.get(url)
    data = response.json()
    #Returns raw data
    return data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key="
#below, paste your NASA API Key.
api_key = "NbUJ0SLqGaA4djDwdou8yBqHFNUYW9bYQSmpi4Oj"
apod_data = fetch_apod(base_url, api_key)
#image = requests.get("http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG")
print(apod_data)
from PIL import Image
#Gets image
from urllib.request import urlopen
url = "http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG"
img = Image.open(urlopen(url))
img.show()
