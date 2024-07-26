##########################
### benmv qtile config ###
##########################

from start import start, screencheck
from libqtile import layout, hook, qtile
from libqtile.config import Click, Drag, Match, Screen
from libqtile.lazy import lazy
import mybar
from keys import keys
from groups import groups
from defaults import mod
from layouts import layouts

@hook.subscribe.startup_once
def autostart_once():
    start(1)

@hook.subscribe.startup
def autostart():
    start()
    screencheck()
    

widget_defaults = dict(
    font = "Fira Sans Mono Bold",
    fontshadow = "000000",
    fontsize = 13,
    padding = 3
)

wallpaper_default = 'Wallpapers/5.jpg'
wallpaper_mode_default = 'stretch'

screens = [
    Screen(
        bottom=mybar.makeBar(1),
        wallpaper=wallpaper_default,
        wallpaper_mode=wallpaper_mode_default
    ),
    Screen(
        bottom=mybar.makeBar(),
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
        Match(wm_class='Steam'),
        Match(wm_class='steam'),
        Match(wm_class='game'),
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
