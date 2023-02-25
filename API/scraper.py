from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = "https://devfolio.co/hackathons"


options = webdriver.ChromeOptions()
#options.add_argument('--headless') 
driver = webdriver.Chrome(options=options)
driver.get(url)


wait = WebDriverWait(driver, 30)

try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "HackathonListing")))
except TimeoutException:
    print("Timed out waiting for Hackathon listings to load")

hackathons = []

listings = driver.find_elements(By.CLASS_NAME, "HackathonListing")

for listing in listings:
    hackathon = {}

    hackathon['name'] = listing.find_element(By.CLASS_NAME, "ListingHeader__Heading-sc-1fcmfeb-1").text.strip()

    dates = listing.find_element(By.CLASS_NAME, "ListingHeader__Info-sc-1fcmfeb-2").text.strip().split(' - ')
    hackathon['start_date'] = dates[0]
    hackathon['end_date'] = dates[1]

    hackathon['location'] = listing.find_element(By.CLASS_NAME, "ListingHeader__Location-sc-1fcmfeb-3").text.strip()

    hackathon['link'] = "https://devfolio.co/hackathons" + listing.find_element(By.CLASS_NAME, "ListingHeader__Link-sc-1fcmfeb-4")['href']

    hackathons.append(hackathon)

driver.quit()

for hackathon in hackathons:
    print(hackathon['name'])
    print("Start Date:", hackathon['start_date'])
    print("End Date:", hackathon['end_date'])
    print("Location:", hackathon['location'])
    print("Link:", hackathon['link'])
    print()
