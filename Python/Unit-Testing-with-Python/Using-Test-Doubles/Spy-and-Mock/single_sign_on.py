import random


class SingleSignOnRegistry:

    def register_new_session(self, credentials):
        """Returns an instance of SSOToken if the credentials are valid"""
        pass

    def is_valid(self, token):
        """Return True if the token is refers to a current session"""
        pass

    def unregistered(self, token):
        """Remove the given token from current sessions"""
        pass


class SSOToken:
    def __init__(self):
        self.id = random.randrange(10000)

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return str(self.id)
