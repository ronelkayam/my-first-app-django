from django.test import TestCase,Client
from django.urls import reverse
from django.db.utils import IntegrityError
from .models import Member


class GymTrackerTests(TestCase):

    def setUp(self):
        """
        run Automatically before each test.
        prepare data to test
        """
        self.client=Client()# for HTTP request
        self.member1 = Member.objects.create(
            first_name="Alon",
            last_name="Smith",
            email="Alon@gmaill.com",
        )

    #Models Tests

    def test_1_member_creation(self):
        member2 = Member.objects.get(email = 'Alon@gmaill.com')
        self.assertEqual(member2.first_name, 'Alon')
        self.assertEqual(member2.last_name, 'Smith')

    def test_2_member_str_representation(self):
        excepted_ste = "Alon Smith"
        self.assertEqual(str(self.member1), excepted_ste)

    def test_3_member_unique__email_constraint(self):
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name="Alon",
                last_name="Smith",
                email = "Alon@gmaill.com"
            )

    #urls & views

    def test_4_member_list_view_status_code(self):
        response = self.client.get(reverse('member_list'))
        self.assertEqual(response.status_code, 200)

    def test_5_member_list_view_template_used(self):
        response = self.client.get(reverse('member_list'))
        self.assertTemplateUsed(response, 'gym_tracker/member_list.html')


    def test_6_member_list_view_context_data(self):
        response = self.client.get(reverse('member_list'))
        self.assertIn(self.member1, response.context['members'])