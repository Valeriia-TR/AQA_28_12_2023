import sqlite3
import json
import requests


class APIAdapter:
    def __init__(self, db_path):
        self.db_path = db_path
        self.base_url = "https://api.restful-api.dev"
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS objects (
                id TEXT PRIMARY KEY,
                name TEXT,
                data TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_object_into_db(self, obj):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO objects (id, name, data)
                VALUES (?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                name = excluded.name,
                data = excluded.data;
            ''', (obj['id'], obj['name'], json.dumps(obj.get('data', {}))))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    def update_object_in_db(self, obj_id, obj):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE objects SET name = ?, data = ? WHERE id = ?
        ''', (obj['name'], json.dumps(obj.get('data', {})), obj_id))
        conn.commit()
        conn.close()

    def get_all_objects_from_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, data FROM objects')
        all_objects = [{'id': row[0], 'name': row[1], 'data': json.loads(row[2])} for row in cursor.fetchall()]
        conn.close()
        return all_objects

    def synchronize_with_api(self):
        response = requests.get(f'{self.base_url}/objects')
        if response.status_code == 200:
            current_api_ids = {obj['id'] for obj in response.json()}
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM objects')
            all_db_ids = {id[0] for id in cursor.fetchall()}
            ids_to_delete = all_db_ids - current_api_ids
            for obj_id in ids_to_delete:
                cursor.execute('DELETE FROM objects WHERE id = ?', (obj_id,))
            for obj in response.json():
                cursor.execute('''
                    INSERT INTO objects (id, name, data) VALUES (?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET name = excluded.name, data = excluded.data;
                ''', (obj['id'], obj['name'], json.dumps(obj['data'])))
            conn.commit()
            conn.close()

    def get_object_by_id(self, obj_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, data FROM objects WHERE id = ?', (obj_id,))
        obj = cursor.fetchone()
        conn.close()
        return {'id': obj[0], 'name': obj[1], 'data': json.loads(obj[2])} if obj else None

    def delete_object_from_db(self, obj_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM objects WHERE id = ?', (obj_id,))
        conn.commit()
        conn.close()

    def update_object_by_id(self, obj_id, update_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE objects SET name = ?, data = ? WHERE id = ?
        ''', (update_data['name'], json.dumps(update_data.get('data', {})), obj_id))
        conn.commit()
        conn.close()
