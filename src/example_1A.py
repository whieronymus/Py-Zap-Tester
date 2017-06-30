from zap import StoreClient
import requests

# EXAMPLE USE CASE
# Store deak_id from a previous Step with a order_id key to retrieve it later

input_data = {"order_id": '1001', "deal_id": "12345"}


output = {}

# When you're done Testing Locally, Copy/Paste Code in between Tags
########################### ZAPIER CODE #######################################

"""
When example_1B Triggers via Shopify Order Update, we don't have access to the HubSpot DealID to update the Deal. This step stores the HubSpot DealID in the StoreClient with the Shopify OrderID as the key so we can look it up in later in Example_1B

We do this because there is no wear to store it in the Shopify Order
"""
order_id = input_data['order_id']
deal_id = input_data['deal_id']

store = StoreClient('Your Secret')

store.set(order_id, deal_id)

# No Output


######################## END ZAPIER CODE ######################################


# For Teesting Output
# Display New Fields available to Zap's Next Steps

def print_output():
    print("Field Name: Value")
    for k, v in output.items():
        print("{}: {}".format(k, v))

print_output()
# You can also use return in Zapier for example:
# return {"test": "value"}
# but I can't recreate that for testing locally so just use output
