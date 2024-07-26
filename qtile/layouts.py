from libqtile import layout

layout_defaults = dict(
    margin = 8,
    border_width = 0,
    border_focus = "87CEEB",
    border_normal = "4682B4"
)


layouts = [
    layout.MonadThreeCol(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    layout.Max()
]
