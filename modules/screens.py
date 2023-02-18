from .theme import palette as theme_colors
from .mywidgets import CapsNumWidget

from json import decoder
from os.path import expanduser

from libqtile.config import Screen
from libqtile import bar, qtile
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget import statusnotifier
from qtile_extras.widget.decorations import \
        PowerLineDecoration as powerline_decor

# from powerline.bindings.qtile import widget as qtile_widget
# from powerline.bindings.qtile.widget import QTilePowerline
# from powerline import Powerline


ssep = {
    'padding': 8,
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


screens = [
    Screen(
        top=bar.Bar([
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
                font="CaskaydiaCove Nerd Font SemiLight",
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
                margin=3

            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[expanduser("~/.config/qtile/icons")],
                background=theme_colors[3],
                padding=5,
                margin_x=4,
                margin_y=4,
                scale=0.7,
                **powerline_left,
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
            widget.Image(
                filename=expanduser(
                    "~/.config/qtile/icons/cpu.svg"),
                height=14,
                background=theme_colors[5],
                padding=4,
            ),
            widget.CPU(
                background=theme_colors[5],
                format="{load_percent}%",
                font="Tinos Nerd Font Bold",
                fontsize=12,
                width=46,
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
            # CapsNumWidget(
            #     **powerline_right,
            #     margin_x=8,
            # ),
            widget.Systray(
                icon_size=18,
                icon_path=expanduser(
                    '~/.local/share/icons/McMojave-circle-blue-dark/'),
                **powerline_right,
                padding=4,
                margin_x=8,
            ),
            widget.BrightnessControl(**powerline_right),
            widget.UPowerWidget(**powerline_right),
            widget.Clock(
                **powerline_right,
                font="OpenDyslexic Nerd Font Bold",
                fontsize=18,
                background=theme_colors[6],
                format="%I:%M%p",
                padding=8,
            ),
            widget.TextBox(
                **powerline_right,
                fontsize=16,
                font="CaskaydiaCove Nerd Font SemiLight",
                mouse_callbacks={'Button1': lazy.shutdown()},
                text="",
            )],
            22,
            background=theme_colors[0],
        ),
        bottom=bar.Bar([
            widget.TextBox(
                **powerline_left,
                background=theme_colors[9],
                text="qtile.core: %s" % qtile.core.name,
            ),
            widget.LaunchBar(
                **powerline_left,
                # FIXME
                background=theme_colors[9],
            ),
            widget.TaskList(
                **powerline_left,
            ),
            widget.TextBox(width=1, **powerline_right),
            widget.Wlan(
                **powerline_right,
                format='{essid} {percent:2.02%}',
                background=theme_colors[3],
            ),
            widget.KeyboardLayout(
                **powerline_right,
                background=theme_colors[4],
            ),
            widget.TextBox(width=5, background=theme_colors[4]),
            ], 25, background=theme_colors[0]
        ),
        wallpaper_mode='stretch',
        wallpaper=expanduser('~/.config/qtile/wallpaper/background.png'),
    )
]
