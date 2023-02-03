import requests
import pandas as pd


class DBI:
    """ class for all api interactions for streamlit app"""

    def __init__(self, url: str):
        self.url = url
        self.header = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

    def update_bug(self, id, title, desc, is_open, owner):
        """ update a bug """
        json_data = {
            'title': str(title),
            'description': str(desc),
            'is_open': str(is_open),
            'owner_id': str(owner)
        }

        requests.patch(
            f'{self.url}/bugs/update/{id}',
            headers=self.header,
            json=json_data,
            timeout=5
        )

    def create_bug(self, title, desc, is_open, owner):
        """ create a bug """
        json_data = {
            'title': str(title),
            'description': str(desc),
            'is_open': str(is_open),
            'owner_id': str(owner)
        }

        requests.post(
            f'{self.url}/bugs/create/{owner}',
            headers=self.header,
            json=json_data,
            timeout=5
        )

    def create_user(self, first, last):
        """ create a user """
        json_data = {
            'id': 0,
            'first': str(first),
            'last': str(last)
        }

        requests.post(
            f'{self.url}/users/create/',
            headers=self.header,
            json=json_data,
            timeout=5
        )

    def update_user(self, id, first, last):
        """ update a users details """
        json_data = {
            'first': str(first),
            'last': str(last)
        }

        requests.patch(
            f'{self.url}/users/update/{id}',
            headers=self.header,
            json=json_data,
            timeout=5
        )

    def get_bugs(self):
        """ fetch details of all bugs """
        bugs = requests.get(f'{self.url}/bugs/?skip=0&limit=100', timeout=5)
        bugs = pd.json_normalize(bugs.json())
        bugs = bugs.rename({
            'id': 'Bug ID',
            'title': 'Title',
            'description': 'Description',
            'is_open': 'Is open?',
            'owner_id': 'Assigned to',
            'time_created': 'Opened'
        }, axis=1)
        return bugs

    def get_users(self):
        """ fetch details of all users """
        users = requests.get(f'{self.url}/users/?skip=0&limit=100', timeout=5)
        users = pd.json_normalize(users.json())
        users = users.rename({
            'id': 'User ID',
            'first': 'First Name',
            'last': 'Last Name'
        }, axis=1)
        return users
