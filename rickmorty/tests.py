from django.test import TestCase

# Create your tests here.
from nose.tools import assert_is_not_none

# Local imports...
from .services import get_characters

class CharacterTestCase(TestCase):
    def test_request_response(self):
        # Call the service, which will send a request to the server.
        response = get_characters()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_is_not_none(response)