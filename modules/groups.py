from libqtile.config import Group, Key, ScratchPad, DropDown
from libqtile.lazy import lazy
from .keys import keys

mod = "mod4"

# Set up our groups and bind their respective keys, got a few workarounds
# in effect since we're using these fancy icons
group_names = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
# Set some default layouts
groups = []
for n in group_names:
    name = n[:1]
    match(name):
        case '1' | '2' | '6':
            groups.append(Group(n, layout='max'))
        case '8' | '9':
            groups.append(Group(n, layout='floating'))
        case _:
            groups.append(Group(n, layout='max'))


# now bind the keys using the first char in each group name
for g in groups:
    keys.extend([
        Key([mod], g.name[:1], lazy.group[g.name].toscreen(), desc="Switch to group {}".format(g.name)),
        Key([mod, "shift"], g.name[:1], lazy.window.togroup(g.name, switch_group=True),
            desc="Move current container to group {}".format(g.name)),
    ])


# Setup ScratchPad group with 2 dropdowns
groups.extend([
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "alacritty --option window.opacity=0.95 \
                --option font.size=9.0", width=0.8, height=0.6, opacity=0.9),

        # define another term, exclusive qtile shell at bottom
        DropDown("qtile-shell", "alacritty --hold -e qtile shell",
                 x=0.05, y=0.4, width=0.9, height=0.6,
                 opacity=0.9, on_focus_lost_hide=True),
        ]),
])

keys.extend([
    # toggle visibiliy of above defined DropDown named "term"
    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], 'F11', lazy.group['scratchpad'].dropdown_toggle('qtile-shell')),
])
