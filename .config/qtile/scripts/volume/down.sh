
VOLUME=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | tr -dc '0-9' | sed 's/^0\{1,2\}//')

wpctl set-mute @DEFAULT_AUDIO_SINK@ 0
wpctl set-volume -l 2.0 @DEFAULT_AUDIO_SINK@ 5%-

ICON="~/Dotfiles/.config/dunst/images/decrease-volume.png"
TEXT="Currently at ${VOLUME}%"
dunstify -a "Volume" -r 9993 -h int:value:"$VOLUME" -i "$ICON" "Volume" "$TEXT" -t 2000
