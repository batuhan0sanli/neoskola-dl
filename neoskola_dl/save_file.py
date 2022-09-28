import os


class SaveFile:
    def __init__(self, path, content):
        self.path = path
        self.content = content
        self._make_dir()

    def _make_dir(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def save(self):
        with open(self.path, 'w') as f:
            f.write(self.content)
