from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from unittest.mock import patch


class EventViewsTest(TestCase):
    
    @patch('events.views.get_events_from_api')
    def test_monthly_view(self, mock_get_events):
        mock_get_events.return_value = [
            {
                "id": 1,
                "name": "Test Event",
                "start_time": "2024-10-02T10:00:00",
                "duration": 120,
                "location": "Test Location",
                "short_description": "Test short description",
                "long_description": "Test long description",
                "tags": [{"id": 1, "name": "Tag1"}],
                "registration_link": "http://test-registration.com"
            }
        ]

        response = self.client.get(reverse('monthly_view_default'))

        print(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Start:')
        self.assertContains(response, '02.10.2024')
        self.assertContains(response, '10:00')


    @patch('events.views.get_events_from_api')
    def test_event_detail_view(self, mock_get_events):
        mock_event = {
            "id": 1,
            "name": "Test Event",
            "start_time": "2024-10-02T10:00:00",
            "duration": 120,
            "location": "Test Location",
            "tags": [{"id": 1, "name": "Tag1"}]
        }
        
        mock_get_events.return_value = [mock_event]  

        response = self.client.get(reverse('event_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Start: 02 October 2024, 10:00')

    @patch('events.views.get_events_from_api')
    def test_filter_events_by_tag(self, mock_get_events):
        mock_get_events.return_value = [
            {
                "id": 1,
                "name": "Test Event",
                "start_time": "2024-10-02T10:00:00",
                "duration": 120,
                "location": "Test Location",
                "short_description": "Test short description",
                "long_description": "Test long description",
                "tags": [{"id": 1, "name": "Tag1"}],
                "registration_link": "http://test-registration.com"
            }
        ]

        response = self.client.get(reverse('monthly_view_default'), {'tag': 'Tag1'})

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Test Event')
        self.assertContains(response, 'Tag1')

        self.assertNotContains(response, 'Tag2')
