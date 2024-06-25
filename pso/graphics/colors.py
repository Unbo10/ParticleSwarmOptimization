class Color:
    # ? Would it be better to do it with a dictionary?
    # * WINDOWS AND FRAMES
    bottom_menu_bg: str = "#0d42a3"
    help_frame_bg: str = "#a1adc4"
    info_frame_bg: str = "#a1adc4"
    window_bg: str = "#f0f0f0"
    goodbye_frame_bg: str = "#1b1b1b"

    # * BUTTONS, LABELS AND TEXT
    # * Background
    bottom_button_bg: str = "#0d42a3"
    hide_button_bg: str = "#a3490d"
    optim_button_bg: str = "#89e379"

    bottom_label_bg: str = info_frame_bg
    optim_label_bg: str = "#d3d3d3"
    goodbye_label_bg: str = goodbye_frame_bg
    goodbye_text_bg: str = goodbye_frame_bg

    # * Foreground (font color)
    bottom_button_fg: str = "#dfdfdf"
    optim_button_fg: str = "#000000"
    hide_button_fg: str = "#dfdfdf"

    bottom_label_fg: str = "#000000"
    goodbye_text_fg: str = "#dfdfdf"
    
    # * Active background (hovered)
    bottom_button_abg: str = "#225fd1"
    optim_button_abg: str = "#123f0a"
    hide_button_abg: str = "#d25e0a"

    # * Active foreground (hovered)
    bottom_button_afg: str = "#ffffff"
    optim_button_afg: str = "#ffffff"
    hide_button_afg: str = "#000000"

    # * Highlight background (focused)
    bottom_button_hbg: str = bottom_button_abg
    optim_button_hbg: str = "#000000"

    # * Clicked background
    bottom_button_cbg: str = "#033186" # Todo: Consider changing it
    optim_button_cbg: str = "#012422"
    hide_button_cbg: str = "#a23d0a"

    # * Clicked foreground
    bottom_button_cfg: str = bottom_button_afg
    optim_button_cfg: str = optim_button_afg
    hide_button_cfg: str = hide_button_fg

    # * SCROLLBAR
    info_scrollbar_bg: str = "#2b2a2a"
    info_scrollbar_trough: str = bottom_label_bg
    info_scrollbar_abg: str = "#0f0f0f"