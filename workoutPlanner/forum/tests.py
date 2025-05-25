from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from workoutPlanner.forum.models import Post

User = get_user_model()

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
        self.url = reverse('api-post-list-create')  # Make sure your api_urls.py has a name='api-post-list-create'

    def test_create_post_successfully(self):
        data = {
            'title': 'Test Post',
            'body': 'This is a test body',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, 'Test Post')

    def test_create_post_missing_title(self):
        data = {
            'body': 'No title here'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_create_post_unauthenticated(self):
        self.client.logout()
        data = {
            'title': 'Should Fail',
            'body': 'No auth'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # if you use IsAuthenticated

