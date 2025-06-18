
# Dokumentacja Endpointów Backendu

# Profiles API

## `/search` — Profile

**Metoda:** `GET`
**Zastosowanie:** Zwraca podsumowanie: liczba sprzedanych samochodów, suma zysków oraz liczba dealerów.

**Przykładowy JSON odpowiedzi:**
```json
{
  "carsSold": 120,
  "profit": 1450000.0,
  "carDealersAmount": 7
}
```
---
# Positions API

## `/positions/` — Lista Stanowisk

**Metoda:** `GET`
**Zastosowanie:** Zwraca wszystkie dostępne stanowiska pracowników.

**Przykładowy JSON odpowiedzi:**
```json
[
  {
    "Position_ID": 1,
    "Position_name": "Sales Manager"
  },
  {
    "Position_ID": 2,
    "Position_name": "Mechanic"
  }
]
```
---

# Invoices API

## `/invoices/search` — Lista Faktur

**Metoda:** `GET`
**Zastosowanie:** Zwraca listę faktur z przypisanymi pracownikami i datami.

**Przykładowy JSON odpowiedzi:**
```json
[
  {
    "Invoice_ID": 101,
    "Value": 25000.0,
    "Date": "2024-01-12",
    "Name": "Jan Kowalski"
  }
]
```

---

## `/invoices/add` — Dodaj Fakturę

**Metoda:** `POST`
**Zastosowanie:** Tworzy nową fakturę oraz powiązaną transakcję.

**Przykładowy JSON żądania:**
```json
{
  "employee": 3,
  "client": 10,
  "amount": 32000.0,
  "nip": "1234567890"
}
```

**Odpowiedź:**
```json
{
  "message": "Added Transaction + Invoice Succesfuly"
}
```
---

# Employees API

##  `/employee_of_month/search` — Pracownik Miesiąca

**Metoda:** `GET`
**Zastosowanie:** Zwraca pracownika z najwyższą sprzedażą w danym miesiącu i roku.

**Parametry wejściowe:**
Brak (aktualnie statycznie ustawione na `month=1`, `year=2024`)

**Przykładowy JSON odpowiedzi:**
```json
{
  "Employee_ID": 5,
  "Name": "Anna",
  "Surname": "Nowak",
  "Position": "Sales Manager",
  "Sales": 55000.0
}
```
**Możliwe odpowiedzi:**
- `200 OK` – znaleziono pracownika
- `204 No Content` – brak danych dla danego okresu
---

## `/employees/add` — Dodaj Pracownika

**Metoda:** `POST`
**Zastosowanie:** Tworzy nowego pracownika.

**Wymagane pola JSON:**
```json
{
  "Name": "Jan",
  "Surname": "Nowak",
  "Gender": "M",
  "Date_of_birth": "1990-01-01",
  "Employee_status_ID": 1,
  "Car_dealer_ID": 2
}
```

---

##  `/employees/update/<employee_id>` — Aktualizacja Pracownika

**Metoda:** `PUT`
**Zastosowanie:** Aktualizuje dane pracownika.

**Dopuszczalne pola do aktualizacji:**
- Name
- Surname
- Gender
- Salary
- Date_of_birth
- Phone_number
- Employee_status_ID
- Car_dealer_ID
- Login_credentials_ID

---

## `/employees/remove/<employee_id>` — Usuwanie (Dezaktywacja) Pracownika

**Metoda:** `DELETE`
**Zastosowanie:** Zmienia status pracownika na „nieaktywny”.

**Odpowiedzi:**
- `200 OK` – pracownik zdezaktywowany
- `404 Not Found` – brak pracownika

---

## `/employees/search` — Wyszukiwanie Pracowników

**Metoda:** `GET`
**Zastosowanie:** Wyszukuje aktywnych pracowników według różnych pól.

**Dostępne parametry wyszukiwania:**
- Employee_ID
- Name
- Surname
- Gender
- Salary
- Date_of_birth
- Phone_number
- Employee_status_id
- Car_dealer_id
- Login_credentials_id

---

## `/employee_status/` — Statusy Pracowników

**Metoda:** `GET`
**Zastosowanie:** Zwraca listę statusów pracowników.

**Przykładowy JSON odpowiedzi:**
```json
[
  {
    "Employee_status_ID": 1,
    "Status_name": "Active"
  },
  {
    "Employee_status_ID": 2,
    "Status_name": "Fired"
  }
]
```

# Clients API
---

## `/clients/add` — Dodaj Klienta

**Metoda:** `POST`
**Zastosowanie:** Tworzy nowego klienta.

**Wymagane pola JSON:**
```json
{
  "Name": "Katarzyna",
  "Surname": "Lis",
  "Gender": "F",
  "Mail": "k.lis@example.com",
  "Phone": "123456789"
}
```

---

## `/clients/search` — Wyszukiwanie Klientów

**Metoda:** `GET`
**Zastosowanie:** Wyszukuje klientów według podstawowych pól.

**Dostępne parametry:**
- Client_ID
- Name
- Surname
- Gender
- Mail
- Phone

---
# Cars API
## `/cars/add` — Dodaj Samochód

**Metoda:** `POST`
**Zastosowanie:** Dodaje nowy samochód do bazy.

**Wymagane pola JSON:**
```json
{
  "Brand": "Toyota",
  "Model": "Corolla",
  "Color": "Red",
  "Mileage": 50000,
  "Price": 60000,
  "Car_condition_ID": 1,
  "Car_dealer_ID": 2
}
```

---

## `/cars/remove/<car_id>` — Usuń Samochód

**Metoda:** `DELETE`
**Zastosowanie:** Usuwa samochód na podstawie ID.

---

## `/cars/update/<car_id>` — Aktualizacja Samochodu

**Metoda:** `PUT`
**Zastosowanie:** Aktualizuje dane pojazdu.

**Pola do aktualizacji:**
- Brand
- Model
- Color
- Mileage
- Price
- Car_condition_ID
- Car_dealer_ID

---

## `/cars/search` — Wyszukiwanie Samochodów

**Metoda:** `GET`
**Zastosowanie:** Wyszukuje samochody według wybranych parametrów.

**Dostępne parametry:**
- Car_ID
- Brand
- Model
- Color
- Mileage
- Price
- Car_condition_ID
- Car_dealer_ID

---

## `/car_dealers/` — Lista Dealerów

**Metoda:** `GET`
**Zastosowanie:** Zwraca wszystkich dealerów.

**Przykładowy JSON odpowiedzi:**
```json
[
  {
    "Car_dealer_ID": 1,
    "Name": "Auto Śląsk"
  }
]
```

---

## `/car_conditions/` — Lista Stanów Samochodów

**Metoda:** `GET`
**Zastosowanie:** Zwraca listę stanów technicznych samochodów.

**Przykładowy JSON odpowiedzi:**
```json
[
  {
    "Car_condition_ID": 1,
    "Condition": "New"
  },
  {
    "Car_condition_ID": 2,
    "Condition": "Used"
  }
]
```
---

# Auth API

## POST `/auth/login`

Autoryzacja użytkownika na podstawie podanych danych logowania.

**Request (JSON):**
```json
{
  "username": "login_użytkownika",
  "password": "hasło"
}
```

**Response (200):**
```json
{
  "message": "Logged in",
  "user": "Imię użytkownika"
}
```

**Response (401):**
```json
{
  "error": "Invalid credentials"
}
```

**Zastosowanie:**
Służy do logowania użytkownika na podstawie jego loginu i hasła. Po pomyślnej weryfikacji tworzy sesję użytkownika.

---

### GET `/auth/status`

Sprawdzenie statusu autoryzacji aktualnego użytkownika.

**Response (gdy zalogowany):**
```json
{
  "authenticated": true,
  "user": "Imię użytkownika"
}
```

**Response (gdy niezalogowany):**
```json
{
  "authenticated": false
}
```

**Zastosowanie:**
Pozwala frontendowi lub innym klientom API określić, czy użytkownik jest aktualnie zalogowany.

---

### POST `/auth/logout`

Wylogowuje aktualnie zalogowanego użytkownika.

**Response (200):**
```json
{
  "message": "Logged out"
}
```

**Wymagania:**
Użytkownik musi być zalogowany (`@login_required`).

**Zastosowanie:**
Zamknięcie sesji użytkownika — usuwa informacje o autoryzacji.
