
## Auto indicator screen #######################################################
##
## This screen is used to indicate that auto-forward mode is in progress.
## Created by me, Feniks. You may remove this whole file if you don't need
## an auto-forward indicator screen.
##

init python:
    def auto_indicator():
        """
        A function which, when called, determines if the Auto indicator
        should be shown on-screen or not.
        """

        # Auto mode is on
        if preferences.afm_enable and not renpy.get_screen('auto_indicator'):
            renpy.show_screen('auto_indicator')
        # Auto mode is off
        elif not preferences.afm_enable and renpy.get_screen('auto_indicator'):
            renpy.hide_screen('auto_indicator')

        return

    # This adds the auto indicator to a list of overlay functions
    # so that it can automatically show the Auto indicator.
    if auto_indicator not in config.overlay_functions:
        config.overlay_functions.append(auto_indicator)

screen auto_indicator():

    zorder 100
    style_prefix "auto"

    frame:
        has hbox

        text _("Auto-Forward")

        text "▸" at auto_blink(1.0) style "skip_triangle"

## This transform is used to blink the arrows one after another.
transform auto_blink(cycle):
    alpha 0.0
    linear 0.5 alpha 1.0
    pause 0.2
    linear 0.5 alpha 0.0
    pause (cycle - .4)
    repeat

style auto_hbox:
    spacing 9

style auto_frame:
    is empty
    ypos 15
    background Frame("#0008", 24, 8, 75, 8, tile=False)
    padding (24, 8, 75, 8)

style auto_text:
    size 24

style auto_triangle:
    is auto_text
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

