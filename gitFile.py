import ast
from datetime import datetime

class File:
    status = True
    message = ''
    keys = []
    inputs = []
    path = ''

    def __init__(self, repo, path = ''):
        try:
            self.repo = repo
            self.status = True
            if path != '':
                file_content = repo.get_contents(path)
                data = ast.literal_eval(file_content.decoded_content.decode().replace("'", '"'))
                self.family = data['family']
                self.keys = data['keys']
                self.code = data['code']
                self.inputs = data['inputs']
                self.returnValue = data['returnValue']
                self.description = data['description']
                self.date = data['date']
                self.lastEdit = data['lastEdit']
                self.path = path
        except:
            self.status = False
            self.message = 'unknown error'

    def __str__(self):
        return f"""
                'family': {self.family},
                'keys': {self.keys},
                'code': {self.code},
                'inputs': {self.inputs},
                'returnValue': {self.returnValue},
                'description': {self.description},
            """

    def add(self, commit_message="Add new file"):
        try:
            if self.keys == [] or self.path == '':
                self.status = False
                self.message = 'insufficient data\npath: ' + self.path + '\nkeys: ' + ','.join(self.keys)
                return
            self.repo.create_file(self.path, commit_message, str({
                'family': self.family,
                'keys': self.keys,
                'code': self.code,
                'inputs': self.inputs,
                'returnValue': self.returnValue,
                'description': self.description,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'lastEdit': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }))
            self.status = True
        except:
            self.status = False
            self.message = 'unknown error'

    def delete(self, commit_message="Delete file"):
        try:
            file_content = self.repo.get_contents(self.path)
            self.repo.delete_file(file_content.path, commit_message, file_content.sha)
            del self
        except:
            self.status = False
            self.message = 'unknown error'

    def edit(self, commit_message="Update file"):
        try:
            file_content = self.repo.get_contents(self.path)
            self.repo.update_file(self.path, commit_message, str({
                'family': self.family,
                'keys': self.keys,
                'code': self.code,
                'inputs': self.inputs,
                'returnValue': self.returnValue,
                'description': self.description,
                'date': self.date,
                'lastEdit': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }), file_content.sha)
            self.status = True
        except:
            self.status = False
            self.message = 'unknown error'