from datetime import datetime

class Member:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._join_date = datetime.now().strftime("%Y-%m-%d")  
    
    # Getter for name
    @property
    def name(self):
        return self._name

    # Getter for email
    @property
    def email(self):
        return self._email

    # Getter for join date
    @property
    def join_date(self):
        return self._join_date

    # Add new member to the database
    def create(self, db):
        db.cursor.execute('''
        INSERT INTO members (name, email, join_date)
        VALUES (?, ?, ?)''', (self.name, self.email, self.join_date))
        db.connection.commit()

    # Check if a member with the given ID exists in the database
    @staticmethod
    def exists(db, member_id):
        db.cursor.execute("SELECT id FROM members WHERE id = ?", (member_id,))
        return db.cursor.fetchone() is not None
