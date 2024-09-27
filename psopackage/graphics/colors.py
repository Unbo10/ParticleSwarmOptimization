class Color:

    # * TESTS
    test1_bg: str = "#ff0000"
    test2_bg: str = "#00ff00"
    test3_bg: str = "#0000ff"
    # ? Would it be better to do it with a dictionary?
    # * WINDOWS AND FRAMES

    bottom_menu_bg: str = "#0d42a3"
    help_frame_bg: str = "#a1adc4"
    info_frame_bg: str = "#a1adc4"
    window_bg: str = "#f0f0f0"
    goodbye_frame_bg: str = "#1b1b1b"

    # ! Consider implementing hbg in all buttons

        # * Select menu
    select_inner_frame_bg: str = "#afcff8"
    select_inner_frame_fg: str = "#000000"
    select_inner_button_bg: str = "#f0f0f0"

    # * Create optimization menu
    create_entry_bg: str = "#d3d3d3"
    create_entry_fg: str = "#000000"

    create_label_bg: str = "#d3d3d3"
    create_label_fg: str = "#000000"

    create_button_bg: str = "#95d8ec"
    create_button_fg: str = "#000000"
    create_button_abg: str = "#d3d3d3"
    create_button_afg: str = "#000000"
    create_button_hbg: str = "#d3d3d3"
    create_button_hcolor: str = "#000000"
    create_button_cbg: str = ""

    # * BUTTONS, LABELS AND TEXT

    # * Background
    # * Main menu
    bottom_button_bg: str = "#0d42a3"
    hide_button_bg: str = "#a3490d"
    optim_button_bg: str = "#89e379"

    bottom_label_bg: str = info_frame_bg
    optim_label_bg: str = "#d3d3d3"
    goodbye_label_bg: str = goodbye_frame_bg

    goodbye_text_bg: str = goodbye_frame_bg

    # * Select menu
    select_button: str = "#f0f0f0"
    select_label_optim_bg: str = "#d3d3d3"
    select_label_no_optim_bg: str = "#d1d1d1"
    select_title_bg: str = "#d3d3d3"
    back_button_bg = select_title_bg
    preview_button_bg: str = select_label_optim_bg

    # * Foreground (font color)
    # * Main menu
    bottom_button_fg: str = "#dfdfdf"
    optim_button_fg: str = "#000000"
    hide_button_fg: str = "#dfdfdf"

    bottom_label_fg: str = "#000000"
    goodbye_text_fg: str = "#dfdfdf"

    # * Select menu
    select_label_optim_fg: str = "#000000"
    select_label_no_optim_fg: str = "#000000"
    select_title_fg: str = "#000000"
    
    # * Active background
    # * Main menu
    bottom_button_abg: str = "#225fd1"
    optim_button_abg: str = "#123f0a" # ! Consider changing optim (gets confused in select menu)
    hide_button_abg: str = "#d25e0a"

    # * Select menu
    back_button_abg: str = "#f0f0f0"
    preview_button_abg: str = "#f7f7f7"

    # * Active foreground
    # * Main menu
    bottom_button_afg: str = "#ffffff"
    optim_button_afg: str = "#ffffff"
    hide_button_afg: str = "#000000"

    # * Select menu
    back_button_afg: str = "#000000"

    # * Highlight background (focused)
    # * Main menu
    bottom_button_hbg: str = bottom_button_bg
    hide_button_hbg: str = "#a23d0a"
    optim_button_hbg: str = optim_button_bg

    # * Select menu
    back_button_hbg: str = "#922929"
    preview_button_hbg: str = preview_button_abg

    # * Highlight color (focused)
    # * Main menu
    bottom_button_hcolor: str = "#ffffff"
    hide_button_hcolor: str = "#000000"
    optim_button_hcolor: str = optim_button_abg

    # * Select menu
    back_button_hcolor: str = "#000000"
    preview_button_hcolor: str = preview_button_abg


    # * Clicked background
    # * Main menu
    bottom_button_cbg: str = "#033186" # Todo: Consider changing it
    optim_button_cbg: str = "#012422"
    hide_button_cbg: str = "#a23d0a"

    # * Select menu
    back_button_cbg: str = back_button_bg
    preview_button_cbg: str = "#e0e0e0"

    # * Clicked foreground
    # * Main menu
    optim_button_cfg: str = optim_button_afg
    hide_button_cfg: str = hide_button_fg

    # * Select menu
    back_button_cfg: str = "#000000"

    # * SCROLLBAR
    # * Main menu
    bottom_scrollbar_bg: str = "#2b2a2a"
    bottom_scrollbar_trough: str = bottom_label_bg
    bottom_scrollbar_abg: str = "#0f0f0f"
    bottom_scrollbar_hbg: str = bottom_label_bg
    bottom_scrollbar_hcolor: str = "#000000"
    
    # * Data colors
    siders: str = "ffffff"
    common_side: str = "000000"
    title_cell: str = "f0f0f0"
    grad_fill_start: str = "085063"
    grad_fill_stop: str = "d6e416"
    cell_fill: str = "042d53"
    cell2_fill: str = "dfdfdf"