# blog# Mój pierwszy blog

To jest aplikacja blogowa napisana przy użyciu Flask. Umożliwia dodawanie, edytowanie i usuwanie wpisów oraz szkiców. Aplikacja posiada również mechanizm logowania i wylogowywania użytkowników.

## Wymagania

- Python 3.10 lub nowszy
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- python-dotenv

## Instalacja

1. Sklonuj to repozytorium:
    ```sh
    git clone <git@github.com:AntoniPomocka/blog.git>
    cd <NAZWA_REPOZYTORIUM>
    ```

2. Utwórz i aktywuj wirtualne środowisko:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:
    ```sh
    pip install -r requirements.txt
    ```

4. Utwórz plik `.env` w katalogu głównym projektu i dodaj w nim następujące zmienne:
    ```
    FLASK_APP=blog
    SECRET_KEY=twój-sekret-klucz
    SQLALCHEMY_DATABASE_URI=sqlite:///app.db
    ```

5. Zainicjuj bazę danych:
    ```sh
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    ```

6. Uruchom aplikację:
    ```sh
    flask run
    ```

Aplikacja powinna być dostępna pod adresem `http://127.0.0.1:5000`.

## Struktura projektu

- `blog/` - główny katalog aplikacji
  - `templates/` - szablony HTML
  - `__init__.py` - plik inicjalizujący aplikację Flask
  - `routes.py` - definicje tras/widoków
  - `models.py` - modele bazy danych SQLAlchemy
  - `forms.py` - definicje formularzy Flask-WTF
- `migrations/` - migracje bazy danych
- `README.md` - ten plik
- `requirements.txt` - lista zależności

## Użycie

### Dodawanie nowego wpisu

Aby dodać nowy wpis, zaloguj się i kliknij na przycisk "Nowy wpis" na stronie głównej. Wypełnij formularz i kliknij przycisk "Dodaj".

### Edytowanie wpisu

Aby edytować istniejący wpis, kliknij na jego tytuł na stronie głównej lub w szkicach, a następnie kliknij "Edytuj". Wprowadź zmiany i kliknij "Zaktualizuj".

### Usuwanie wpisu

Aby usunąć wpis, kliknij na jego tytuł, a następnie kliknij przycisk "Usuń". Potwierdź operację w wyskakującym okienku.

