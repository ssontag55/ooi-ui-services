#!/usr/bin/env python
'''
unit testing for simple data access

'''
__author__ = 'andybird'

import unittest
from flask import url_for
from ooiservices.app import create_app, db
import requests
import json

'''
These tests are used to validate and test the getting of data for the ui plotting services
'''

class UframeDataTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TESTING_CONFIG')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
''' TODO: rewrite tests to reflect data from uframe
    def test_get_data_from_uframe_simple_ok(self):
        response = self.client.get('/uframe/get_data', content_type='application/json')
        self.assertTrue(response.status_code == 200)

    def test_get_data_from_uframe_simple_no_annotation(self):
        response = self.client.get('/uframe/get_data', content_type='application/json')
        data = json.loads(response.data)
        self.assertFalse("annotation" in str(data['cols']))
        self.assertFalse("annotationText" in str(data['cols']))

    def test_get_data_from_uframe_ok(self):
        response = self.client.get('/uframe/get_data?annotation=false', content_type='application/json')
        self.assertTrue(response.status_code == requests.codes.ok)

    def test_get_data_from_uframe_has_cols(self):
        response = self.client.get('/uframe/get_data?annotation=false', content_type='application/json')
        data = json.loads(response.data)
        self.assertTrue("cols" in data)

    def test_get_data_from_uframe_has_rows(self):
        response = self.client.get('/uframe/get_data?annotation=false', content_type='application/json')
        data = json.loads(response.data)
        self.assertTrue("rows" in data)

    def test_get_data_from_uframe_has_annotations(self):
        'CHECK annotations exist in the data'
        response = self.client.get('/uframe/get_data?annotation=true', content_type='application/json')
        data = json.loads(response.data)
        self.assertTrue("annotation" in str(data['cols']))
        self.assertTrue("annotationText" in str(data['cols']))

    def test_get_data_from_uframe_has_correct_col_length(self):
        'CHECK data lenfth'
        response = self.client.get('/uframe/get_data?annotation=false', content_type='application/json')
        data = json.loads(response.data)
        col_length = len(data['cols'])
        row_col_length = len(data['rows'][0]['c'])
        self.assertTrue(col_length == row_col_length)
'''