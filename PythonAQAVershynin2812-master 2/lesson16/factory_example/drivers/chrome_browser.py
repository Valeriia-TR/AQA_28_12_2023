from lesson16.factory_example.drivers.base_browser import Browser


class ChromeBrowser(Browser):
    _name = 'Chrome'

    def __init__(self):
        super().__init__()
