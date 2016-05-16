

from pecan import hooks

class ConfigHook(hooks.PecanHook):

    @staticmethod
    def before(state):
        print '---------i am in the hook---------------'


class SecondHook(hooks.PecanHook):

    @staticmethod
    def before(state):
        print '---------i am in the second hook---------------'

    @staticmethod
    def after(state):
        print '---------i am in the second hook in after state---------------'

    @staticmethod
    def on_route(state):
        print '---------i am in the second hook in on-route state---------------'
