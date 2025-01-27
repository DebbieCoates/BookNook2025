from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Member

# Model Tests
class MemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        if not Member.objects.filter(user=cls.user).exists():
            Member.objects.create(user=cls.user, bio='Test bio', location='Test location')

    def test_member_str(self):
        member = Member.objects.get(user=self.user)
        expected_object_name = f'{member}'
        self.assertEqual(expected_object_name, "testuser's member profile")

# View Tests
class MemberViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        if not Member.objects.filter(user=cls.user).exists():
            cls.member = Member.objects.create(user=cls.user, bio='Test bio', location='Test location')

    def setUp(self):
        self.client.login(username='testuser', password='testpass')

    def test_member_profile_view(self):
        response = self.client.get(reverse('member_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'member/member_profile.html')

    def test_update_member_view(self):
        response = self.client.get(reverse('update_member'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'member/update_member.html')
