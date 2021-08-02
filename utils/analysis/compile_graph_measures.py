import numpy as np
import pandas as pd

class CompileGraphMeasures:
    def __init__(self, *columns):
        self.columns = columns[0]

        
        self.dataframe = self.init_compiled_dataframe()
        

    def init_compiled_dataframe(self):

        init_dataframe = pd.DataFrame(data = [], columns = self.columns)

        return init_dataframe
        
    def append_results(self, new_dataframe, **kwargs):
        
         self.dataframe = self.dataframe.append(new_dataframe)
         self.dataframe.reset_index(drop = True, inplace = True)

        


