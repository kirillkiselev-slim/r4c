class RobotSerializer:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        valid_models = ["R2", "13", "X5"]
        valid_versions = ["D2", "XS", "LT", "A1", "C8"]

        model = self.data.get('model', '').upper()
        version = self.data.get('version', '').upper()

        if model not in valid_models:
            self.errors = {'model': 'Not a valid model'}
            return False

        if version not in valid_versions:
            self.errors = {'version': 'Not a valid version'}
            return False

        return True