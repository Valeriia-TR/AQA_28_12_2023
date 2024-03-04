from lesson16.factory_example.drivers.chrome_browser import ChromeBrowser
from lesson16.factory_example.drivers.firefox_browser import FirefoxBrowser


class BrowserFactory:
    def __init__(self):
        self.last_browser = None

    def get_browser(self, name):
        self.last_browser = name
        if name == 'Chrome':
            return ChromeBrowser()
        elif name == 'Firefox':
            return FirefoxBrowser()
        else:
            raise Exception('wrong browser dude')

browser_factory = BrowserFactory()
chrome1 = browser_factory.get_browser('Chrome')
chrome2 = browser_factory.get_browser('Chrome')
firefox = browser_factory.get_browser('Firefox')
print()