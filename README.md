# Szkoła w Chmurze - zadanie rekrutacyjne

## Instrukcja uruchomienia:
1. Instalacja potrzebnych bibliotek:
    ```
    pip install -r requirements.txt
    ```
2. Uruchomienie migracji (na potrzeby tego zadania wystarczy baza SQLite):
    ```
    python manage.py migrate
    ```
3. Stworzenie super usera (aby ewentualnie móc podejrzeć zmiany w adminie):
    ```
    python manage.py createsuperuser
    ```
4. Uruchomienie serwera:
    ```
    python manage.py runserver
    ```
   
    Pod adresem http://127.0.0.1:8000/swagger/ znajduje się specyfikacja OpenApi

5. Testowanie:
    ```
    python manage.py test
    ```
   