from .theme import palette as theme_colors

# from json import decoder
from os.path import expanduser

from libqtile.config import Screen
from libqtile import bar, qtile
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget import lazify_imports, statusnotifier
from qtile_extras.widget.decorations import \
        PowerLineDecoration as powerline_decor
from modules.mywidgets import CapsNumWidget

qtile_core = str(qtile.core.name)
ssep = {
    'padding': 4,
}


powerline_right = {
    "decorations": [
        powerline_decor(),
        powerline_decor(path="arrow_right")
    ]
}
powerline_left = {
    "decorations": [
        powerline_decor(),
        powerline_decor(path="arrow_left")
    ]
}


top_widgets = [
    widget.Image(
        **powerline_left,
        filename=expanduser("~/.config/qtile/icons/arch01.png"),
        mouse_callbacks={
            'Button1': lazy.spawn("rofi -modi combi,window,drun \
                -combi window,drun -show drun")
        },
        height=18,
        padding=5,
        margin=2,
        scale=0.7,
        background=theme_colors[16],
    ),
    widget.GroupBox(
        **powerline_left,
        name="GroupBoxTop",
        fontshadow="#23283b",
        fontsize=14,
        background=theme_colors[8],
        active=theme_colors[20],
        inactive=theme_colors[18],
        rounded=True,
        highlight_method='block',
        urgent_alert_method='line',
        urgent_border="#0a0",
        this_current_screen_border=theme_colors[17],
        this_screen_border=theme_colors[17],
        other_current_screen_border=theme_colors[20],
        other_screen_border=theme_colors[3],
        disable_drag=True,
        markup=True,
        padding=2,
        margin=3,
    ),
    widget.TextBox(width=1, background=theme_colors[3]),
    widget.CurrentLayoutIcon(
        **powerline_left,
        custom_icon_paths=[expanduser("~/.config/qtile/icons")],
        background=theme_colors[3],
        padding=5,
        scale=0.8,
    ),
    widget.Prompt(**powerline_left),
    widget.Spacer(width=bar.STRETCH, **powerline_right),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
        **powerline_right,
    ),
    widget.Visualizer(),
]


# Add Systray widget for x11 or StatusNotifier for wayland
if qtile_core == 'wayland':
    top_widgets.append(statusnotifier.StatusNotifier(
        icon_size=22,
        icon_path="/usr/share/icons/breeze-dark",
        margin_x=6,
    ))
elif qtile_core == 'x11':
    top_widgets.append(widget.Systray(
        icon_size=22,
        icon_path="/usr/share/icons/breeze-dark",
        margin_x=6,
    ))


top_widgets.extend([
    widget.Visualizer(),
    widget.UPowerWidget(),
    CapsNumWidget(),
    widget.Clock(
        format="%I:%M%p",
        fontsize=18,
        align="center",
    ),
    widget.TextBox(
        fontsize=16,
        margin_y=4,
        mouse_callbacks={'Button1': lazy.shutdown()},
        text="",
    ),
])


screens = [
    Screen(
        top=bar.Bar(
            top_widgets,
            26,
            background=theme_colors[0],
        ),
        bottom=bar.Bar([
            widget.TextBox(
                **powerline_left,
                background=theme_colors[9],
                text="qtile.core: "+qtile_core,
            ),
            # widget.LaunchBar(
            #     **powerline_left,
            #     # FIXME
            #     background=theme_colors[9],
            # ),
            widget.TaskList(**powerline_left),
            widget.TextBox(width=1, **powerline_right),
            widget.Wlan(
                **powerline_right,
                format='{essid} {percent:2.02%}',
                background=theme_colors[3],
            ),
            widget.Image(
                filename=expanduser(
                    "~/.config/qtile/icons/cpu.svg"),
                height=14,
                background=theme_colors[5],
                padding=4,
            ),
            widget.CPU(
                background=theme_colors[5],
                fontsize=16,
                font="Agave Nerd Font Bold",
                format="{load_percent}%",
                width=54,
                align="right",
            ),
            widget.CPUGraph(
                **powerline_right,
                background=theme_colors[5],
                width=60,
                margin_x=10,
                type="line",
                line_width=1,
                border=0,
            ),
            widget.Image(
                filename=expanduser(
                    "~/.config/qtile/icons/gnome-dev-memory.svg"),
                height=14,
                background=theme_colors[7],
                padding=4,
            ),
            widget.MemoryGraph(
                **powerline_right,
                background=theme_colors[7],
                width=60,
                margin_x=10,
            ),
            widget.KeyboardLayout(
                background=theme_colors[4],
            )],
        26, background=theme_colors[0]),
        wallpaper_mode='stretch',
        wallpaper=expanduser('~/.config/qtile/wallpaper/vaderwallpaper.jpg'),
    )
]
