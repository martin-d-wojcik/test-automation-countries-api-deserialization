from unittest import TestCase
import requests
from jsonschema import validate
from helper.response import ResponseHelper
from rest_api.country import Endpoints, JsonSchemas
from rest_api import country_custom_class


class TestCountries(TestCase):
    def test_get_country_by_name(self):
        # prepare
        url = Endpoints.country_by_name.format('denmark')

        # perform
        response = requests.get(url)
        native_name = ResponseHelper.get_value_from_response(response, 'nativeName')
        country_object = country_custom_class.get_deserialized_object(response)

        # assert
        capital_from_object = country_object.capital
        translations_nl_from_object = country_object.translations.nl
        self.assertEqual(response.status_code, 200)
        self.assertEqual(capital_from_object, 'Copenhagen')
        self.assertEqual(translations_nl_from_object, 'Denemarken')
        validate(response.json(), JsonSchemas.country_by_name)
