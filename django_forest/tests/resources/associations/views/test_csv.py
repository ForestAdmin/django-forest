import copy
import sys
from datetime import datetime
from unittest import mock

import pytest
import pytz
from django.test import TransactionTestCase
from django.urls import reverse

from django_forest.tests.fixtures.schema import test_schema
from django_forest.utils.schema import Schema
from django_forest.utils.schema.json_api_schema import JsonApiSchema


# reset forest config dir auto import
from django_forest.utils.scope import ScopeManager


@pytest.fixture()
def reset_config_dir_import():
    for key in list(sys.modules.keys()):
        if key.startswith('django_forest.tests.forest'):
            del sys.modules[key]


@pytest.mark.usefixtures('reset_config_dir_import')
class ResourceAssociationCsvViewTests(TransactionTestCase):
    fixtures = ['question.json', 'choice.json']

    def setUp(self):
        Schema.schema = copy.deepcopy(test_schema)
        Schema.add_smart_features()
        Schema.handle_json_api_schema()
        self.url = reverse('django_forest:resources:associations:csv',
                           kwargs={'resource': 'Question', 'pk': 1, 'association_resource': 'choice_set'})
        self.reverse_url = reverse('django_forest:resources:associations:csv',
                                   kwargs={'resource': 'Choice', 'pk': 1, 'association_resource': 'question'})
        self.bad_association_url = reverse('django_forest:resources:associations:csv',
                                           kwargs={'resource': 'Question', 'pk': 1, 'association_resource': 'foo'})
        self.client = self.client_class(
            HTTP_AUTHORIZATION='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUiLCJlbWFpbCI6Imd1aWxsYXVtZWNAZm9yZXN0YWRtaW4uY29tIiwiZmlyc3RfbmFtZSI6Ikd1aWxsYXVtZSIsImxhc3RfbmFtZSI6IkNpc2NvIiwidGVhbSI6Ik9wZXJhdGlvbnMiLCJyZW5kZXJpbmdfaWQiOjEsImV4cCI6MTYyNTY3OTYyNi44ODYwMTh9.mHjA05yvMr99gFMuFv0SnPDCeOd2ZyMSN868V7lsjnw')
        ScopeManager.cache = {
            '1': {
                'scopes': {},
                'fetched_at': datetime(2021, 7, 8, 9, 20, 22, 582772, tzinfo=pytz.UTC)
            }
        }

    def tearDown(self):
        # reset _registry after each test
        JsonApiSchema._registry = {}
        ScopeManager.cache = {}

    @mock.patch('jose.jwt.decode', return_value={'id': 1, 'rendering_id': 1})
    @mock.patch('django_forest.utils.scope.datetime')
    def test_get(self, mocked_datetime, mocked_decode):
        mocked_datetime.now.return_value = datetime(2021, 7, 8, 9, 20, 23, 582772, tzinfo=pytz.UTC)
        response = self.client.get(self.url, {
            'fields[Choice]': 'id,question,choice_text',
            'fields[question]': 'question_text',
            'search': '',
            'searchExtended': '',
            'filename': 'choices',
            'header': 'id,question,choice text',
            'timezone': 'Europe/Paris'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'id,question,choice text\r\n1,what is your favorite color?,yes\r\n2,what is your favorite color?,no\r\n')

    def test_get_no_association(self):
        response = self.client.get(self.bad_association_url, {
            'fields[Choice]': 'id,question,choice_text',
            'fields[question]': 'question_text',
            'search': '',
            'searchExtended': '',
            'filename': 'choices',
            'header': 'id,question,choice text',
            'timezone': 'Europe/Paris'
        })
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data, {'errors': [{'detail': 'cannot find association resource foo for Model Question'}]})
