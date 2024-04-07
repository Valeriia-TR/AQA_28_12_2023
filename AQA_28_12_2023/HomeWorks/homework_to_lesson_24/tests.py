from AQA_28_12_2023.HomeWorks.homework_to_lesson_24.infrastructure import Book


def test_get_all_objects(objects):
    response = objects.get_all_objects()
    assert response.status_code == 200
    assert type(response.json()) is list

def test_get_objects_check_content(objects):
    response = objects.get_all_objects()
    assert len(response.json()) > 0
    assert 'id' in response.json()[0]


def test_get_objects_by_ids_check_content(objects):
    ids_to_test = [3, 5, 7]
    response = objects.get_objects_by_ids(ids_to_test)
    assert response.status_code == 200
    response_ids = [item['id'] for item in response.json()]
    for id in ids_to_test:
        assert str(id) in response_ids


def test_get_single_object(objects):
    object_id = 7
    response = objects.get_single_object(object_id)
    assert response.status_code == 200
    assert response.json()['id'] == str(object_id)


def test_create_object(objects):
    new_object = objects.create_object()
    print(new_object.json())
    assert new_object.status_code == 200
    assert new_object.json()['createdAt']


def test_update_object(objects):
    updated_object = objects.update_object()
    assert updated_object.status_code == 200
    assert updated_object.json()['updatedAt']
    print(updated_object.json())


def test_partial_update_object(objects):
    patched_object = objects.partial_update_object(objects.updated_name)
    print(patched_object.json())
    assert patched_object.status_code == 200
    assert patched_object.json()['name'] == objects.updated_name['name']


def test_delete_object(objects):
    deleted_object, deleted_object_id = objects.delete_object()
    assert deleted_object.status_code == 200
    assert deleted_object.json()['message'] == f"Object with id = {deleted_object_id} has been deleted."
    get_response = objects.get_single_object(deleted_object_id)
    assert get_response.status_code == 404


def test_create_book():
    book = Book(title="Test Book", author="Test Author", year=2021)
    assert book.id is not None
    assert book.created_time is not None
    assert book.delete_book()


def test_get_book_by_id():
    book = Book(title="Test Book", author="Test Author", year=2021)
    fetched_book = Book.get_book_by_id(book.id)
    assert fetched_book['name'] == "Test Book"
    assert book.delete_book()


def test_update_book():
    book = Book(title="Old Book", author="Old Author", year=2020)
    updated_info = book.update_book(new_title="New Book", new_author="New Author", new_year=2022)
    assert updated_info['name'] == "New Book"
    updated_book = Book.get_book_by_id(book.id)
    assert updated_book['data']['author'] == "New Author"
    assert book.delete_book()


def test_delete_book():
    book = Book(title="Book to Delete", author="Author", year=2021)
    delete_status = book.delete_book()
    assert delete_status
    response = Book.get_book_by_id(book.id)
    assert response == {}
