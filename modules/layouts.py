from libqtile import layout
from libqtile.config import Match
from theme import theme_colors

layouts = [
    layout.Max(),
    layout.MonadTall(
        ratio=0.75,
        max_ratio=0.8,
        min_ratio=0.5,
        change_ratio=0.05,
    ),
    layout.TreeTab(
        fontsize=11,
        sections=["TreeTab"],
        section_fontsize=10,
        active_bg=theme_colors[0],
        padding_left=0,
        padding_x=0,
        padding_y=3,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200,
        bg_color="#000000B9",
    ),
    layout.Tile(),
    layout.Floating(),
]
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="dunst"),
        Match(wm_class="gimp"),
        Match(wm_class="keepassxc"),
        #Match(wm_class="telegram-desktop"),
        Match(wm_class="kvantummanager"),
        Match(wm_class="qt5ct"),
        Match(wm_class="lxappearance"),
    ]
)

