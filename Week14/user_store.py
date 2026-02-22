import json
import os


class UserStore:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        """
        Returns a list of user dictionaries.
        Handles missing file gracefully.
        """
        users = []

        if not os.path.exists(self.file_path):
            return users

        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    users.append(json.loads(line))
        return users

    def save(self, users):
        """
        Writes users as JSON lines (one JSON object per line).
        Overwrites the file with the full list.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            for user in users:
                f.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id: int):
        """
        Returns the user dict with matching id or None.
        """
        users = self.load()
        for user in users:
            if user.get("id") == user_id:
                return user
        return None

    def update_user(self, user_id: int, updated_data: dict):
        """
        Updates a user by id with fields from updated_data.
        Returns True if updated, False if not found.
        """
        users = self.load()

        for user in users:
            if user.get("id") == user_id:
                user.update(updated_data)
                self.save(users)
                return True

        return False

    def delete_user(self, user_id: int):
        """
        Deletes a user by id.
        Returns True if deleted, False if not found.
        """
        users = self.load()

        for i, user in enumerate(users):
            if user.get("id") == user_id:
                users.pop(i)
                self.save(users)
                return True

        return False