
import os

import numpy as np
import openpyxl as px
import openpyxl.styles as px_styles
import openpyxl.worksheet.worksheet as px_worksheet
import pandas as pd

class Data:
    def __init__(self, excel_file_name: str) -> None:
        self.__particle_history: list[pd.DataFrame] = []
        self.__gbest_history: list[list[int]] = []
        self.__number_of_optimizations: int = 0
        self.__xlsx_name: str = excel_file_name # * Without the extension and directory
        self.__xlsx_path: str = f"database/{self.__xlsx_name}.xlsx" # * It is determined if it exists in Main
    
    def append_optimization(self, optimization_df: pd.DataFrame) -> None:
        # TODO: Style the spreadsheet (colors to the headers gbests, and maybe iterations) and try making two optimizations in the same file and having two files
        
        if self.__xlsx_name not in os.listdir():
            self.create_spreadsheet()
        
        workbook: px.Workbook = px.load_workbook(self.__xlsx_path)
        sheet_number: int = len(workbook.sheetnames)
        sheet_name: str = f"Optimization {sheet_number}"
        if sheet_name not in workbook.sheetnames:
            print("AAA")
            workbook.create_sheet(title=f"Optimization {sheet_number}")
        else:
            pass

        sheet: px_worksheet.Worksheet = workbook[sheet_name]
        sheet["B2"] = "Iteration"
        sheet["C2"] = "Particle"
        sheet["D2"] = "Heuristic coordinates"
        sheet["E2"] = "Position coordinates"
        sheet["F2"] = "Velocity coordinates"
        sheet["G2"] = "Best personal position coordinates"
        for column in range(2, 8):
            sheet.cell(row=2, column=column).alignment = px_styles.Alignment(horizontal="center", vertical="center", wrap_text=True)
            sheet.row_dimensions[2].height = 40
        optimization_records: tuple[tuple] = optimization_df.to_records(index=False)
        column_width: int = 6*(len(optimization_records[0][0]) + 1)
        for column in ["C", "D", "E", "F", "G"]:
            sheet.column_dimensions[column].width = column_width
        number_of_iterations: int = optimization_df["Heuristic"].isna().sum()
        sheet.column_dimensions["B"].width = 10
        number_of_particles: int = 0
        while optimization_records[number_of_particles][0] is not np.NaN:
            number_of_particles += 1
        particle_index: int = 1
        for row in range(optimization_df.shape[0]):
            if optimization_records[row][0] is not np.NaN:
                cell = sheet.cell(row=row + 3, column=3)
                cell.value = particle_index
                cell.alignment = px_styles.Alignment(horizontal="center",
                    vertical="center")
                if particle_index == number_of_particles:
                    particle_index = 1
                else:
                    particle_index += 1
            else:
                pass
        starting_row: int = 3
        ending_row: str = number_of_particles + 2
        iteration_number: int = 0
        while starting_row < optimization_df.shape[0]:
            sheet.merge_cells(f"B{starting_row}:B{ending_row}")
            sheet[f"B{starting_row}"] = iteration_number
            iteration_number += 1
            sheet[f"B{starting_row}"].alignment = px_styles.Alignment(horizontal="center", vertical="center")
            starting_row = ending_row + 2
            ending_row = starting_row + number_of_particles - 1

        # * Appending the arrays to the corresponding spreadsheet
        for row in range(optimization_df.shape[0]):
            for column in range(optimization_df.shape[1]):
                value = optimization_records[row][column]
                if isinstance(value, np.ndarray):
                    # * To avoid iterating through NaNs
                    value: str = ', '.join(map(str, value))
                    # * Makes each value of the tuple of floats a string (using map) and then joins them with a comma in a single string
                cell = sheet.cell(row=row + 3, column=column + 4)
                cell.value = value
                cell.alignment = px_styles.Alignment(horizontal="center",
                    vertical="center", wrap_text=True)
                # * Rows and columns start at 1
        for row in sheet.iter_rows():
            for cell in row:
                cell.font = px_styles.Font(name="FreeMono", size=11, bold=True)

        workbook.save(self.__xlsx_path)
        self.__particle_history.append(optimization_df)
    
    def append_gbest_indexes(self, optimization_gbest_indexes: list[int]) -> None:
        self.__gbest_history.append(optimization_gbest_indexes)
        self.__number_of_optimizations += 1

    def create_spreadsheet(self) -> None:
        try:
            # * Initializing file as an Excel one
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