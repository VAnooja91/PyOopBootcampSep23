from abc import ABC, abstractmethod

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