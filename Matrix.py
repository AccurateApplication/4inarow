import numpy


class Matrix:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.matrix = numpy.zeros(self.rows,self.columns)

