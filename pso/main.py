
# * This class is supposed to serve as the interaction with all the other
# * classes. It will contain the Data object that will store the results of
# * any optimization done while the program is running.

import os
import re

import toml

from pso.database.data import Data
from pso.graphics.gui import GUI
from pso.optimization import Optimization
class Main:
    def __init__(self) -> None:
        self.optimization_history: list[Optimization] = []
        self.database: Data = Data(excel_file_name=self.determine_xlsx_name())
        print("Data object created")
        self.gui: GUI = GUI(program_version=self.get_version(), data=self.database, optimization_history=self.optimization_history)
    
    def determine_xlsx_name(self) -> str:
        try:
            session_number = len(os.listdir(path="database/optimization_results")) + 1
            if session_number == 0:
                raise OSError
        except OSError:
            # * In case the directory does not exist or it is empty,
            # * the session is going to be the first one.
            return "session1_results"
        else:
            return f"session{session_number}_results"

    def initialize_optimization(self) -> None:
        self.__optimizations.append(Optimization(data=self.__history))

    def run_optimization(self) -> None:
        pass

    def get_version(self) -> str:
        conf_file_path = '../pyproject.toml'
        data = toml.load(conf_file_path)
        version = data.get('tool', {}).get('poetry', {}).get('version', 'Version not found')
        return version

def run():
    main = Main()
    main.gui.run()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print()
        print("Exiting the program.")
        exit()

