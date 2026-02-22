import sqlite3
from typing import List, Optional, Dict


class UserStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_db()

    def _connect(self):
        
        return sqlite3.connect(self.db_path, check_same_thread=False)

    #REQUIREMENTS: CONSTRCUTURE, INIT_DB, LOAD, SAVE, FIND_BY_ID

    #INIT_DB: CREATE TABLE IF IT DOESNT EXIST.
    def init_db(self):
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

    #LOAD: RETURN LIST OF USER DICTIONARIES FROM DATABASE
    def load(self) -> List[Dict]:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, name, age, created_at FROM users ORDER BY id")
            rows = cur.fetchall()
            return [
                {"id": r[0], "name": r[1], "age": r[2], "created_at": r[3]}
                for r in rows
            ]
        finally:
            conn.close()

    #SAVE: INSERTS OR UPDATES USERS IN THE DATABASE. USE SQL TRIPLE  QUOTES MULTI LINE.
    def save(self, users: List[Dict]):   
        conn = self._connect()
        try:
            cur = conn.cursor()
            for user in users:
                cur.execute(
                    """
                    INSERT INTO users (id, name, age, created_at)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        name = excluded.name,
                        age = excluded.age,
                        created_at = excluded.created_at
                    """,
                    (user["id"], user["name"], user["age"], user["created_at"]),
                )
            conn.commit()
        finally:
            conn.close()

    #FIND_BY_ID: RETURNS USER DICT OR NONE USING SQL QUERY
    def find_by_id(self, user_id: int) -> Optional[Dict]:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, name, age, created_at FROM users WHERE id = ?",
                (user_id,),
            )
            row = cur.fetchone()
            if row is None:
                return None
            return {"id": row[0], "name": row[1], "age": row[2], "created_at": row[3]}
        finally:
            conn.close()

    #REQUIREMENTS: UPDATE, DELETE

    #UPDATE_USER: USE SQL UPDATE STATEMENT. RETURN SUCCESS STATEMENT 
    def update_user(self, user_id: int, updated_data: Dict) -> bool:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET name = ?, age = ? WHERE id = ?",
                (updated_data["name"], updated_data["age"], user_id),
            )
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    #DELETE_USER: REMOVE A USER BY ID USING SQL DELETE STATEMENT, RETURN TRUE IF DELETED.
    def delete_user(self, user_id: int) -> bool:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()