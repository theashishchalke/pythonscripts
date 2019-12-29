from gophish import Gophish
from gophish.models import *

#Required declarations
api_key = "APIKEYHERE"
gohost = "GOPHISH_ADMIN_URL"
api = Gophish(api_key, host=gohost, verify=False)

#Get campaign Name
campaigndict = {} #Create an empty campaign dictionary
print("Printing a list of available campaigns:")
for campaign in api.campaigns.get(): #Use API Call to get all campaigns
    #Update campaigns to the campaigndict dictionary with campaignname:id format
    campaigndict.update([(campaign.name,str(campaign.id))])
    #Print all the available Campaigns.
    print("Name: " + campaign.name + " " + "ID: " + str(campaign.id))
#print(campaigndict) #Print the campaigndict dictionary for visual analysis