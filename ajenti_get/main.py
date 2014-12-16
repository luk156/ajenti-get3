from ajenti.api import *
from ajenti.ui.binder import Binder
from ajenti.plugins.main.api import SectionPlugin
from ajenti.ui import on
import os

class GetIstance (object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{%s}' % (self.name.replace('_settings.py',''))

@plugin
class TestPlugin (SectionPlugin):
    def init(self):
        self.title = 'GeT3'  # those are not class attributes and can be only set in or after init()
        self.icon = 'question'
        self.category = 'Software'

        """
        UI Inflater searches for the named XML layout and inflates it into
        an UIElement object tree
        """
        settings = filter(lambda x: '_settings.py' in x , os.listdir("/home/django/get3/GeT3/settings/"))
        self.instances = [GetIstance(a) for a in settings]

        self.append(self.ui.inflate('ajenti_get:main'))
        self.binder = Binder(self, self.find('bindroot'))

        self.refresh()
        self.binder.populate()

    def refresh(self):
        """
        Changing element properties automatically results
        in an UI updated being issued to client
        """
        #self.find('counter-label').text = 'Counter: %i' % self.counter

    #@on('increment-button', 'click')
    #def on_button(self):
        """
        This method is called every time a child element
        with ID 'increment-button' fires a 'click' event
        """
        #self.counter += 1
        #self.refresh()