import json
import urllib2

# question 2
my_json = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=mo&chamber=upper&search_window=session:2016').read()

data = json.loads(my_json)

for bills in data:
    print bills
