from django.test import TestCase
from django.urls import reverse

class SnackTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        # print(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    # def test_detail_status_code(self):
    #     url = reverse('snack_detail')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
        
    # def test_detail_page_template(self):
    #     url = reverse('snack_detail')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_detail.html")
    #     self.assertTemplateUsed(response, "base.html")

    def test_wrong_uri_returns_404(self):
        response = self.client.get('templates/blog')
        self.assertEqual(response.status_code, 404)