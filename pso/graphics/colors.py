class Color:
    # ? Would it be better to do it with a dictionary?
    # * WINDOWS AND FRAMES
    window_bg: str = "#f0f0f0"
    bottom_menu_bg: str = "#0d42a3"
    # * BUTTONS AND LABELS
    # * Background
    bottom_button_bg: str = "#0d42a3"
    optim_button_bg: str = "#89e379"
    optim_label_bg: str = "#d3d3d3"
    # * Foreground (font color)
    bottom_button_fg: str = "#dfdfdf"
    optim_button_fg: str = "#000000"
    # * Active background (hovered)
    bottom_button_abg: str = "#225fd1"
    optim_button_abg: str = "#123f0a"
    # * Active foreground (hovered)
    bottom_button_afg: str = "#ffffff"
    optim_button_afg: str = "#ffffff"
    # * Highlight background (focused)
    bottom_button_hbg: str = bottom_button_abg
    optim_button_hbg: str = "#000000"
    # * Clicked background
    bottom_button_cbg: str = "#033186" # Todo: Consider changing it
    optim_button_cbg: str = "#012422"
    # * Clicked foreground
    bottom_button_cfg: str = bottom_button_afg
    optim_button_cfg: str = optim_button_afg
