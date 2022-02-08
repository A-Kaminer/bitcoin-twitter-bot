class Authorization:
    """
Key file format:
consumer_key:###############
consumer_secret:################
access_token:################
access_token_secret:####################
    """
    def __init__(self):
        with open("keys", "r") as keys:
            l = keys.readlines()
        l = [element.split(":") for element in l]
        dictionary = {}
        for element in l:
            dictionary[element[0]] = element[1]
            
        self.consumer_key = dictionary["consumer_key"]
        self.consumer_secret = dictionary["consumer_secret"]
        self.access_token = dictionary["access_token"]
        self.access_token_secret = dictionary["access_token_secret"]

    def get_consumer_key(self):
        return self.consumer_key

    def get_consumer_secret(self):
        return self.consumer_secret

    def get_access_token(self):
        return self.access_token

    def get_access_token_secret(self):
        return self.access_token_secret

    def print_keys(self):
        print(f"consumer_key:{self.get_consumer_key()}")
        print(f"consumer_secret:{self.get_consumer_secret()}")
        print(f"access_token:{self.get_access_token()}")
        print(f"access_token_secret:{self.get_access_token_secret()}")
