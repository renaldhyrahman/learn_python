import json
import os


class Memory:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self):
        if not os.path.exists(self.file_name):
            return []
        try:
            with open(self.file_name, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # File exists but empty or corrupted,
            # treat  it as empty list
            return []

    def save(self, data: list):
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    # Unused, archived
    # def update(self, data: dict | list):
    #     if not isinstance(data, (dict, list)):
    #         raise TypeError("Memory.update() only accepts dict or list")
    #     saved_data = self.read()
    #     if isinstance(data, dict):
    #         saved_data.append(data)
    #     else:
    #         saved_data.extend(data)
    #     self.save(saved_data)
