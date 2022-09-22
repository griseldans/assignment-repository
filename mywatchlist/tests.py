from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.views import show_watchlist, show_json, show_xml

class TestFunction(TestCase):
    def test_show_watchlist(self):
        klien = Client()
        respon = klien.get(reverse("mywatchlist:show_watchlist"))
        self.assertEqual(respon.status_code, 200)

    def test_show_json(self):
        klien = Client()
        respon = klien.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(respon.status_code, 200)

    def test_show_watchlist(self):
        klien = Client()
        respon = klien.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(respon.status_code, 200)
