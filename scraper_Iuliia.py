import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

# Open file and CSV writer
outfile = open('election.csv', 'w')
writer = csv.writer(outfile)

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

# Set up BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find table body/rows
table = soup.find('table', {'class': 'electtable'})
rows = table.find_all('tr')

for row in rows:


  # Here's one way to get all of the data into a list

    # # Get all of the cells (td tags) for each row
    # cells = row.find_all('td')

    # # Create a new empty list to hold the output
    # data = []

    # # Loop over each cell in the row
    # for cell in cells:
    #     # Add the cell's data to the row_data output
    #     data.append(cell.text)

    # Here's another way to do it with list comprehensions
    data = [cell.text for cell in row.find_all('td')]

    writer.writerow(data)

    # # Traceback (most recent call last):
  # File "scraper_Iuliia.py", line 51, in <module>
    # writer.writerow(data)
# UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0' in position 0: ordinal not in range(128)
