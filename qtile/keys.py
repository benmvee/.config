from libqtile.config import Key
from libqtile.lazy import lazy
import defaults

mod = defaults.mod


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
    
    # Setting brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Toggle layouts.
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Launching things.
    Key([mod], "b", lazy.spawn(defaults.browser), desc="Launch browser"),
    Key([mod], "d", lazy.spawn(defaults.launcher), desc="Launch launcher"),
    Key([mod], "f", lazy.spawn(defaults.files), desc="Launch file manager"),
    Key([mod], "Return", lazy.spawn(defaults.terminal), desc="Launch terminal"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Session management.
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
   
]
