from zap import StoreClient
import requests

# EXAMPLE USE CASE
# Shopify does not have an "Update Order" Action in Zapier
# We make a call directly to their API to solve this problem.

input_data = {"order_id": '1001', "deal_id": "12345"}


output = {}

# When you're done Testing Locally, Copy/Paste Code in between Tags
########################### ZAPIER CODE #######################################





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
