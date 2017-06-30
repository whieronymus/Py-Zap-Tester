import sys


class StoreClient():
    secrets = {
        "Your Secret": {
            'Hello': 'World',
            'Foo': 'Bar',
            'Test 1': 'Value 1',
            'Shopify_API_KEY': "XXXXXXXXXXXXXXX",
            'Shopify_PASSWORD': "YYYYYYYYYYYYYYY",
            '1001': '12345'
        }
    }

    def __init__(self, secret):
        if secret in self.secrets:
            print("Existing Secret Storage")

        else:
            self.add_new_secret(secret)

        self.secret_key = secret
        self.storage = self.secrets[secret]

    def set(self, key, value):
        self.validate_capacity()
        self.validate_key(key)
        self.validate_value(value)
        self.storage[key] = value

    def set_many(self, *args, **kwargs):
        if args:
            if len(args) > 1 or type(args[0]) is not dict:
                raise Exception("Only accepts 1 dict as arg")
            [self.set(key, args[0][key]) for key in args[0]]
        if kwargs:
            [self.set(key, kwargs[key]) for key in kwargs]

    def get(self, key):
        return self.storage[key]

    def get_many(self, *args):
        if len(args) == 1:
            if type(args[0]) == str:
                return self.get(args[0])
            elif type(args[0]) in [list, dict]:
                return dict((key, self.get(key)) for key in args[0])
            else:
                raise Exception("Expected str, list or dict")
        else:
            return dict((key, self.get(key)) for key in args)

    def delete(self, key):
        del self.storage[key]

    def delete_many(self, *args):
        if len(args) == 1:
            if type(args[0]) == str:
                self.delete(args[0])
            elif type(args[0]) in [list, dict]:
                dict((key, self.delete(key)) for key in args[0])
            else:
                raise Exception("Expected str, list or dict")
        else:
            dict((key, self.delete(key)) for key in args)

    def clear(self):
        self.storage = {}

    def add_new_secret(self, key):
        self.validate_key(key)
        self.secrets[key] = {}

    def validate_key(self, key):
        if len(key) < 32:
            return True
        raise Exception("Keys must be under 32 chars in length")

    def validate_capacity(self):
        if len(self.storage) <= 500:
            return True
        raise Exception("You have reached your 500 key maximum")

    def validate_value(self, value):
        if sys.getsizeof(value) < 2500:
            return True
        raise Exception("Value must be under 2500 bytes")
