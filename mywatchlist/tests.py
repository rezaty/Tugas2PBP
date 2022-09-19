from django.test import TestCase, Client 
class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_url(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
# Create your tests here.
