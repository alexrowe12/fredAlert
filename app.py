from bs4 import BeautifulSoup as bs
import requests
import time
import difflib

def alert(siteNum):
    with open("bearerToken.txt", "r") as file:
        # Read the entire contents of the file into a single string
        bearer_token = file.read()
    
    # Replace with your actual API credentials
    url = "https://sms.api.sinch.com/xms/v1/e7f8e2ece7134b36940d7f2ae3dab63e/batches"
    authorization_header = bearer_token
    content_type_header = "application/json"

    # Message payload
    message_data = {
        "from": "12066578213",
        "to": ["16467712679"],
        "body": "Change detected"
    }

    # Make the POST request with headers and JSON data
    response = requests.post(url, headers={
        "Authorization": authorization_header,
        "Content-Type": content_type_header
    }, json=message_data)

    # Check the response status code
    if response.status_code == 201:
        print("Message sent successfully!")
    else:
        print(f"API request failed with status code: {response.status_code}")
        print(f"Response text: {response.text}")  # Print response for debugging

# URLS of websites to scan
faWebsiteURL = "https://www.fredagain.com/#tour"
faTicketMasterURL = "https://www.ticketmaster.com/fred-again-tickets/artist/2818001"
faStubHubURL = "https://www.stubhub.com/fred-again-tickets/performer/101863087"
faSongKickURL = "https://www.songkick.com/artists/10060749-fred-again"
faSeatGeekURL = "https://seatgeek.com/fred-again-tickets"

# List of websites to iterate on
siteList = [faWebsiteURL, faTicketMasterURL, faStubHubURL, faSongKickURL, faSeatGeekURL]

# Fetch initial data and store it in siteData
siteData = []
for url in siteList:
    initial_data1, initial_data2 = "", ""

    while initial_data1 != initial_data2:
        r = requests.get(url)
        soup = bs(r.content, 'html5lib')
        initial_data1 = soup.prettify()

        time.sleep(2)

        r = requests.get(url)
        soup = bs(r.content, 'html5lib')
        initial_data2 = soup.prettify()

    siteData.append(initial_data1)

currIndex = 0
isOn = True

# Constantly iterates through and checks site data
while (isOn):
    for url in siteList:
        r = requests.get(url)
        soup = bs(r.content, 'html5lib')
        currData = soup.prettify()

        # More robust comparison using difflib
        if difflib.SequenceMatcher(None, siteData[currIndex], currData).ratio() < 0.95:
            alert(currIndex)
            siteData[currIndex] = currData
        else:
            print("No significant changes found")

        currIndex += 1

    currIndex = 0
    time.sleep(8)