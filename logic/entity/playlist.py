class Playlist:

    def __init__(self, name, description, public=False):
        self.name = name
        self.description = description
        self.public = public

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "public": self.public
        }
