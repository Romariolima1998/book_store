# Bookstore

Bookstore APP from Backend Python 

## Prerequisites

```
Python 3.5>
Docker && docker-compose

```

## Quickstart

1. Clone this project

   ```shell
   git clone 
https://github.com/Romariolima1998/book_store.git
   ```

2. Install dependencies:

   ```shell
   cd bookstore
   pip install -r requiriments.txt
   ```

3. Run local dev server:

   ```shell
    python manage.py migrate
    python manage.py runserver
   ```
   
4. Run docker dev server environment:

   ```shell
   docker-compose up -d --build 
   docker-compose exec web python manage.py migrate
   ```

5. Run tests inside of docker:

   ```shell
   docker-compose exec web python manage.py test
   ```



