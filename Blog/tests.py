
# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post
class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            Title='A good Title',
            Body='Nice Body content',
            Author=self.user,
        )

    def test_string_representation(self):
        post = Post(Title='A sample Title')
        self.assertEqual(str(post), post.Title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.Title}', 'A good Title')
        self.assertEqual(f'{self.post.Author}', 'testuser')
        self.assertEqual(f'{self.post.Body}', 'Nice Body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body content')
        self.assertTemplateUsed(response, 'Home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good Title')
        self.assertTemplateUsed(response, 'post_detail.html')

# Create your tests here.
