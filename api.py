from sunlight import openstates
import sunlight.service
from sunlight.errors import BadRequestException
import json

active_legislators = openstates.legislators(
    active='true'
)
print(active_legislators)

bills_2016 = openstates.bills(
    created_at = "%2016%"
)

for bill in bills_2016:
    print bill["title", "action"]


#module_name = "openstates"
#service_url = "http://openstates.org/api/v1"


#class Openstates(sunlight.service.Service):

    #def legislator_detail(self, active, **kwargs):
        #return self.get(["legislators", active], **kwargs)
