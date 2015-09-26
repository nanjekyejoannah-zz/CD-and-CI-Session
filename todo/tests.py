
from django.test import TestCase


class CodefishTest(TestCase):
    def test_entered_the_home_page(self):
        response = self.client.get('/')
        self.assertContains(response, "yaya ")

    def test_leads_to_the_create_page(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="/create">' )
