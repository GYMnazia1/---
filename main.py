class TLogElement:
    def __init__( self ):
        self.__in1 = False
        self.__in2 = False
        self._res = False
    def __setIn1 ( self, newIn1 ):
        self.__in1 = newIn1
        self.calc()
    def __setIn2 ( self, newIn2 ):
        self.__in2 = newIn2
        self.calc()    
    In1 = property (lambda x: x.__in1, __setIn1)
    In2 = property (lambda x: x.__in2, __setIn2)
    Res = property (lambda x: x._res )
