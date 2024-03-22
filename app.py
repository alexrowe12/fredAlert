from bs4 import BeautifulSoup as bs
import requests
import time

# URLS of websites to scan
faWebsiteURL = "https://www.fredagain.com/#tour"
faTicketMasterURL = "https://www.ticketmaster.com/fred-again-tickets/artist/2818001"
faStubHubURL = "https://www.stubhub.com/fred-again-tickets/performer/101863087"
faSongKickURL = "https://www.songkick.com/artists/10060749-fred-again"
faSeatGeekURL = "https://seatgeek.com/fred-again-tickets"

# List of websites to iterate on
siteList = [faWebsiteURL, faTicketMasterURL, faStubHubURL, faSongKickURL, faSeatGeekURL]
siteData = []
currData = ""
currIndex = 0
isOn = True

# Constantly iterates through a checks site data
while (isOn):
    for url in siteList:
        r = requests.get(url) 
        soup = bs(r.content, 'html5lib') 
        currData = soup.prettify()

def alert(site):
