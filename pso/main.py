
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
        self.__history: Data = Data(excel_file_name=self.get_last_xslx_file())
        self.optimizations: list[Optimization] = []
        self.gui: GUI = GUI(program_version=self.get_version())
    
    def initialize_optimization(self) -> None:
        self.__optimizations.append(Optimization())

    def run_optimization(self) -> None:
        pass

    def get_version(self) -> str:
        # Define the file path
        conf_file_path = '../pyproject.toml'

        # Load the .toml file
        data = toml.load(conf_file_path)

        # Get the version
        version = data.get('tool', {}).get('poetry', {}).get('version', 'Version not found')

        return version
    
    def get_last_xslx_file (self) -> str:
        path: str = 'database'
        files: list[str] = os.listdir(path)
        last_session: int = 0
        # * Refers to the number of the session to be looked at in the
        # * for cycle
        current_session: int = 0
        xlsx_files: list[str] = [f for f in files if f.endswith('.xlsx')]
        if len(xlsx_files) == 0:
            return "session1_results"
        else:
            for i in range(len(xlsx_files)):
                current_session = int(re.findall(r'\d+', xlsx_files[i])[0])
                if current_session > last_session:
                    last_session = current_session
            return f'session{last_session}_results'
        # ? Maybe raise an exception here?

if __name__ == "__main__":
    try:
        main = Main()
        print(main.get_version())
        main.user_interface()
    except KeyboardInterrupt:
        print("Exiting the program.")
        exit()

