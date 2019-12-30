# Native python imports
import datetime
import requests
import csv

# External package imports
from bs4 import BeautifulSoup


def main():
    """Main function call."""
    time = datetime.datetime.now()
    todays_date = str(time.month) + str(time.day) + str(time.year)

    # Get URL and soup object
    r = requests.get("https://www.uber.com/global/en/cities")
    soup = BeautifulSoup(r.text, "html.parser")
    cities_container = soup.find("section", attrs={"class": "cities-list"})
    cities_list = cities_container.findAll("li")

    # Create csv writer object
    f = open("uber_operating_cities_" + todays_date + ".csv", "wb")
    csv_writer = csv.writer(f)

    # write header
    csv_writer.writerow(["city_name", "city_url", "operating_date"])

    # Iterate through cities and write
    for city in cities_list:
        city_name = city.get_text().strip().encode("utf-8")
        city_url = city.find("a")["href"]
        csv_writer.writerow([city_name, city_url])

    # Close file
    f.close()


if __name__ == "__main__":
    main()
