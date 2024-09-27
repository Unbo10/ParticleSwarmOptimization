
# * This class is supposed to serve as the interaction with all the other
# * classes. It will contain the Data object that will store the results of
# * any optimization done while the program is running.

import os
import re

import toml

from psopackage.database.data import Data
from psopackage.graphics.gui import GUI
from psopackage.optimization import Optimization
class Main:
    def __init__(self) -> None:
        # * The history object is going to store the results of the optimization
        self.optimization_history: list[Optimization] = []
        # * The database object is going to store the results of the optimization
        self.database: Data = Data(excel_file_name=self.determine_xlsx_name())
        print("Data object created")
        # * The GUI object is going to be the main interaction with the user
        self.gui: GUI = GUI(program_version=self.get_version(), data=self.database, optimization_history=self.optimization_history)
    
    def determine_xlsx_name(self) -> str:
        try:
            # * Tries to find the number of sessions. If it fails, it will return session1_results
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
        # * Appends a new optimization object to the optimization history
        self.__optimizations.append(Optimization(data=self.__history))

    def run_optimization(self) -> None:
        pass

    def get_version(self) -> str:
        # * Gets the version from the pyproject.toml file
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

