# LaHerencia


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

    class OptionsButton{
        - tk.Frame parent_frame
        - callable callable
        - dict callable_args
        - tuple padx
        - tuple pady

        - enter(event e)
        - leave(event e)
        - click(event e)
        - release(event event)
        - display(int row, int column, str sticky)
    }

    OptionsButton --> Color : "uses(?)"
    OptionsButton "1" --|> "1" tkButton

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

    class OptimizationFrame {
        %% - __init__(tk.Frame root, Optimization optimization, int width, int height, int separation, int scrollbar_width, int frame_index)
        - tk.Frame frame
        - int width
        - int height
        - int scrollbar_width
        - int separation
        - int index
        - dict widget_parameters
        - tk.Label name_label
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