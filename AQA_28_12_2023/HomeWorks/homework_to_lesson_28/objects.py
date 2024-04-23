import requests
import json


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
            "name": "Updated object name",
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

    def delete_object(self, object_id):
        return requests.delete(f'{self.base_url}/objects/{object_id}')

    def save_to_db(self, adapter):
        adapter.insert_object_into_db(self.default_object_data)
