from my_blog.blueprints.social_profile.models import UserProfile
import json


class TestModel(object):
    """
    Class that contains models testing methods
    """
    def test_social_profile(self):
        """
        Tests to_json() and deserialize() methods of object UserProfile
        :return: True if properties of deserialized object match original one`s
        """
        profile = UserProfile(name='test',
                              oauth_provider='google',
                              picture_url='path')
        profile_json = profile.to_json()
        deserialized_profile = json.loads(profile_json,
                                          object_hook=UserProfile.deserialize)
        assert 'test' in deserialized_profile.name
        assert 'google' in deserialized_profile.oauth_provider
        assert 'path' in deserialized_profile.picture_url
