
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("History"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0

        has vbox

        style_prefix "history"

        for h in _history_list:

            frame:
                has hbox
                if h.who:
                    label h.who style 'history_name':
                        substitute False
                        ## Take the color of the who text
                        ## from the Character, if set
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        xsize 200   # this number and the null width
                                    # number should be the same
                else:
                    null width 200

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_frame:
    xsize 1400
    ysize None
    background None

style history_hbox:
    spacing 20

style history_vbox:
    spacing 20

style history_name:
    xalign 1.0

style history_name_text:
    textalign 1.0
    align (1.0, 0.0)
    color '#f93c3e'

style history_text:
    textalign 0.0

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
