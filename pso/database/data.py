
import os

import numpy as np
import openpyxl as px
import pandas as pd

class Data:
    def __init__(self, excel_file_name: str) -> None:
        self.__particle_history: list[pd.DataFrame] = []
        self.__gbest_history: list[list[int]] = []
        self.__number_of_optimizations: int = 0
        self.__xlsx_name: str = excel_file_name # * Without the extension and directory
        self.__xlsx_path: str = f"database/{self.__xlsx_name}.xlsx"
    
    def append_optimization(self, optimization_df: pd.DataFrame) -> None:
        # TODO: Might need to do a sepparate process for the first optimization, since it will be overwritten and not appended.
        
        if self.__xlsx_name not in os.listdir():
            self.create_spreadsheet()
        
        workbook: px.Workbook = px.load_workbook(self.__xlsx_path)
        sheet_number: int = len(workbook.sheetnames)
        sheet_name: str = f"Optimization {sheet_number}"
        if sheet_number not in workbook.sheetnames:
            workbook.create_sheet(title=f"Optimization {sheet_number}")
        else:
            pass
        writer: pd.ExcelWriter = pd.ExcelWriter(engine="openpyxl",
            mode="w", path=self.__xlsx_path)
        
        optimization_df.to_excel(excel_writer=writer,
            sheet_name= sheet_name, index=False)
        writer.close()

        self.__particle_history.append(optimization_df)
    
    def append_gbest_indexes(self, optimization_gbest_indexes: list[int]) -> None:
        self.__gbest_history.append(optimization_gbest_indexes)
        self.__number_of_optimizations += 1

    def create_spreadsheet(self) -> None:
        try:
            # Initializing file as an Excel one
            empty_df: pd.DataFrame = pd.DataFrame()
            with pd.ExcelWriter(self.__xlsx_path, engine="openpyxl") as writer:
                empty_df.to_excel(excel_writer=writer)
                writer.book.active.title = "Optimization 1"
                writer.book.save(self.__xlsx_path)
        except FileExistsError as e:
            print(e)
            print("No need to create it again (should happen only in testing).")

    def print_optimization(self, optimization_index: int) -> None:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.expand_frame_repr", False)
        pd.set_option("max_colwidth", None)
        pd.set_option("display.max_rows", None)
        print(self.__particle_history[optimization_index])

    # * Getters

    def get_particle_history(self) -> list[pd.DataFrame]:
        return self.__particle_history