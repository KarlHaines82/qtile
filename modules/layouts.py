from libqtile.config import Match
from libqtile.layout import floating, max, xmonad, tree, tile, zoomy
from .theme import palette as theme_colors

layouts = [
    max.Max(margin=15),
    xmonad.MonadTall(
        ratio=0.75,
        max_ratio=0.8,
        min_ratio=0.5,
        change_ratio=0.05,
        margin=15,
    ),
    tree.TreeTab(
        fontsize=9,
        sections=["TreeTab"],
        section_fontsize=13,
        active_bg=theme_colors[0],
        padding_left=0,
        padding_x=5,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=175,
        bg_color=["#000000A8", "#29283BA8", "#DD6DA5A8"],
    ),
    tile.Tile(margin=15),
    floating.Floating(),
    zoomy.Zoomy(margin=15),
]
floating_layout = floating.Floating(
    float_rules=[
        *floating.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="dunst"),
        Match(wm_class="gimp"),
        Match(wm_class="keepassxc"),
        # Match(wm_class="telegram-desktop"),
        Match(wm_class="kvantummanager"),
        Match(wm_class="qt5ct"),
        Match(wm_class="lxappearance"),
    ]
)
