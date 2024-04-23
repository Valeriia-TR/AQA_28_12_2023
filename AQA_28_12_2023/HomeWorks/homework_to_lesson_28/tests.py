from AQA_28_12_2023.HomeWorks.homework_to_lesson_28.api_adapter import APIAdapter
from AQA_28_12_2023.HomeWorks.homework_to_lesson_28.objects import Objects


adapter = APIAdapter('my_database.db')
objects_instance = Objects()
adapter.synchronize_with_api()
objects_from_db = adapter.get_all_objects_from_db()


def test_get_objects():
    objects_from_db = adapter.get_all_objects_from_db()
    print(objects_from_db)
    objects_api = objects_instance.get_all_objects()
    print(objects_api.json())
    assert objects_api.json() == objects_from_db


def test_create_object():
    new_object = objects_instance.create_object().json()
    adapter.insert_object_into_db(new_object)
    objects_from_db = adapter.get_all_objects_from_db()
    object_ids_from_db = [obj['id'] for obj in objects_from_db]
    assert new_object['id'] in object_ids_from_db


def test_update_object():
    updated_object = objects_instance.update_object()
    assert updated_object.status_code == 200
    updated_object_data = updated_object.json()
    assert 'updatedAt' in updated_object_data
    object_id = updated_object_data['id']
    adapter.insert_object_into_db(updated_object_data)
    object_from_db = adapter.get_object_by_id(object_id)
    print(f"Object from DB: {object_from_db}")
    print(f"Updated object from API: {updated_object_data}")
    assert object_from_db is not None, "Object not found in the database"
    assert object_from_db['name'] == updated_object_data['name'], "Object name was not updated in the database"


def test_delete_object():
    new_object_response = objects_instance.create_object()
    assert new_object_response.status_code == 200
    new_object_data = new_object_response.json()
    adapter.insert_object_into_db(new_object_data)
    object_id = new_object_data['id']
    object_from_db_before_delete = adapter.get_object_by_id(object_id)
    assert object_from_db_before_delete is not None, "Object should be in the database before deletion"
    delete_response = objects_instance.delete_object(object_id)
    assert delete_response.status_code == 200, "API should confirm deletion with a 200 status code"
    adapter.synchronize_with_api()
    object_from_db_after_delete = adapter.get_object_by_id(object_id)
    assert object_from_db_after_delete is None, "Object should not be in the database after deletion"
