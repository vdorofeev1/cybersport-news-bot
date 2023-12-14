import unittest
from script.cybersport_requests import login_request, materials_request, slug_request


class CyberSportRequestsTest(unittest.TestCase):
    login_url = 'https://www.cybersport.ru/api/identity/login'
    materials_url = 'https://www.cybersport.ru/api/materials?page%5Blimit%5D=5&filter%5Bmain%5D=true'
    slug_url = 'https://www.cybersport.ru/api/materials/slug/'

    @classmethod
    def setUpClass(cls):
        login_response = login_request.login_request(cls.login_url)
        cls.login_token = login_response["token"]
        cls.login_refresh_token = login_response["refresh_token"]
        login_status_code = int(login_response["status_code"])

        assert login_status_code == 200, "Login failed"

    def test_materials_request(self):
        materials_response = materials_request.materials_request(self.login_token, self.login_refresh_token,
                                                                 CyberSportRequestsTest.materials_url)
        materials_status_code = materials_response["status_code"]

        self.assertEqual(materials_status_code, 200)

    def test_slug_request(self):
        slug = 'mouz-vybila-heroic-iz-blast-premier-world-final-2023'

        slug_response = slug_request.slug_request(slug, self.login_token, self.login_refresh_token,
                                                  CyberSportRequestsTest.slug_url)
        slug_status_code = slug_response["status_code"]

        self.assertEqual(slug_status_code, 200)
