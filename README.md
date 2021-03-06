# IPC Web Scraper
IPC is an association that creates acceptability standards for the electronics industry. Engineers and technicians are trained and certified to perform work and inspect to IPC standards.
Common IPC Standards:
* **IPC-A-600** Acceptability of Printed Boards
* **IPC-A-610** Acceptability of Electronics Assemblies
* **IPC/WHMA-A-620** Acceptability of Cable and Wire Harness Assemblies

## What this project does
The [IPC website](https://www.ipc.org/cert-search) publishes the number of IPC certified personnel at a given company as well as the company's location. However, their website is broken since it does not allow filtering of companies by US state. In addition, the IPC website does not support an export option for the data.

This project is a web scraper to extract the company name, location, and number of IPC certified personnel from the IPC website. The data can then be opened using a spreadsheet viewer such as Excel for data analysis. This project is created using Python and the BeautifulSoup library.