from bs4 import BeautifulSoup
import requests, csv

def parseLocation(location):
    location_list = location.split(", ", 2)
    if 2 == len(location_list):
        location_list.append(location_list[1])
        location_list[1] = ""
    elif 1 == len(location_list):
        location_list.append("")
        location_list.append(location_list[0])
        location_list[0] = ""
    return location_list


print("*** Program started ***")

start_page = 0
end_page = 10    # Use 1375 for the real end page

f = open('export.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(["Company", "City", "State", "Country", "Number of Certs"])

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

            # print(name, location, num_cert)

            location = parseLocation(location)

            # print(location)
            print(name, location, num_cert)

            writer.writerow([name, location[0], location[1], location[2], num_cert])
            
    except Exception as e:
        print(e)

f.close()
print("*** Program finished ***")