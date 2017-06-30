from zap import StoreClient
import requests

# EXAMPLE USE CASE
# Retreive deal_id from the StoreClient where we saved it in example_1A

input_data = {'order_id': '1001'}

output = {}

# When you're done Testing Locally, Copy/Paste Code in between Tags
########################### ZAPIER CODE #######################################

"""
The Shopify Order has been Updated Triggering this Zap, we need to Update the
HubSpot Deal ID, so we grab it from the StoreClient
"""

order_id = input_data['order_id']
store = StoreClient('Your Secret')

output = {'deal_id': store.get(order_id)}

# Cleanup Store after we're done with the Order
# (Assuming you won't need it again later)
# Otherwise you will eventually max out the capcity (500 keys)
# in your StoreClient, causing your Zaps to fail
store.delete(order_id)


######################## END ZAPIER CODE ######################################


# For Teesting Output
# Display New Fields available to Zap's Next Steps

def print_output():
    print("Field Name: Value")
    for k, v in output.items():
        print("{}: {}".format(k, v))

print_output()

# >>> 'deal_id: 12345'
# You can now use create a HubSpot Update Deal Action in your
# Next step to Update the Deal as needed.
