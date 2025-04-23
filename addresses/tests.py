from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class AddressTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_empty_q_returns_400(self):
        response = self.client.post("/api/addresses/", {"q": ""}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_missing_q_returns_400(self):
        response = self.client.post("/api/addresses/", {}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_valid_q_returns_200_or_404(self):
        # Remplace par une adresse valide que tu sais reconnue par l'API utilisée dans ta vue
        response = self.client.post("/api/addresses/", {"q": "10 rue de Rivoli, Paris"}, format='json')
        self.assertIn(response.status_code, [200, 404])  # L'API externe peut renvoyer 404 si pas trouvée
        self.assertTrue("error" in response.json() or "results" in response.json())

    def test_q_with_only_spaces_returns_400(self):
        response = self.client.post("/api/addresses/", {"q": "    "}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
