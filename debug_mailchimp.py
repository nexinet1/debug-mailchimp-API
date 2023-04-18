#First, make sure you have installed the mailchimp_marketing Python package. 
pip install mailchimp_marketing


#Next, import the necessary modules:
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import logging


#Set up logging so that you can see any error messages that are returned by the API:
logging.basicConfig(level=logging.DEBUG)


#Create an instance of the Client class and authenticate with the API using your credentials
client = MailchimpMarketing.Client()
client.set_config({
    "api_key": "your_api_key",
    "server": "your_server_prefix"
})



#Now you can make API requests and debug any issues that arise. For example, if you wanted to retrieve a list of audiences, you could use the following code:
try:
    response = client.lists.get_lists()
    print(response)
except ApiClientError as error:
    print("Error: {}".format(error.text))
    
    

#If there is an issue with your API credentials or with the request itself, you will see an error message in your terminal. For example, if your credentials are invalid, you might see a message like this    
Error: {"type":"http://developer.mailchimp.com/documentation/mailchimp/guides/error-glossary/","title":"API Key Invalid","status":401,"detail":"Your API key may be invalid, or you've attempted to access the wrong datacenter."}

