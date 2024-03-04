from lesson16.factory_example.drivers.base_browser import Browser


class FirefoxBrowser(Browser):
    _name = 'Firefox'
    def __init__(self):
        super().__init__()
