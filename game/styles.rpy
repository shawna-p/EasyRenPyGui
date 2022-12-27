################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)



################################################################################
## GUI Configuration Variables
################################################################################
## Some choice gui values have been left in, to make them
## easier to adjust for accessibility purposes e.g. to allow
## players to change the default text font or size by rebuilding the gui.
## You may add more back if you need to adjust them, or find-and-replace
## any instances where they are used directly with their value.

# The text font for dialogue and choice menus
define gui.text_font = gui.preference("font", "DejaVuSans.ttf")
# The text font for buttons
define gui.interface_text_font = gui.preference("interface_font", "DejaVuSans.ttf")
# The default size of in-game text
define gui.text_size = gui.preference("size", 33)
# The font for character names
define gui.name_text_font = gui.preference("name_font", "DejaVuSans.ttf")
# The size for character names
define gui.name_text_size = gui.preference("name_size", 45)

## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#cccc00'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#888888'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#e0e066'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#ffffff'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#515100'
define gui.hover_muted_color = '#7a7a00'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes ########################################################

## The size of text in the game's user interface.
define gui.interface_text_size = 33

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Style Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    adjust_spacing False

style hyperlink_text:
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    xysize (None, None)
    padding (0, 0)

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    xalign 0.0
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color

style label_text is gui_text:
    size 36
    color gui.accent_color


style bar:
    ysize 38
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 38
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style slider:
    ysize 38
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize 38
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
