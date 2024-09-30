import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta
def get_events_from_api(tag=None):
    api_key = settings.API_KEY
    url = f'{settings.API_BASE_URL}/events/'
    headers = {'api-key': api_key}
    
    if tag:
        url += f'?tag={tag}'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  
    return []

def monthly_view(request, year=None, month=None):
    current_year = datetime.now().year
    current_month = datetime.now().month

    if not year or not month:
        year = current_year
        month = current_month

    all_events = get_events_from_api()

    for event in all_events:
        if 'start_time' in event:
            event['start_time'] = datetime.strptime(event['start_time'], '%Y-%m-%dT%H:%M:%S')

    filtered_events = [event for event in all_events if event['start_time'].year == year and event['start_time'].month == month]

    previous_month_date = datetime(year, month, 1) - timedelta(days=1)
    next_month_date = datetime(year, month, 28) + timedelta(days=4)

    previous_month = previous_month_date.month
    previous_year = previous_month_date.year
    next_month = next_month_date.month
    next_year = next_month_date.year

    tags = {tag['name'] for event in all_events for tag in event['tags']}

    selected_tag = request.GET.get('tag', None)

    if selected_tag:
        filtered_events = [event for event in filtered_events if any(tag['name'] == selected_tag for tag in event['tags'])]

    return render(request, 'events/monthly_view.html', {
        'events': filtered_events,
        'tags': tags,
        'selected_tag': selected_tag,
        'year': year,
        'month': month,
        'previous_month': previous_month,
        'previous_year': previous_year,
        'next_month': next_month,
        'next_year': next_year,
        'current_year': current_year,
        'current_month': current_month
    })



def event_detail(request, event_id):
    url = f"{settings.API_BASE_URL}/events/{event_id}/"
    headers = {'api-key': settings.API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        event = response.json()
        if 'start_time' in event:
            event['start_time'] = datetime.strptime(event['start_time'], '%Y-%m-%dT%H:%M:%S')

        return render(request, 'events/event_detail.html', {'event': event})
    else:
        return render(request, 'events/event_not_found.html', status=404)

def filter_events_by_tag(request):
    tag = request.GET.get('tag', None)
    events = get_events_from_api(tag=tag)
    return render(request, 'events/filtered_events.html', {'events': events, 'tag': tag})
def get_available_tags_from_api():
    api_key = settings.API_KEY
    url = f'{settings.API_BASE_URL}/tags/'
    headers = {'api-key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  
    return []
def calendar_view(request):
    
    selected_tag = request.GET.get('tag')  
    events = get_events_from_api()
    
    available_tags = {tag['name'] for event in events for tag in event['tags']}
    
    if selected_tag:
        events = [event for event in events if any(tag['name'] == selected_tag for tag in event['tags'])]
    
    return render(request, 'events/calendar_view.html', {
        'events': events,
        'tags': available_tags,
        'selected_tag': selected_tag,
        'year': datetime.now().year,
        'month': datetime.now().month
    })
def home(request):
    return render(request, 'events/home.html')