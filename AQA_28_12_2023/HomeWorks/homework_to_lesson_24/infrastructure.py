import requests
import json
import random


class Objects:
    def __init__(self):
        self.base_url = "https://api.restful-api.dev"
        self.headers = {'content-type': 'application/json'}
        self.default_object_data = {
            "name": "New object",
            "data": {
                "year": 2024,
                "price": 999
            }
        }
        self.default_object_update_data = {
            "name": "New object",
            "data": {
                "year": 2024,
                "price": 999,
                "updated data": "updated data"
            }
        }
        self.updated_name = {"name": "New name for new object"}



    def get_all_objects(self):
        return requests.get(f'{self.base_url}/objects')

    def get_objects_by_ids(self, ids):
        return requests.get(f'{self.base_url}/objects', params={'id': ids})

    def get_single_object(self, object_id):
        return requests.get(f'{self.base_url}/objects/{object_id}')

    def create_object(self):
        return requests.post(f'{self.base_url}/objects', headers=self.headers, data=json.dumps(self.default_object_data))

    def update_object(self):
        created_new_object = self.create_object()
        return requests.put(f'{self.base_url}/objects/{created_new_object.json()["id"]}',
                            headers=self.headers, data=json.dumps(self.default_object_update_data))

    def partial_update_object(self, data):
        created_new_object = self.create_object()
        return requests.patch(f'{self.base_url}/objects/{created_new_object.json()["id"]}',
                              headers=self.headers, data=json.dumps(data))

    def delete_object(self):
        created_new_object = self.create_object()
        object_id = created_new_object.json()["id"]
        return requests.delete(f'{self.base_url}/objects/{object_id}'), object_id


class Book:
    base_url = 'https://api.restful-api.dev/objects'

    def __init__(self, title=None, author=None, year=None):
        self.headers = {'Content-Type': 'application/json'}
        self.book_data = {
            'name': title if title else "Untitled",
            'data': {
                'author': author if author else "Unknown",
                'year': year if year else random.randint(1800, 2023)
            }
        }
        self.object_response = requests.post(url=self.base_url, headers=self.headers, data=json.dumps(self.book_data))
        if self.object_response.status_code == 200:
            self.id = self.object_response.json().get('id')
            self.created_time = self.object_response.json().get('createdAt')
        else:
            self.id = None
            self.created_time = None

    @classmethod
    def create_random_books(cls, count=5):
        books = []
        for _ in range(count):
            book = cls(
                title=f"Book {random.randint(1, 100)}",
                author=f"Author {random.randint(1, 100)}",
                year=random.randint(1800, 2023)
            )
            if book.id:
                books.append(book)
        return books

    @staticmethod
    def get_all_books():
        response = requests.get(Book.base_url)
        if response.status_code == 200:
            return response.json()
        return []

    @staticmethod
    def get_book_by_id(book_id):
        response = requests.get(f'{Book.base_url}/{book_id}')
        if response.status_code == 200:
            return response.json()
        return {}

    def update_book(self, new_title=None, new_author=None, new_year=None):
        updated_data = {
            'name': new_title if new_title else self.book_data['name'],
            'data': {
                'author': new_author if new_author else self.book_data['data']['author'],
                'year': new_year if new_year else self.book_data['data']['year']
            }
        }
        response = requests.put(url=f'{self.base_url}/{self.id}', headers=self.headers, data=json.dumps(updated_data))
        return response.json()

    def delete_book(self):
        if self.id:
            response = requests.delete(f'{self.base_url}/{self.id}')
            return response.status_code == 200
        return False