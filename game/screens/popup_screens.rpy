
## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "#0008" # You can replace this with your own overlay image

    frame:
        has vbox

        label _(message) style "confirm_prompt"

        hbox:

            textbutton _("Confirm") action yes_action
            # Modified so you can just have a confirmation prompt
            if no_action is not None:
                textbutton _("Cancel") action no_action

    ## Right-click and escape answer "no".
    if no_action is not None:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action

style confirm_frame:
    background Frame("gui/frame.png", 60, 60, 60, 60, tile=False)
    padding (60, 60, 60, 60)
    xalign 0.5
    yalign 0.5

style confirm_vbox:
    align (0.5, 0.5)
    spacing 45

style confirm_prompt:
    xalign 0.5

style confirm_prompt_text:
    text_align 0.5
    align (0.5, 0.5)
    layout "subtitle"

style confirm_hbox:
    xalign 0.5
    spacing 150

style confirm_button:
    xalign 0.5

style confirm_button_text:
    text_align 0.5


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_hbox:
    spacing 9

style skip_frame:
    is empty
    ypos 15
    background Frame("gui/skip.png", 24, 8, 75, 8, tile=False)
    padding (24, 8, 75, 8)

style skip_text:
    size 24

style skip_triangle:
    is skip_text
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame:
    is empty
    ypos 68

    background Frame("gui/notify.png", 24, 8, 60, 8, tile=False)
    padding (24, 8, 60, 8)

style notify_text:
    size 24



