import sys
class Product:

    def __init__(self, name, url, spreadsheet_id):
        self._name = name
        self._url = url
        self._spreadsheet_id = spreadsheet_id
    

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self._name = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def spreadsheet_id(self):
        return self._spreadsheet_id

    @spreadsheet_id.setter
    def spreadsheet_id(self):
        self._spreadsheet_id = value