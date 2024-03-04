

def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')
    return inner


@singleton
class UniqueConnection:
    def __init__(self, creds):
        self.creds=creds


first_connection = UniqueConnection('first credentials')
second_connection = UniqueConnection('second credentials')
print(second_connection.creds)