# ZAPIER PYTHON CODE TEST ENVIRONMENT

The purpose of this App is to give Zapier users helpful information
when using the Code (Python) Step in Zapier.

I've done my best to mimic Zapier's Environment so you can code
locally on your machine and get the same results as you will see
when testing or running your Zap on Zapier.

Debugging is far easier when done locally, rather than on Zapier.
There are no real debugging tools when using the Zapier editor, and
it doesn't always even give you an error description at all when
running code.

I spent several days of frustration before really understanding
the limitations and capabilities of code steps on Zapier. So I'm
hoping to help those in a similar situation from having to go
through the frustrating steps I did. If you're new to Zapier and
would like to create Code Steps to give you more flexibility in the
Zapier platform itself, I believe you have come to the right place.


### Contents:

* Zapier Template
* zap.StoreClient
* Real world "Code" Step examples
* General Advice and Help using Zapier Code Step


#### Zapier Template

This file should be used to create every new code step in Zapier.
You shouldn't need to touch the Zapier Editor until you already
have your code running bug free locally using the template. At that
point you can copy and paste your code from your local files directly
into the Zapier Editor and assuming your inputs are valid, have the
same success on Zapier. Storing you code locally also allows you
to upload your Code to Git/GitHub/etc with version control so you
don't accidentally delete a zap that had 2 hours of code time spent
on it (like I did).

I've only been using it a short time, but I believe it completely
replicates the Zapier Environment. I know there are probably a few
bugs and use cases that don't match exactly, but I haven't run into
them yet, and when I do I will do my best to keep this update with
fixes. Please feel free to create issues if you notice any problems.

There really isn't a lot of code to the template, but having something
like this when I started using Zapier would have saved me a lot of
time.


#### StoreClient

Zapier's Store Client is a small cloud based storage system you
can use to store data in your Zaps. You could in theory store it
in a Google Sheet or something as well, but in my opinion, there
are many use cases better suited for StoreClient than storing
small bits of data elsewhere. See the examples for a few.

You can view Zapier's StoreClient Documentation here:
https://zapier.com/help/code-python/#storeclient-python

The largest code compenent of this Project is a StoreClient class
that is used to mimic the StoreClient's functionality locally.
I'm implemented all the methods with I believe the same validation
as Zapier's StoreClient.

The biggest caveat to using the local version vs
you can run locally to Test Python Code you plan to use on Zapier is
that after runtime your data is does not remain. There are a couple
workarounds for this if you'd like to test code across multiple steps.
I'll add them later on if anyone would like suggestions.

If there are issues or you have ideas to expand please create an issue
and pass the ideas my way!


#### Real World Examples

There are only a couple examples at the moment:

The first one uses the Store Client to store some data across multiple
steps

And the second one is an example of using an API Call that isn't
available to the App in Zapier.

If you have suggestions for additional samples please let me know.
Also, feel free to let me know what creative ways you're using it!



#### General Advice and Help using Zapier Code Step


"Full" Documentation on Python Code Zaps available here:
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


##### INPUT DATA
Create and fill input_data dictionary to mirror functionality of
Zapier's Input Data fields in the Run Python Zap

`input_data = {}`
`output = {}`

###### Set/Get Input Data (Implemented as Dictionary)

Example:
`input_data['order_number'] = 1019`
`value = input_data['order_number']`
`print(value)`
>>> 1019

NOTE: All Input Data values are returned as string literals
`input_data['order_number'] = u'39849829857'`


############ ZAP STORE #################
The StoreClient allows you save data for later use. Use this if
your current Zap can't store data you'll need for a later one.
I've created a simple Class that mimics the behavior for testing.

Storing and retrieving data with StoreClient is very simple.
There is no need to import it - it comes pre-imported in your Code environment.

NOTE: 500 Key Limit
Make sure you Delete Keys when you're done with them

Example Usage:
`store = StoreClient('Your Secret')`
`store.set('hello', 'world')`
`value = store.get('hello')`
`print(value)`
>>> 'world'
`store.delete('hello')`


