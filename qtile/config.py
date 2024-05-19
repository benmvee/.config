##########################
### benmv qtile config ###
##########################

import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import colours

if qtile.core.name == "x11":
    x11 = True
    wayland = False
    start = '~/.config/qtile/x11.sh'
    launcher = "rofi -combi-modi window,drun,ssh -theme solarized -font \"hack 10\" -show combi"
elif qtile.core.name == "wayland":
    wayland = True
    x11 = False
    start = '~/.config/qtile/wayland.sh'
    launcher = "fuzzel"

### STARTUP
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(start)
    subprocess.Popen([home])
    
@hook.subscribe.startup
def autostart():
    os.system("setxkbmap gb")
    os.system('~/.config/screens.sh')


### MODIFIER
mod = "mod4"

### SHORTCUTS
terminal = "alacritty"
browser = "google-chrome"
files = "dolphin"


### KEYS

keys = [
    # Switching windows.
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving windows.
    Key([mod, "shift"], "Left", lazy.layout.swap_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resizing windows.
    Key([mod, "control"], "Left", lazy.layout.normalize(), desc="Normalize Monad layout"),
    Key([mod, "control"], "Right", lazy.layout.maximize(), desc="Maximize focused window in Monad layout"),
    Key([mod, "control"], "Down", lazy.layout.shrink(), desc="Shrink window in Monad layout"),
    Key([mod, "control"], "Up", lazy.layout.grow(), desc="Grow window in Monad layout"),

    # Killing windows.
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # Toggle layouts.
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Launching things.
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "d", lazy.spawn(launcher), desc="Launch launcher"),
    Key([mod], "f", lazy.spawn(files), desc="Launch file manager"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Session management.
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

### GROUPS
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name),),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name),),
            # # mod1 + control + letter of group = move focused window to group
            Key([mod, "control"], i.name, lazy.window.togroup(i.name), desc="move focused window to group {}".format(i.name)),
        ]
    )

### DEFAULTS

layout_defaults = dict(
    margin = 8,
    border_width = 0,
    border_focus = "87CEEB",
    border_normal = "4682B4"
)

widget_defaults = dict(
    font = "Fira Sans Mono Bold",
    fontshadow = "000000",
    fontsize = 13,
    padding = 3
)

def barSeparator():
    separator = widget.Sep(linewidth = 0,
        size_percent = 35,
        padding = 20)
    return separator

extension_defaults = widget_defaults.copy()

layouts = [
    layout.MonadThreeCol(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    layout.Max()
]


### BAR

def makeBar(primary=False):
    widgets = [
        widget.GroupBox(
            highlight_method='line',
            highlight_color=['00000000', '00000000'],
            this_current_screen_border='87CEEB',
            this_screen_border='4682B4',
            other_current_screen_border='87CEEB',
            other_screen_border='676767',
            rounded=False
        ),
        widget.Spacer(10),
        widget.Prompt(
            prompt="[benmv@archlinux ~]$ ",
            font="Hack Bold",
            cursorblink=0.3
        ),
        widget.Spacer(),
        barSeparator(),
        widget.Net(
            format="SPEED: {up:.1f}{up_suffix} ↑↓ {down:.1f}{down_suffix}",
            prefix='M',
            foreground=colours.pastel['Yellow'],
            width=170
        ),
        barSeparator(),
        widget.Load(
            format="LOAD: {load:.1f} ({time})",
            foreground=colours.pastel['Pink']
            ),
        barSeparator(),
        widget.Memory(
            format="MEMORY: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            foreground=colours.pastel['Blue']
            ),
        barSeparator(),
        widget.CPU(
            format="CPU: {freq_current}GHz {load_percent}%",
            foreground=colours.pastel['Purple'],
            width=125
        ),
        barSeparator(),
        widget.Battery(
            format="BATTERY: {percent:2.0%} ({hour:d}:{min:02d})",
            foreground=colours.pastel['Orange'],
            low_oreground=colours.pastel['Orange']
        ),
        barSeparator(),
        widget.KeyboardLayout(
            foreground=colours.pastel['Blue'],
        ),
        barSeparator(),
        widget.Clock(
            format="%Y-%m-%d %H:%M:%S",
            foreground=colours.pastel['Green']
        ),
        barSeparator()
    ]

    if primary:
        widgets.extend([
            widget.Systray(),
            widget.Spacer(2),
            widget.CurrentLayoutIcon(scale=0.5),
            widget.Spacer(4)
        ])
    else:
        widgets.extend([
            widget.Spacer(length=2),
            widget.CurrentLayoutIcon(scale=0.5),
            widget.Spacer(4)
        ])

    thisBar = bar.Bar(widgets, 30, margin = [0,8,8,8], background=["000000"])
    return thisBar

wallpaper_default = 'Wallpapers/5.jpg'
wallpaper_mode_default = 'stretch'

screens = [
    Screen(
        bottom=makeBar(1),
        wallpaper=wallpaper_default,
        wallpaper_mode=wallpaper_mode_default
    ),
    Screen(
        bottom=makeBar(),
        wallpaper=wallpaper_default,
        wallpaper_mode=wallpaper_mode_default
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
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
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
