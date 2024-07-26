from libqtile import bar, widget
import mycolours

def barSeparator():
    separator = widget.Sep(linewidth = 0,
        size_percent = 35,
        padding = 20)
    return separator

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
            foreground=mycolours.pastel['Yellow'],
            width=170
        ),
        barSeparator(),
        widget.Load(
            format="LOAD: {load:.1f} ({time})",
            foreground=mycolours.pastel['Pink']
            ),
        barSeparator(),
        widget.Memory(
            format="MEMORY: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            foreground=mycolours.pastel['Blue']
            ),
        barSeparator(),
        widget.CPU(
            format="CPU: {freq_current}GHz {load_percent}%",
            foreground=mycolours.pastel['Purple'],
            width=125
        ),
        barSeparator(),
        widget.Battery(
            format="BATTERY: {percent:2.0%} ({hour:d}:{min:02d})",
            foreground=mycolours.pastel['Orange'],
            low_oreground=mycolours.pastel['Orange']
        ),
        barSeparator(),
        widget.KeyboardLayout(
            foreground=mycolours.pastel['Blue'],
        ),
        barSeparator(),
        widget.Clock(
            format="%Y-%m-%d %H:%M:%S",
            foreground=mycolours.pastel['Green']
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