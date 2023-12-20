import unittest
from script.cybersport_requests import materials_request, slug_request


class CyberSportRequestsTest(unittest.TestCase):
    materials_url = 'https://www.cybersport.ru/api/materials?page%5Blimit%5D=5&filter%5Bmain%5D=true'
    slug_url = 'https://www.cybersport.ru/api/materials/slug/'

    def test_materials_request(self):
        materials_response = materials_request.materials_request(CyberSportRequestsTest.materials_url)
        materials_status_code = materials_response["status_code"]

        self.assertEqual(materials_status_code, 200)

    def test_slug_request(self):
        slug = 'mouz-vybila-heroic-iz-blast-premier-world-final-2023'

        slug_response = slug_request.slug_request(slug, CyberSportRequestsTest.slug_url)
        slug_status_code = slug_response["status_code"]

        self.assertEqual(slug_status_code, 200)
