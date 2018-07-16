# app/models.py

# contains models for the app

import datetime

from flask_restful import Resource

class Entry(Resource):
    """Add new entry"""

    # constructor
    def __init__(self):
        # all entries placeholder
        self.entries = []

    def add_entry(self, title, description):
        """Adds new entries"""

        now = datetime.datetime.now()
        date_created = now.strftime("%Y-%m-%d %H:%M")
        single_entry_holder = dict()
        single_entry_holder['title'] = title
        single_entry_holder['description'] = description
        single_entry_holder['created'] = str(date_created)
        self.entries.append(single_entry_holder)

    def all_entries(self):
        """Return available entries"""

        return self.entries