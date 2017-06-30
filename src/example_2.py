from zap import StoreClient
import requests

# EXAMPLE USE CASE
# Shopify does not have an "Update Order" Action in Zapier
# We make a call directly to their API to solve this problem.
# Say we get Tracking Infomation from another App and place
# them in our Input Data fields

input_data = {
    "order_id": '1001',
    "line_item_id": '33333333',
    "tracking_number": "1234567890",
    "carrier": "USPS"
}


output = {}

# When you're done Testing Locally, Copy/Paste Code in between Tags
########################### ZAPIER CODE #######################################

# Pull Data from Previous Steps in Zap
order_id = input_data["order_id"]
line_item_id = input_data["line_item_id"]
tracking_number = input_data['tracking_number']
carrier = input_data['carrier']

# Pull API Keys from our Secret Store
store = StoreClient('Your Secret')
api_key = store.get('Shopify_API_KEY')
password = store.get('Shopify_PASSWORD')
store_name = "abcsuperstore"


def fulfill_order():
    """
    Set Shopify Order status to fulfilled and add Tracking information
    This also Triggers 'Order Shipped' Email to Customer
    """
    endpoint = "https://{}:{}@{}.myshopify.com/admin/orders/{}/fulfillments.json".format(api_key,
                                                                                         password,
                                                                                         store_name,
                                                                                         order_id)
    params = {
        "fulfillment": {
            "tracking_number": tracking_number,
            "tracking_company": carrier,
            "line_items": [
                {
                    "id": line_item_id
                }
            ]
        }
    }

    r = requests.post(endpoint, json=params)
    r.raise_for_status()
    return r

# Supplying output with the response Json makes it available for other Steps
# You might also decide to do some Error catching here based on the json
# response, in case of failures

output = fulfill_order().json()

######################## END ZAPIER CODE ######################################


# For Teesting Output
# Display New Fields available to Zap's Next Steps

def print_output():
    print("Field Name: Value")
    for k, v in output.items():
        print("{}: {}".format(k, v))

print_output()
# Shopify's Response is too long to Post here, but you can use any variable
# in the resulting JSON in steps after this one.
