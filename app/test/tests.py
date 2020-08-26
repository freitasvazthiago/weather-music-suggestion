from django.test import Client, TestCase
from weather.views import MusicView

from faker import Faker


class MusicViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        # creating instance of a client.
        super(MusicViewTests, cls).setUpClass()

    def test_get(self):
        self.fake = Faker('pt_br')
        self.client = Client()

        print(self.fake.city())
        # Issue a GET request.
        response = self.client.get('/weather/' + self.fake.city() + '/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

class StatisticViewTests(TestCase):
    
    @classmethod
    def setUpClass(cls):
        # creating instance of a client.
        super(StatisticViewTests, cls).setUpClass()

    def test_get(self):
        self.client = Client()
        # Issue a GET request.
        response = self.client.get('/statistic/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)