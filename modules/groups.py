from libqtile.config import Group, Key
from libqtile.lazy import lazy
from modules import keys

mod = "mod4"

# Set up our groups and bind their respective keys, got a few workarounds
# in effect since we're using these fancy icons
group_names = ["1  ", "2  ", "3  ", "4  ", "5  ", "6  ", "7  ", "8  ", "9  "]
# Set some default layouts
groups = []
for n in group_names:
    name=n[:1]
    match(name):
        case '1'|'2'|'6':
            groups.append(Group(n, layout='max'))
        case '3':
            groups.append(Group(n, layout='treetab'))
        case '4'|'5'|'9':
            groups.append(Group(n, layout='floating'))
        case _:
            groups.append(Group(n, layout='monadtall'))
# now bind the keys using the first char in each group name

# now bind the keys using the first char in each group name
for g in groups:
    keys.keys.extend([
        Key([mod], g.name[:1], lazy.group[g.name].toscreen(), desc="Switch to group {}".format(g.name)),
        Key([mod, "shift"], g.name[:1], lazy.window.togroup(g.name,switch_group=True),
            desc="Move current container to group {}".format(g.name)),
    ])
