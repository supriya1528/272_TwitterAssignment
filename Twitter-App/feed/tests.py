
#import unittest

#from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from .views import index
import datetime
import time
import re





# Supriya Contribution#

class TestCase(TestCase):
   
    def test_index_loads_(self):
        print("Test case to check if url is responsponding")
        response=self.client.get('http://127.0.0.1:8000')
        print(response.status_code)
        self.assertEqual(response.status_code,200)
        print("Test Successful")

        #Mohana Contribution#

     
    def test_create(self):
        self.factory = RequestFactory()
        print("To check if tweet is created")
        request = self.factory.post('',{"content":"create: "+str(datetime.datetime.now())})
        response = index(request)
        print(response)
        self.assertEqual(response.status_code, 200)
        print("Test successful")

        # Varun Contribution #

    def test_delete(self):
        time.sleep(5)
        self.factory=RequestFactory()
        request = self.factory.post('',{"content":"Delete: "+str(datetime.datetime.now())})
        response = index(request)
        match_string = re.search("\/status\/[0-9].*\"",response.content.decode('utf-8'))
        tmp_id = match_string[0].split("/")[2].split("\"")[0]
        time.sleep(5)
        request= self.factory.post('',{"ID":str(tmp_id)})
        response=index(request)
        print("Tweet Deleted!")
        self.assertEqual(response.url, "delete.html")
        print("delete tweets ")

        # Kevin Contribution#

    def test_getQuery(self):
        self.factory = RequestFactory()
        print("retrieve")
        request = self.factory.post('',{"getQuery":"Dogs"})
        response = index(request)
        total_count = len(re.findall("\<li\>",response.content.decode('utf-8')))
        self.assertTrue(total_count>0)
        print(" We need a twitter developer premium account for this case to be success")






