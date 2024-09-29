To jest aplikacja stworzona w Django, która pełni funkcję kalendarza wydarzeń. Umożliwia przeglądanie wydarzeń na podstawie miesiąca oraz wyświetlanie szczegółowych informacji o każdym z wydarzeń.

Funkcjonalności
Widok miesięczny wydarzeń.
Filtracja wydarzeń po tagach.
Szczegóły każdego wydarzenia.


Wymagania
Python 3.9 lub nowszy
Django 4.x

Instalacja
Sklonuj repozytorium:
git clone https://github.com/yourusername/event-calendar-django.git
cd event-calendar-django

Zainstaluj wymagane zależności:
pip install -r requirements.txt

Zainicjuj bazę danych:
python manage.py migrate

Uruchom serwer deweloperski:
python manage.py runserver

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/
