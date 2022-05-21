from datetime import datetime


#Classe para converter formato datetime em string e vice-versa
class ConversaoDatas:
    def __init__(self):
        self.formato_data = '%Y/%m/%d %H:%M:%S'
        self.formato_string = '%d/%m/%Y às %H:%M:%S'

    def paraString(self, date):
        return datetime.strftime(date, self.formato_string)

    def paraDatetime(self, string):
        return datetime.strptime(string, self.formato_data)

