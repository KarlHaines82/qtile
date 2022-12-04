from libqtile.config import Screen, Bar
from libqtile.lazy import lazy
from libqtile import bar, widget
from os.path import expanduser
from theme import theme_colors
import mywidgets

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename=expanduser("~/.config/qtile/eos-icon.png"),
                    mouse_callbacks={
                        'Button1': lazy.spawn("rofi -modi combi,window,drun -combi window,drun -show drun")
                    },
                    background=theme_colors[0],
                    width=18,
                    height=18,
                    padding=3,
                ),
                widget.GroupBox(
                    name="GroupBoxTop",
                    font="UbuntuMono Nerd Font",
                    margin_y=4,
                    margin_x=0,
                    padding_y=0,
                    padding_x=0,
                    borderwidth=3,
                    active=theme_colors[-2],
                    inactive=theme_colors[-1],
                    rounded=True,
                    highlight_method='line',
                    urgent_alert_method='block',
                    urgent_border=theme_colors[8],
                    this_current_screen_border=theme_colors[9],
                    this_screen_border=theme_colors[4],
                    other_current_screen_border=theme_colors[0],
                    other_screen_border=theme_colors[0],
                    foreground=theme_colors[11],
                    background=theme_colors[0],
                    disable_drag=True,
                    markup=True,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[expanduser("~/.config/qtile/icons")],
                    foreground=theme_colors[9],
                    background=theme_colors[0],                    padding=5,
                    margin_x=4,
                    margin_y=4,
                    scale=0.7,
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                mywidgets.CapsNumWidget(),
                widget.WidgetBox(
                    widgets=[
                        widget.CPUGraph(width=60),
                        widget.MemoryGraph(width=60),
                        widget.HDDBusyGraph(width=60),
                    ],
                ),
                #widget.StatusNotifier(
                #    icon_size=22,
                #    icon_theme='Shiny-Color-Dark-Icons',
                #),
                widget.Systray(
                    icon_size=22,
                    icon_theme='Shiny-Color-Dark-Icons',
                ),
                #widget.PulseVolume(),
                widget.Clock(
                    fontsize=18,
                    format="%I:%M",
                    padding=4,
                ),
                widget.TextBox(

                    fontsize=20,
                    mouse_callbacks={'Button1': lazy.shutdown()},
                    font="UbuntuMono Nerd Font",
                    text=" ",
                    padding=2,
                    margin_x=2,
                ),
            ],
            30,
            background=theme_colors[0],
        ),
        wallpaper_mode='STRETCH',
        wallpaper='~/.config/qtile/bg2.png',
    ),
]
