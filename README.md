<h1 align="center">The Inheritance</h1>



## Project explanation:
To know and understand better the PSO algorithm, we encourage you to check the Wiki of this project:
- ![Wiki](https://github.com/Unbo10/ParticleSwarmOptimization/wiki/PSO's-heuristic)

Once you are familiarized with it, we can proceed. We chose to work on this problem because it was a great way to apply all the concepts that we learned in class, to learn how to use external libraries to make a graphic interface or work with a database and finally, because it was a challenge. 

The PSO algorithm consists of a set of Particles that "explore" the function, with the purpose of finding it's minimum. That's why the implementation that we made consists of a ```Vector``` class, that is the class from wich ```Position```, ```Heuristic``` and ```Velocity``` inherit. Then, we define the ```Particle``` class, that consists of the three previous classes and has methods such as ```initialize_randomly``` or ```_update_velocity```, that allows us to control the particles over the domain of the function. Finally, we have the ```ParticleSwarm``` class, which is the set of all the particles that we want to create. This is the abstraction of the project that enables us to solve the problem, with the algorithm. The steps to follow are detailed in the Wiki.


## How to run the project using a virtual environment:
First of all, what is a virtual envoronment? A virtual envirnment is a "separate folder" that creates an independent set of installed packages. This means that we can have different versions of some packages in that folder than those that we have globally installed. This is useful because some versions of this project might need specifically some requirements that change over time.

### Steps for Windows:

- First step, clone the repository:
```bash
git clone https://github.com/Unbo10/ParticleSwarmOptimization.git
```

- Next, in the folder that you cloned the repository, create the virtual environment:
```bash
pip install virtualenv
```

- Create environment folder inside the current project directory:
```bash
python -m venv env
```

- Activate the virtual environment:
```bash
env\Scripts\activate.bat
```
- Once you activate it you should see ```(env)``` on the terminal.

- Install the project package:
```bash
pip install -e.
```

- Go to the pso folder:
```bash
cd pso
```
- Run main.py:
```bash
py main.py
```

## Class Diagram of the swarm and vector packages:
``` mermaid
    classDiagram
    class Optimization{
        - I Data data
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - int dimensions
        - int iterations
        - int particle_amount
        - ParticleSwarm swarm

        - heuristic(Position position, int selection)
        - optimize()

        + get_dimensions(): int
        + get_index(): int
        + get_iterations(): int
        + get_swarm(): ParticleSwarm
    }
    Optimization "1" --o "1" ParticleSwarm


    class ParticleSwarm{
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - int particle_amount
        - list[Particle] particles
        - Position gbest
        + callable heuristic_f

        - __repr__() : str
        # initialize_particles_randomly(int bound)
        + update_gbest(): None

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector
        + get_particles(): ~Particle~
        + get_heuristic(): callable
    }
    ParticleSwarm "1" o--"*" Particle

    class Particle{
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        + dict color
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - Heuristic heuristic
        - Position pbest
        - Position position
        - Velocity velocity
        - int index
        - bool has_gbest

        # update_pbest(position)
        # update_velocity(Position gbest)
        + initialize_randomly(int bound)
        
        + get_pbest()
        + get_position()
        + get_velocity()
        + get_heuristic()
        + get_index()

        + set_heuristic(Heuristic heuristic)
        + set_index(int index)
        + set_pbest(Position pbest)
        + set_position(Position position)
        + set_velocity(Velocity velocity)
    }
    Particle "1" o-- "1" Heuristic
    Particle "1" o-- "2" Position
    Particle "1" o-- "1" Velocity


    class Vector {
        # np.ndarray coordinates
        # int dimensions

        - __repr__() : str
        + initialize_randomly(float)
        # update()
        
        + get_coordinates() : np.ndarray
        + get_dimensions() : int
        + set_coordinates(coordinates: np.ndarray)
        + set_dimensions(dimensions: int)  
    }

    class Heuristic{
        <!-- ? Should the inherited attributes be kept in the child class?-->
        <!-- ? Should ndarrays be simply called arrays since the fact they are np has to do more with the implementation? -->
        # callable heuristic
        # update()
        + get_heuristic_f()
    }
    Heuristic "1" --|> "1" Vector

    class Position{
        # update(Velocity: velocity)
    }
    Position "1" --|> "1" Vector

    class Velocity {
        
        - __init__(int dimensions)
    }
    Velocity "1" --|> "1" Vector

```




## Complete Class Diagram, with the data and graphic user interface packages:
``` mermaid
    classDiagram
    direction TB

    class Main {
        + GUI gui
        + Data database
        + ~Optimization~ optimization_history
        
        + get_last_xslx_file() str
        + get_version() str
    }

    %% ? Should inherited composition (or any) relations be stated

    Main "1" --* "1" Data
    Main "1" --o "*" Optimization
    Main "1" --* "1" GUI

    class GUI {
        - C tk.Tk() root
        - __init__(~Optimization~ optimization_history, str program_version)
        # tk.Frame root_frame
        - ~Optimization~ optimization_history
        # int window_height
        # window_width
        - <ExitMenu> exit_menu
        - <MainMenu> main_menu
        - <SelectMenu> select_menu
        - dict menus

        # change_menu(menu_name)
        # initialize_root(int width, int height, str title)
        + run()
    }

    GUI "1" --> "1" Color : uses (?)
    GUI "1" --o "*" Optimization
    GUI "1" --* "1" MainMenu
    GUI "1" --* "1" SelectMenu
    GUI "1" --* "1" ExitMenu

    class Color {
        + C str test1_bg
        + C str test2_bg
        + C str test3_bg
    }

    class FontName {
        + str button
        + str label
        + str title
    }

    class ExitMenu {
        + tk.Frame root
        - callable initialize_root
        - tk.PhotoImage image
        - tk.Label label
        - tk.Text text

        + display()
    }

    ExitMenu --> Color : "uses(?)"
    ExitMenu --> FontName : "uses(?)"

    class MainMenu {
        %% - __init__(tk.Frame parent_frame, callable initialize_window, callable change_menu, str program_version, int window_width, int window_height)
        # tk.Frame parent_frame
        + tk.Frame root
        - callable initialize_window
        # tk.Label title
        # int window_width
        # int window_height
        # int title_height
        # int bottom_frame_height
        - BottomFrame bottom_frame
        - OptionsFrame options_frame

        + display()
    }

    MainMenu "1" --* "1" BottomFrame
    MainMenu "1" --* "1" OptionsFrame
    MainMenu --> Color : "uses(?)"
    MainMenu --> FontName : "uses(?)"

    class BottomFrame {
        %%- __init__(tk.Frame parent_frame, int window_width, int window_height, int title_height, int bottom_frame_height, str program_version)
        - int window_width
        - int window_height
        - int title_height
        - int height
        - int pop_up_frame_height
        - BottomButton info_button
        - BottomButton help_button
        - tk.Label version_label
        # <PopUpFrame> pop_up_frames

        + display()
    }
    
    BottomFrame "1" --|> "1" tkFrame
    BottomFrame --> Color : "uses(?)"
    BottomFrame --> FontName : "uses(?)"
    BottomFrame "1" --* "2" BottomButton

    class BottomButton {
        - tk.PhotoImage image
        - tk.PhotoImage active_image
        - str bg
        - str abg
        - str cbg
        + PopUpFrame pop_up_frame

        - enter(tk.Event e)
        - leave(tk.Event e)
        - click(tk.Event e)
        - release(tk.Event event, <PopUpFrame> pop_up_frames)
        - bind_to_events(dict pop_up_frames)
        + display(<PopUpFrame> pop_up_frames, int row, int column, str sticky)
    }

    BottomButton "1" --|> "1" tkButton
    BottomButton --> Color : "uses(?)"
    BottomButton "1" --* "1" PopUpFrame

    class PopUpFrame {
        - str name
        - str text_to_insert
        - tk.Text text
        - tk.Button hide_button
        - tk.Scrollbar scrollbar
        - int width
        - int height
        - int y
        + bool visible

        - enter_hide_button(tk.Event e)
        - leave_hide_button(tk.Event e)
        - click_hide_button(tk.Event e)
        - release_hide_button(tk.Event e, PopUpFrame other_frame)
        - bind_hide_button(PopUpFrame other_frame)
        + display(PopUpFrame other_frame)
        + get_name() str
    }

    PopUpFrame "1" --|> "1" tkFrame
    PopUpFrame --> Color : "uses(?)"
    PopUpFrame --> FontName : "uses(?)"

    class OptionsFrame {
        - tk.Frame parent_frame
        + tk.Frame root
        - callable change_menu
        - tk.Label title
        - int window_width
        - int window_height
        - int title_height
        - int bottom_frame_height
        - dict button_parameters
        - OptionsButton create_button
        - OptionsButton select_button
        - OptionsButton exit_button
        - dict buttons

        +display()
    }

    OptionsFrame "1" --* "3" OptionsButton
    OptionsFrame --> Color : "uses(?)"
    OptionsFrame --> FontName : "uses(?)"
    OptionsFrame "1" --* "3" OptionsButton

    class OptionsButton{
        - tk.Frame parent_frame
        - callable callable
        - dict callable_args
        - tuple padx
        - tuple pady
        - str optim_button_fg
        - str optim_button_hbg
        - str optim_button_hcolor
        - str optim_button_abg
        - str optim_button_bg
        - str back_button_afg

        - enter(tk.Event e)
        - leave(tk.Event e)
        - click(tk.Event e)
        - release(tk.Event event, list<PopUpF> pop_up_frames)
        - bind_to_events(dict pop_up_frames)
        + grid_display(intPopUpFrame  pop_up_frames, row, int column, str sticky)
        + pack_display(str fill, str anchor)
    }

    OptionsButton "1" --|> "1" tkButton
    OptionsButton --> Color : "uses(?)"

    class CreateButton {
        - str text1
        - str text2
        - str __active_text
        - callable __callable1
        - callable __callable2

        + __init__(tk.Frame parent_frame, str text1, str text2, callable callable1, callable callable2, int padx, int pady)
        - _release(tk.Event event)
    }

    CreateButton "1" --|> "1" OptionsButton
    CreateButton --> Color : "uses"


    class CreateInput {
        - tk.Label __label
        - tk.StringVar input_value
        - tk.Entry entry
        - str __default_value

        + __init__(tk.Frame parent_frame, str default_value, str text, int width)
        - __select_text(tk.Event e) : None
        + grid(int label_row, int column, str sticky)
        + get_input() : str
    }

    CreateInput --> Color : "uses"
    CreateInput --> FontName : "uses"

    class CreateMenu {
        - tk.Button __run_view_button
        - tk.Button __reset_button
        - tk.Frame __buttons_frame
        - tk.Button __back_button
        - tk.Tk root
        - int __width
        - int __height
        - tk.Label __title
        - tk.Frame __inputs_frame

        + display_graph(str graph_type)
        + forget() : None
        + run_or_view_optimization(tk.Event e, bool create_optimization) : None
        - __create_contour_levels(list[float] levels_boundaries) : np.linspace
        - __create_x_y_values(int bound) : tuple[np.ndarray]
        - __create_fig(str option) : Figure
    }

    CreateMenu --> Color : "uses"
    CreateMenu --> FontName : "uses"

    class FunctionChoiceMenu {
        - list~str~ __options
        - callable __display_graph
        - tk.StringVar __choice
        - tk.OptionMenu __dropdown_menu
        - tk.Label __label

        + __init__(tk.Frame parent_frame, str text, list~str~ options, callable display_graph)
        - __trigger_graph_change(*args) : None
        + grid(int label_row, int column, str sticky) : None
    }

    FunctionChoiceMenu --> Color : "uses"
    FunctionChoiceMenu --> FontName : "uses"

    class SelectMenu {
        %% - __init__(tk.Frame parent_frame, callable initialize_window, callable change_menu, ~Optimization~ optimization_history, int window_width, int window_height)
        - ~Optimization~ optimization_history
        - int window_width
        - int window_height
        - int title_height
        - callable initialize_window
        + tk.Frame root
        - tk.Label title
        - tk.Canvas canvas
        - int container_frame_width
        - int container_frame_height
        - tk.Frame container_frame
        - int scrollbar_width
        - tk.Scrollbar scrollbar
        - BackButton back_button
        - tk.Label no_optimizations_label
        - OptionsButton create_optimization_button
        - ~OptimizationFrame~ optimization_frames

        - scroll_mouse_wheel(tk.Event event)
        + display()
        + forget()
    }

    SelectMenu --> Color : "uses(?)"
    SelectMenu --> FontName : "uses(?)
    SelectMenu "1" --* "1" OptionsButton
    SelectMenu "1" *-- "*" OptimizationFrame
    SelectMenu "1" --* "1" BackButton

    class BackButton {
        - tk.PhotoImage image
        - tk.PhotoImage active_image
        - int width
        - int height
        - callable change_menu
        - dict change_menu_args

        - enter(tk.Event e)
        - leave(tk.Event e)
        - click(tk.Event e)
        - release(tk.Event e)
        - bind_to_events()
        + display()
    }

    class ViewButton {
        - tk.Image __image
        - tk.Image __active_image
        - ViewFrame view_frame
        - callable __forget_select_menu

        + __init__(tk.Frame master, tk.Image image, tk.Image active_image, callable forget_select_menu, callable initialize_window, callable change_menu, Optimization optimization, str bg=Color.select_label_optim_bg, str fg=Color.select_label_optim_fg)
        - __enter(tk.Event e) : None
        - __leave(tk.Event e) : None
        - __click(tk.Event e) : None
        - __bind_to_events() : None
    }

    ViewButton --> Color : "uses"
    ViewButton --> ViewFrame : "contains"
    ViewButton --> Optimization : "uses"

    class ViewFrame {
        - callable __initialize_window
        - Optimization __optimization
        - Figure __function_fig
        - tk.Label __title
        - BackButton __back_button

        + __init__(callable initialize_window, callable change_menu, Optimization optimization, Figure function_fig, str bg=Color.test3_bg) : ViewFrame
    }

    ViewFrame --> Color : "uses"
    ViewFrame --> FontName : "uses"
    ViewFrame --> BackButton : "contains"
    ViewFrame --> Optimization : "uses"
    ViewFrame --> Figure : "uses"

    class OptimizationFrame {
        %% - __init__(tk.Frame root, Optimization optimization, int width, int height, int separation, int scrollbar_width, int frame_index)
        - tk.Frame frame
        - int width
        - int height
        - int scrollbar_width
        - int separation
        - int index
        - dict widget_parameters
        - tk.Label Fontname_label
        - tk.Label function_label
        - tk.Label dimensions_label
        - tk.Label minima_indicator_label
        - tk.Label minima_value_label
        - tk.Label cognitive_coefficient_label
        - tk.Label num_particles_label
        - tk.Label social_coefficient_label
        - tk.PhotoImage preview_image
        - tk.PhotoImage preview_active_image
        - tk.Button preview_button
        - tk.Label inertia_coefficient_label
        - tk.Label iterations_label

        +display(int parent_width)
        + enter_preview_button(e)
        + click_preview_button(e)
        + leave_preview_button(e)
        + release_preview_button(e)    
    }

    class Optimization{
        - I Data data
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - int dimensions
        - int iterations
        - int particle_amount
        - ParticleSwarm swarm

        - heuristic(Position position, int selection)
        - optimize()

        + get_dimensions(): int
        + get_index(): int
        + get_iterations(): int
        + get_swarm(): ParticleSwarm
    }
    Optimization "1" --o "1" ParticleSwarm
    Optimization "*" --* "1" Data

    class Data {
        - __init__(str excel_file_name)
        - <pd.DataFrame> particle_history
        - ~~int~~ gbest_history
        - int number_of_optimizations
        - str xlsx_name
        - str xlsx_path

        + append_gbest_indexes(list<int> optimization_gbest_indexes)
        + append_optimization(pd.DataFrame optimization_df)
        + create_spreadsheet()
        + print_optimization(int optimization_index)
        + get_particle_history() ~pd.DatscrollbaraFrame~
    }

    class ParticleSwarm{
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - int particle_amount
        - list[Particle] particles
        - Position gbest
        + callable heuristic_f

        - __repr__() : str
        # initialize_particles_randomly(int bound)
        + update_gbest(): None

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector
        + get_particles(): ~Particle~
        + get_heuristic(): callable
    }
    ParticleSwarm "1" o--"*" Particle

    class Particle{
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        + dict color
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - Heuristic heuristic
        - Position pbest
        - Position position
        - Velocity velocity
        - int index
        - bool has_gbest

        # update_pbest(position)
        # update_velocity(Position gbest)
        + initialize_randomly(int bound)
        
        + get_pbest()
        + get_position()
        + get_velocity()
        + get_heuristic()
        + get_index()

        + set_heuristic(Heuristic heuristic)
        + set_index(int index)
        + set_pbest(Position pbest)
        + set_position(Position position)
        + set_velocity(Velocity velocity)
    }
    Particle "1" o-- "1" Heuristic
    Particle "1" o-- "2" Position
    Particle "1" o-- "1" Velocity


    class Vector {
        # np.ndarray coordinates
        # int dimensions

        - __repr__() : str
        + initialize_randomly(float)
        # update()
        
        + get_coordinates() : np.ndarray
        + get_dimensions() : int
        + set_coordinates(coordinates: np.ndarray)
        + set_dimensions(dimensions: int)  
    }

    class Heuristic{
        <!-- ? Should the inherited attributes be kept in the child class?-->
        <!-- ? Should ndarrays be simply called arrays since the fact they are np has to do more with the implementation? -->
        # callable heuristic
        # update()
        + get_heuristic_f()
    }
    Heuristic "1" --|> "1" Vector

    class Position{
        # update(Velocity: velocity)
    }
    Position "1" --|> "1" Vector

    class Velocity {
        
        - __init__(int dimensions)
    }
    Velocity "1" --|> "1" Vector

    ```
