from django.test import TestCase
# from katalog.models import CatalogItem

# class BarangTestCase(TestCase):
#     def setUp(self):
#         CatalogItem.objects.create(item_name="iPhone", description="mahal")
#         CatalogItem.objects.create(item_name="Ayam Bakar Balgebun", description="murah")

#     def barang_bisa_dibeli_sekarang(self):
#         """Barang yang saat ini juga bisa langsung didapatkan"""
#         iphone = CatalogItem.objects.get(item_name="iPhone")
#         ayam = CatalogItem.objects.get(item_name="Ayam Bakar Balgebun")
#         self.assertEqual(iphone.get() , "iPhone tidak bisa dibeli sekarang")
#         self.assertEqual(ayam.beli(), "Ayam Bakar Balgebun bisa dibeli sekarang juga, kecuali tutup")