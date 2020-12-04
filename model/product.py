class Product:

    def __init__(self, name, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    @property
    def name(self):
        return self._name


 @nome.setter
    def nome(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self._nome = value