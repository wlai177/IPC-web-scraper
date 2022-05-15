from bs4 import BeautifulSoup
import requests


start_page = 0
end_page = 1    # Use 1375 for the real end page

for page in range (start_page, end_page):

    try:
        URL = "https://www.ipc.org/cert-search?page=" + str(page)
        source = requests.get(URL)
        source.raise_for_status() # Makes sure URL is valid

        # Extract table info from a single page
        soup = BeautifulSoup(source.text, 'html.parser')
        companies = soup.find('tbody').find_all('tr')

        # Extract company info from table
        for company in companies:

            # Iterate through the <td> tags to extract company info
            company = company.find_all('td')

            # Last row is junk data, so ignore it
            if 3 != len(company):
                break

            name = company[0].a.text
            location = company[1].text
            num_cert = company[2].text

            print(name, location, num_cert)
            
    except Exception as e:
        print(e)

print("*** Program finished ***")