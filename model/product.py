import sys
from model.site import Site

class Product:

    def __init__(self, name, spreadsheet_id, sites_list: Site):
        self._name = name
        self._spreadsheet_id = spreadsheet_id
        self._sites_list = sites_list
    

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
    def spreadsheet_id(self, value):
        self._spreadsheet_id = value

    @property
    def sites_list(self):
        return self._sites_list

    @sites_list.setter
    def sites_list(self, value):
        self._sites_list = value