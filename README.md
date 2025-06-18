# Carzilla - find your dream car

## Autorzy:
Jakub Bagiński, Michał Bloch, Bartosz Mączka, Aleksander Paliwoda, Marta Piraszewska

### O czym jest projekt?
Projekt jest stworzony do obsługi sieci dealerów samochodowych. Strona ma spełniać funkcjonalność prowadzenia działalności (faktury, pracownicy itd.), wyszukiwania danych (samochodów), tworzenia statystyk (ilość faktur danego pracownika, zarobki, pracownik miesiąca itp.)

### Założenia
 - domyślnie strona jest dla pracowników firmy
 - bez logowania jest dostępna wyszukiwarka samochodów
 - każdy pracownik może wystawiać faktury
 - menadżerownie mogą dodatkowo zwalniać i zatrudniać pracowników
 - po zalogowaniu pojawiają się opcje w kafelkach
 - po wybraniu konkretnej tabeli pojawiają się opcje co można zrobić (dodaj, wyszukaj, edytuj, usuń (tylko dla menagera))

### Uruchomienie
Aplikacja wykorzystuje Docker i Docker Compose do zarządzania środowiskiem uruchomieniowym, co pozwala na łatwe i szybkie uruchomienie całości bez konieczności ręcznej konfiguracji zależności.

Aby uruchomić aplikację, wystarczy użyć poniższego polecenia:
```
docker-compose up
```
Polecenie to zbuduje obrazy (jeśli to konieczne) i uruchomi wszystkie kontenery zdefiniowane w pliku docker-compose.yml, a logi kontenerów będą wyświetlane na bieżąco w terminalu.

Jeśli chcesz uruchomić aplikację w tle (tzw. detached mode), dodaj flagę `-d`:
```
docker-compose up -d
```
Dzięki wykorzystaniu konteneryzacji, aplikacja działa w izolowanym i spójnym środowisku, niezależnie od konfiguracji lokalnego systemu operacyjnego.

### Dokumentacja
[Aplikacja Webowa](docs/Działanie_aplikacji.pdf)

[Serwer Aplikacji](docs/dokumentacja_backend.md)

[Baza Danych](docs/dokumentacja_baza_danych.md)

[Testowanie](docs/testy.pdf)

### Użyte Technologie
Dev stack użyty do implementacji aplikacji, który zapewnia modularność, skalowalność i łatwość wdrażania:

- **Docker & Docker Compose** – do konteneryzacji i zarządzania środowiskiem aplikacji

- **Frontend: React** – biblioteka JavaScript do budowy interfejsu użytkownika

- **Backend: Python Flask** – lekki framework webowy do budowy REST API

- **Baza danych: PostgreSQL** – system baz danych SQL

### Podział prac
- Jakub Bagiński -> obsługa backendu, integracja z bazą danych
- Michał Bloch -> troubleshooting, setup, logowanie i zabezpieczenia strony
- Bartosz Mączka -> integracja frontendu z backendem
- Aleksander Paliwoda -> obsługa frontend, intuicyjna aplikacja, łatwość obsługi
- Marta Piraszewska -> obsługa bazy danych, triggery, funkcje