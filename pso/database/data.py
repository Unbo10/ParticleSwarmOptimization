

import numpy as np
import pandas as pd

class Data:
    def __init__(self) -> None:
        self.__particle_history: list[pd.DataFrame] = []
        self.__gbest_history: list[list[int]] = []
        self.__number_of_optimizations: int = 0
    
    def append_optimization(self, optimization_df: pd.DataFrame) -> None:
        self.__particle_history.append(optimization_df)
        # ? .at[iter]?
    
    def append_gbest_indexes(self, optimization_gbest_indexes: list[int]) -> None:
        self.__gbest_history.append(optimization_gbest_indexes)
        self.__number_of_optimizations += 1

    def create_spreadsheet(self) -> None:
        writer = pd.ExcelWriter('optimization_results.xlsx', engine='xlsxwriter')
        
        for i in range(self.__number_of_optimizations):
            self.__particle_history[i].to_excel(excel_writer=writer, sheet_name=f'Optimization {i}')
        writer.close()

    def print_optimization(self, optimization_index: int) -> None:
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('max_colwidth', None)
        pd.set_option('display.max_rows', None)
        print(self.__particle_history[optimization_index])

    # * Getters

    def get_particle_history(self) -> list[pd.DataFrame]:
        return self.__particle_history