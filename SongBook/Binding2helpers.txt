songname_helper = """
MDTextField:
    hint_text: "Enter Song Name"
    helper_text: "It is Case Sensitive"
    helper_text_mode: "on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    size_hint_x: None
    width: 300
"""

songnum_helper = """
MDTextField:
    hint_text: "Enter Song Number"
    helper_text: "Enter Correct Number"
    helper_text_mode: "persistent"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    size_hint_x: None
    width: 300
"""