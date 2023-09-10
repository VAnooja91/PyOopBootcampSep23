from abc import ABC, abstractmethod

def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    else:
        raise FormateError(f"unknown formatter {name}")
    return formatter

class FormateError(Exception):
    pass

#class TableFormatter:
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
            Emit the table headings
        '''
        #raise NotImplementedError()
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
            Emit a single row of table data
        '''
        #raise NotImplementedError()
        pass

class TextTableFormatter(TableFormatter):    
    ''' 
        Emit a table in plain-text format
    '''
    def headings(self, headers):
        ''' 
            Emit heading with a dashed line
        '''
        for hdr in headers:
            print(f'{hdr:>10s}', end=' ')
        else:
            print()
            print(('-' * 10 + ' ') * len(headers))    

    def row(self, rowdata):
        '''
            Emit a single row for plain-text format
        '''
        for field in rowdata:
            print(f'{field:>10s}', end=' ')
        else:
            print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self,rowdata):
        print(','.join(rowdata))
