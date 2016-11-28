import json, requests

# First we get the URL listing all the bills that satisfy our criteria
url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&chamber=upper&q=Health'

r = requests.get(url)
bills = json.loads(r.content)

# Loop over each of those bills
for bill in bills:
    # Get the bill ID, which we need later
    bill_id = bill['bill_id']

    # Make a second request to the bill detail endpoint to obtain the most recent action
    detail_url = 'http://openstates.org/api/v1/bills/mo/2016/' + bill_id
    detail_request = requests.get(detail_url)
    detail_data = json.loads(detail_request.content)

    # Print the bill's title
    print bill['title']

    # The actions key returns a list of dictionaries. We get the last item (the most recent)
    # and print its action attribute
    print detail_data['actions'][-1]['action']

    # Just a spacer to make the printing look nicer
    print '----------'
