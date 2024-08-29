
# * This class is supposed to serve as the interaction with all the other
# * classes. It will contain the Data object that will store the results of
# * any optimization done while the program is running.

import os

from pso.database.data import Data
from pso.optimization import Optimization
class Main:
    def __init__(self) -> None:
        self.__history = Data(excel_file_name=self.determine_xlsx_name())
        self.__optimizations: list[Optimization] = []
    
    def determine_xlsx_name(self) -> str:
        try:
            session_number = len(os.listdir(path="database/optimization_results"))
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

if __name__ == "__main__":
    try:
        main = Main()
        print(main.determine_xlsx_name())
    except KeyboardInterrupt:
        print("Exiting the program.")
        exit()

