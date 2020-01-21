from vortex.config import INSTANCE_DIRECTORY


class Core:

    def setup_instance(self, target_instance):
        pass

    def __init__(self, _instance):
        self.instance = _instance
        self.setup_instance(self.instance)

