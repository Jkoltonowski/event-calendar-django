from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class MonthlyViewTest(TestCase):

    @patch('events.views.get_events_from_api')
    def test_monthly_view(self, mock_get_events):
        mock_get_events.return_value = [
            {
                'id': 1,
                'name': 'Test Event',
                'start_time': '2024-09-15T10:00:00',
                'tags': [{'name': 'Tag1'}]
            }
        ]

        client = Client()
        response = client.get(reverse('monthly_view', args=[2024, 9]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

class EventDetailTest(TestCase):

    @patch('events.views.requests.get')
    def test_event_detail_view(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'id': 1,
            'name': 'Test Event',
            'start_time': '2024-09-15T10:00:00'
        }

        client = Client()
        response = client.get(reverse('event_detail', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')
