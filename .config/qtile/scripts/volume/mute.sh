
VOLUME=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | tr -dc '0-9' | sed 's/^0\{1,2\}//')

wpctl set-mute @DEFAULT_AUDIO_SINK@ 0

ICON="~/Dotfiles/.config/dunst/images/mute-volume.png"
TEXT="Currently Muted"
dunstify -a "Volume" -r 9993 -h int:value:"$VOLUME" -i "$ICON" "Volume" "$TEXT" -t 2000
