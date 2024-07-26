import subprocess

def screencheck():
    result = subprocess.run(['xrandr', '|', 'grep', 'HDMI-1 connected'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = "Connected" if "HDMI-1 connected" in result.stdout else "Not Connected"
    
    if output == "Connected":
        # Turn off eDP-1 and set HDMI-1 as primary
        subprocess.Popen(["xrandr", "--output", "eDP-1", "--off"])
        subprocess.Popen(["xrandr", "--output", "HDMI-1", "--auto", "--primary"])
    else:
        # Turn off HDMI-1 and enable eDP-1
        subprocess.Popen(["xrandr", "--output", "HDMI-1", "--off"])
        subprocess.Popen(["xrandr", "--output", "eDP-1", "--auto", "--scale", "0.5x0.5"])

def start(once=False):
    if once:
        subprocess.Popen(["nm-applet", "--indicator"])
        subprocess.Popen(["pa-applet"])
        subprocess.Popen(["picom"])
        subprocess.Popen(["lxsession"])
        subprocess.Popen(["xset", "s", "off", "-dpms"])
    subprocess.run(["setxkbmap", "gb"])

if __name__ == "__main__":
    start()