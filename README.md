# Project Marco
Project Marco is an application that allows for more intelligent vacation planning,

## Getting Started

###Prerequisites
To use project Marco, you will need to run the following commands 

```
pip3 install sklearn
```
- Data
    - List countries English-speaking population.html -- language.py
    - language.json -- language.py
    - Travel Advisories.html (exmaple) -- safety.py
    - airports.csv -- kiwi.py, skyscanner.py
    - city_links_csv.csv -- scrape_city_links.py
    - destination.csv -- scrape_city_pages.py
- Functions
    - scrape_city_links.py -- Scrape city links from Lonely Planet
    - scapre_city_pages.py -- Scrape info from city pages on Lonely Planet
    - constants.py -- Keywords and keywords dictionary
    - country.py -- Get country of a city
    - process_city_keywords.py -- WIP
    - process_static_data.py -- Output static info
    - current_location.py -- Get user's current location by ip address
    - safety.py -- Get travel advisories
    - get_keywords.py -- Get keywords from a paragraph
    - language.py -- Get percentage of English speakers by country
    - kiwi.py -- Flight costs information by kiwi.com
    - skyscanner.py -- Flight costs information by skyscanner api
    - pile_driver.py -- 
    - weather_data.py -- Getting weather related data
- Archived
    - Proposal
        - Proposal.txt
        - proposal.pdf
    - Functions
        - hotel_costs.py -- Slow hotel costs information scraper
    - outline_pseudocode.py -- Project outline
        - get_flight_costs from kiwi (old)