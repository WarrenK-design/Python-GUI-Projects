# Uses the weather API for america https://docs.airnowapi.org/CurrentObservationsByZip/query
# NEED TO CRETAE A .env file with APIKEY= <YOUR API KEY FROM https://docs.airnowapi.org/CurrentObservationsByZip/query>
from tkinter import *
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

root = Tk()
root.title("Weather App")
root.geometry("600x100")

# Create zip look up function
def zipLookup():
    apikey = os.getenv("APIKEY")
    zip_code =zip.get()
    # Request the info
    url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip_code+"&distance=25&API_KEY="+apikey

    try:
        api_request = requests.get(url)
        api = json.loads(api_request.content)
        city =api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        # Good
        # Moderate
        # Unhealthy for Sensitive Groups
        # Unhealthy
        # Very Unhealthy
        # Hazardous
        # Unavailable
        weather_colour = ""
        if category == "Good":
            weather_colour = "#0C0"
        elif category == "Moderate":
            weather_colour = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900"
        elif category == "Unhealthy":
            weather_colour = "#FF000"
        elif category == "Very Unhealthy":
            weather_colour = "#990066"
        elif category == "Hazardous":
            weather_colour = "#660000"
        elif category == "Unavailable":
            weather_colour = "#FFFFFF "

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 15),
                        background=weather_colour)
        root.configure(background=weather_colour)
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = "Error"


zip = Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S )

root.mainloop()