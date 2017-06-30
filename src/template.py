from zap import StoreClient
import requests

# This Template Replicates Zapier's Environment
# If your code inbetween the "ZAPIER CODE" Tags works locally,
# You should be able to Copy/Paste it to your Zapier Code Step

# Fill input_data with test values you'll bring in form previous Zap Steps
# Do this above the "ZAPIER CODE" line so everything within the Zapier tags
# mimic Zapier Enviornment
# Example:
# input_data = {"order_id": "1001", "email": "test@email.com"}
input_data = {}
# or:
# input_data["order_id"] = "1001"
# input_data["email"] = "test@email.com"

output = {}

# When you're done Testing Locally, Copy/Paste Code in between Tags
########################### ZAPIER CODE #######################################


# NOTE: output must be JSON serializable
output = {"Dictionary": "With fields that will be available in later Steps"}

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
