# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# from dotenv import load_dotenv
# load_dotenv()
#

import os
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import subprocess
# from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "BackSpace", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "q", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),
    Key([mod, "shift"], "t", lazy.spawn("telegram-desktop"), desc="Spawn telegram"),
    Key([mod], "w", lazy.spawn("firefox"), desc="Spawn firefox"),
    Key([mod], "f", lazy.spawn("dolphin"), desc="Spawn File Manager"),

    # lock screen
    Key([mod, "shift"], "l", lazy.spawn("betterlockscreen -l"), desc="lock screen"),
    # flameshot screenshot taker
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),


    # volume related 
    Key([mod], "F3", lazy.spawn('sh -c ~/.config/qtile/scripts/volume/up.sh'), desc="increase volume "),
    Key([mod], "F2", lazy.spawn('sh -c ~/.config/qtile/scripts/volume/down.sh'), desc="decrease volume"),
    Key([mod], "F4", lazy.spawn('sh -c ~/.config/qtile/scripts/volume/mute.sh'), desc="mute volume "),

    # rofi related keys
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Spawn a rofi command using a prompt widget"),
    Key([mod, "shift"], "h", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"), desc="clipboard"),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc="show all windows"),
    Key([mod, "shift"], "c", lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"), desc="calculator"),
    Key([mod], "e", lazy.spawn("rofi -modi emoji -show emoji"), desc="emoji"),
]


def Search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")

def lock():
    qtile.cmd_spawn("betterlockscreen -l")

def Wifi():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/rofi-wifi-menu")

def Bluetooth():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/rofi-bluetooth-menu")
# groups = [Group(i) for i in '1234']
# groups = [Group(f"{i+1}", label="󰏃") for i in range(5)]
groups = [
    Group(
        '1',
        label="󰈹",
        matches=[
            Match(wm_class="firefox"),
            ],
        layout="column"
    ),
    Group('2', label="", layout="column", matches=[Match(wm_class="kitty")]),
    Group('3', label="", layout="column", matches=[Match(wm_class="telegram-desktop")]),
    Group('4', label="", layout="column", matches=[Match(wm_class="dolphin")]),
    Group('5', label="󰒓", layout="column", matches=[Match(wm_class="Bitwarden")]),
#     Group('6', label="六", layout="monadtall"),
#     Group('7', label="七", layout="monadtall"),
#     Group('8', label="八", layout="monadtall"),
#     Group('9', label="九", layout="monadtall"),
#     Group('0', label="十", layout="max", matches=[Match(wm_class=["mpv"])])
]

from libqtile.widget.textbox import TextBox


def left_half_circle(fg_color, bg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=22,
        foreground=fg_color,
        background=bg_color,
        padding=0)


def right_half_circle(fg_color, bg_color):
    return TextBox(
        text='\uE0B4',
        fontsize=23,
        background=bg_color,
        foreground=fg_color,
        padding=0)


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\ue0ba',
        padding=0,
        margin=0,
        fontsize=40,
        background=bg_color,
        foreground=fg_color)

def lower_right_triangle(bg_color, fg_color):
    return TextBox(
            text='\ue0b8',
            padding=0,
            margin=0,
            fontsize=40,
            background=bg_color,
            foreground=fg_color)

def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=25,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=35,
        background=bg_color,
        foreground=fg_color)




for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=["#add8e6", "#add8e6"], border_width=2, margin=2, rounded_borders=1),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=["#add8e6", "#add8e6"], border_width=2, margin=2, rounded_borders=1),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(border_focus=["#add8e6", "#add8e6"], border_width=2, margin=2, rounded_borders=1)
]

#colors for the bar
def init_colors():
    return [["#D8DEE9", "#D8DEE9"], # color 0
            ["#2E3440", "#2E3440"], # color 1
            ["#4C566A", "#4C566A"], # color 2
            ["#A3BE8C", "#A3BE8C"], # color 3
            ["#8FBCBB", "#8FBCBB"], # color 4
            ["#EBCB8B", "#EBCB8B"], # color 5
            ["#BF616A", "#BF616A"], # color 6
            ["#81A1C1", "#81A1C1"], # color 7
            ["#B48EAD", "#B48EAD"], # color 8
            ["#D08770", "#D08770"]] # color 9


colors = init_colors()
#colors for the bar

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=12,
    padding=5,
    foreground=colors[0],
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                # TextBox(text='', foreground=colors[9], fontsize=16),
                widget.Spacer(background=colors[0], length=3),
                left_half_circle(colors[2], colors[0]),
                widget.Spacer(background=colors[2], length=3),
                widget.Image(filename='~/.config/qtile/assets/happy.png'),

                widget.Spacer(background=colors[2], length=5),

                widget.GroupBox(highlight_method="line",
                                active=colors[9],
                                block_highlight_text_color=colors[4],
                                urgent_border=colors[4],
                                urgent_text=colors[4]),

                lower_left_triangle(colors[2], colors[9]),
                widget.CurrentLayout(background = colors[9],  margin=0, padding=2),
                widget.CurrentLayoutIcon(background=colors[9], ),
                lower_left_triangle(colors[9], colors[1]),

                # right_arrow(colors[1], colors[2]),
                widget.TaskList(
                    padding_x=1,
                    background=colors[1],
                    border=colors[9],
                    highlight_method="block",
                    max_title_width=200,
                    spacing=10,
                    fontsize=10,
                    font="ComicShannsMono Nerd Font Regular",
                    unfocused_border=colors[2],
                    # opacity=0.8,
                    txt_floating="🗗 ",
                    txt_maximized="🗖 ",
                    txt_minimized="🗕 ",
                    urgent_border=colors[1]
                ),

                # arrow_left,
                # left_arrow(colors[1], colors[7]),
                # left_half_circle(colors[7], colors[1]),
                # widget.Wallpaper(directory='~/Pictures/wallpapers/',
                #                  background=colors[7],
                #                  foreground=colors[0],
                #                  label="Wallpaper",
                #                  wallpaper="~/Pictures/wallpapers/astronut-destroy.jpg"
                #                  # random_selection=True,
                #                  ),
                # right_half_circle(colors[7], colors[1]),

                # # left_arrow(colors[7], colors[0]),
                #
                # widget.CheckUpdates(background=colors[0],
                #                     foreground=colors[1],
                #                     initial_text="Checking Updates",
                #                     colour_no_updates=colors[8],
                #                     no_update_string="Updates: 0",
                #                     fmt="updates: {}",
                #                     display_format="Updates: {}",
                #                     update_interval=1000,
                #                     ),
                #

                left_half_circle(colors[9], colors[1]),
                widget.Clock(
                        format=" %I:%M %p %a %d",
                        background=colors[9],
                        foreground=colors[0],
                        font="ComicShannsMono Nerd Font Bold"
                        ),

                widget.Spacer(background=colors[9], length=4),
                lower_right_triangle(colors[1], colors[9]),
                widget.Spacer(background=colors[1], length=7),

                # SEARCH LOGO
                widget.Image(
                    filename='~/.config/qtile/assets/search.png',
                    margin=2,
                    background=colors[1],
                    mouse_callbacks={"Button1": Search},
                ),
                widget.TextBox(
                    fmt='Search',
                    background=colors[1],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    mouse_callbacks={"Button1": Search},
                ),

                widget.Spacer(background=colors[1], length=7),
                lower_left_triangle(colors[1], colors[9]),
                widget.Spacer(background=colors[9], length=7),

                # updates widget
                widget.CheckUpdates(background=colors[9],
                                    display_format='Updates: {updates}  ',
                                    font="JetBrains Mono Nerd Font Bold",
                                    initial_text="Checking Updates",
                                    colour_no_updates=colors[0],
                                    no_update_string="Updates: 0  ",
                                    update_interval=1000,
                                    ),

                right_half_circle(colors[9], colors[1]),


                # spacer to make SEARCH LOGO in middle
                widget.Spacer(background=colors[1], length=bar.STRETCH),

                # left_half_circle(colors[0], colors[1]),
                lower_left_triangle(colors[1], colors[2]),
                widget.Net(
                        format='󰀂   {up}  {down}',
                        background=colors[2],
                        font="JetBrains Mono Bold"
                        ),

                lower_left_triangle(colors[2], colors[9]),

                widget.Wlan(
                    format='󱚽 {essid} {percent:2.0%}',
                    background=colors[9],
                    mouse_callbacks={"Button1": Wifi},
                ),
                # right_half_circle(colors[0], colors[1]),
                lower_left_triangle(colors[9], colors[2]),

                # left_arrow(colors[0], colors[3]),
                # widget.Spacer(background=colors[1], length=2),

                # left_half_circle(colors[3], colors[1]),
                widget.OpenWeather(
                    location="mumbai",
                    background=colors[2],
                    format='{location_city}:{temp}  {icon}',
                    app_key=os.environ.get('APIKEY'),
                ),
                # right_half_circle(colors[2], colors[1]),

                # lower_left_triangle(colors[2], colors[9]),

                # widget.Spacer(background=colors[1], length=2),

                # left_arrow(colors[3], colors[9]),
                # left_half_circle(colors[9], colors[1]),
                # right_half_circle(colors[9], colors[1]),

                # widget.Wallpaper(
                #         directory='~/.config/qtile/wallpapers',
                #         background=colors[9],
                #         wallpaper="~/.config/qtile/wallpapers/ds-0.jpg",
                #         label="wallpaper  ",
                #         option="stretch",
                #         ),
                #
                # lower_left_triangle(colors[9], colors[2]),

                # widget.Spacer(background=colors[1], length=2),

                # widget.Battery(),
                # left_arrow(colors[9], colors[6]),
                # lower_left_triangle(colors[6], colors[1]),
                lower_left_triangle(colors[2], colors[9]),
                widget.Bluetooth(
                    default_show_battery=True,
                    default_text=' {connected_devices} ',
                    format=' {percentage} {icon}',
                    background=colors[9],
                    mouse_callbacks={"Button1": Bluetooth}
                ),

                lower_left_triangle(colors[9], colors[2]),

                widget.Image(
                    filename='~/.config/qtile/assets/shutdown.png',
                    background=colors[2],
                    mouse_callbacks={"Button1":power},
                ),
                # widget.Spacer(background=colors[6], length=10),
                right_half_circle(colors[2], colors[0]),

                widget.Spacer(background=colors[0], length=3),

            ],
            # define bar height
            22,
            border_width=[1, 0, 2, 0],  # Draw top and bottom borders
            border_color=["#4c566a", "#4c566a", "#add8e6", "#add8e6"],  # Borders are lightblue
            background="#4c566a",
            foreground="#d8dee9"
            # opacity=0.5,


        ),
            # set static wallpaper
            wallpaper = '~/.config/qtile/wallpapers/ds-2.jpg',
            # set wallpaper mode to 'fill' or 'stretch'
            wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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
