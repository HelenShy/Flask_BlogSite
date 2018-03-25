import json


class UserProfile:
    def __init__(self, name, oauth_provider, picture_url):
        """

        :param name:
        :param oauth_provider:
        :param picture_url:
        """
        self.name = name
        self.oauth_provider = oauth_provider
        self.picture_url = picture_url

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    @classmethod
    def deserialize(cls, dct):
        return cls(dct['name'], dct['oauth_provider'], dct['picture_url'])
