Event Calendar - Aplikacja Kalendarza Wydarzeń
Event Calendar to aplikacja stworzona w Django, która umożliwia przeglądanie oraz zarządzanie wydarzeniami w kalendarzu. Wydarzenia są pobierane z zewnętrznego API, dzięki czemu nie ma potrzeby tworzenia lokalnej bazy danych. Użytkownicy mogą przeglądać wydarzenia na podstawie miesiąca, filtrować je po tagach oraz wyświetlać szczegółowe informacje o każdym z wydarzeń.

Funkcjonalności
Widok kalendarza: Możliwość przeglądania wydarzeń w widoku miesięcznym, tygodniowym i dziennym.
Widok kafelkowy: Alternatywny widok kafelkowy do przeglądania wydarzeń w danym miesiącu.
Filtracja po tagach: Umożliwia filtrowanie wydarzeń na podstawie przypisanych tagów.
Szczegóły wydarzenia: Wyświetlanie szczegółowych informacji o wybranym wydarzeniu, w tym opisu, daty rozpoczęcia, lokalizacji i możliwości rejestracji (jeśli dostępna).
Tooltipy z opisami: Wyświetlanie krótkich opisów wydarzeń po najechaniu na nie w widoku kalendarza.
Strona główna: Wybór pomiędzy widokiem kalendarza a kafelkowym oraz podgląd nadchodzących wydarzeń.
Wymagania
Zależności wymienione w pliku requirements.txt

Instalacja
Sklonuj repozytorium:
git clone https://github.com/jkoltonowski/event-calendar-django.git
cd event-calendar-django

Utwórz wirtualne środowisko (opcjonalnie, ale zalecane):
python -m venv venv
.\venv\Scripts\activate <- Na Windows:

source venv/bin/activate <- Na macOS/Linux:

Zainstaluj wymagane zależności:
pip install -r requirements.txt

Uruchom serwer deweloperski:
python manage.py runserver
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/

Jak korzystać
Po uruchomieniu serwera, przejdź pod adres http://127.0.0.1:8000/, gdzie zobaczysz stronę główną aplikacji. Możesz wybrać widok kalendarza lub kafelkowy, przeglądać wydarzenia, filtrować je po tagach oraz zobaczyć szczegóły wydarzeń.

Aby dodać nowe wydarzenia, będziesz musiał to zrobić poprzez zewnętrzne API, z którego wydarzenia są pobierane.
