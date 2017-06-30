"""
Full (though crappy) Documentation on Python Zaps available here:
https://zapier.com/help/code-python/

The environment is vanilla Python 2.7.10. Your script is sandboxed
and can only run for a limited amount of time and within a limited
amount of memory. If you exceed those limits - your script will be
killed

REQUESTS is the only module available outside the standard library
There is no method to import/install other libraries

You may import any module inside the standard library with the import
statement. List of Standard library modules for reference:
https://docs.python.org/2.7/py-modindex.html

Example:
import re
from random import randint


Use Cases:
- Transform incorrect dates or convert between other data types.
- Use custom regular expressions to extract extra data like emails
  or tracking numbers from large text blobs.
- Make an extra API call to a different service with requests
  without building a full dev app.
- Augment data from a trigger with extra data from some other source
  (either generated or external API).
- Anything else you can dream up!



############ INPUT DATA ################
Create and fill input_data dictionary to mirror functionality of
Zapier's Input Data fields in the Run Python Zap
"""
input_data = {}
output = {}
"""
# Set/Get Input Data (Implemented as Dictionary)
# Example:
input_data['order_number'] = 1019
value = input_data['order_number']
print(value)
>>> 1019

NOTE: All Input Data values are returned as string literals
"""
input_data['order_number'] = u'39849829857'
"""
############ ZAP STORE #################
The StoreClient allows you save data for later use. Use this if
your current Zap can't store data you'll need for a later one.
I've created a simple Class that mimics the behavior for testing.

Storing and retrieving data with StoreClient is very simple.
There is no need to import it - it comes pre-imported in your Code environment.

NOTE: 500 Key Limit
Make sure you Delete Keys when you're done with them

Example Usage:
store = StoreClient('ZvRjAWvxEg9Rpatj')
store.set('hello', 'world')
value = store.get('hello')
print(value)
>>> 'world'
store.delete('hello')

More documentation here
https://zapier.com/help/code-python/#storeclient-python
"""
