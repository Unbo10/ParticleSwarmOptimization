
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
        self.history: Data = Data(excel_file_name=self.get_last_xslx_file())
        self.optimizations: list[Optimization] = []
        self.gui: GUI = GUI(program_version=self.get_version())

    def get_last_xlsx_file (self) -> str:
        path: str = 'database'
        files: list[str] = os.listdir(path)
        last_session: int = 0
        # * Refers to the number of the session to be looked at in the
        # * for cycle
        current_session: int = 0
        xlsx_files: list[str] = [f for f in files if f.startswith("session")]
        if len(xlsx_files) == 0:
            last_session = 1
        else:
            for i in range(len(xlsx_files)):
                current_session = int(re.findall(r'\d+', xlsx_files[i])[0])
                # * Current session will be the first (and only) sequence of numbers found in the i-th xlsx file name.
                if current_session > last_session:
                    last_session = current_session
            return f'session{last_session}_results'
        raise OSError("No excel files found.")

    def get_version(self) -> str:
        conf_file_path = '../pyproject.toml'
        data = toml.load(conf_file_path)
        version = data.get('tool', {}).get('poetry', {}).get('version', 'Version not found')

        return version

if __name__ == "__main__":
    try:
        main = Main()
        main.gui.run()
    except KeyboardInterrupt:
        print("Exiting the program.")
        exit()

