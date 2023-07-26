## Mobile Input ################################################################
##
## This is a custom InputValue which does not begin as selected/ready for
## input and requires an action to be enabled. Pressing the Enter button
## will disable the input again.
##
## This makes it a good choice for most custom input screens, particularly
## on mobile devices where the keyboard can take up most of the screen space.
##
## As per usual, this file may be removed without consequence.
##
## Read more about InputValue here:
## https://www.renpy.org/doc/html/screen_python.html#inputvalue
##
init python:

    class EnterInputValue(FieldInputValue):
        """
        Subclass of InputValue which allows the Enter key to dismiss
        the input button. Does not begin as selected (so, on mobile the
        keyboard won't immediately appear).
        """

        def __init__(self, object, field, default=False):
            self.object = object
            self.field = field

            self.default = default

        def enter(self):
            """Disable this input when the user presses Enter."""
            renpy.run(self.Disable())
            raise renpy.IgnoreEvent()

default demo_name = "Feniks"

## An example screen using EnterInputValue
screen name_input_screen():

    ## The "object" here is `store` since it's a regular store variable.
    ## If the variable was persistent.name, it would use `persistent` instead.
    default name_input = EnterInputValue(store, 'demo_name')

    add "#601249bb"

    vbox:
        align (0.5, 0.5)
        spacing 25
        button:
            background "#000b"
            hover_background "#0003"
            # Ensure you can type without needing to hover this button
            key_events True
            # Enable the input
            action name_input.Toggle()
            has hbox
            spacing 25
            text "Name:"
            # The actual input, which uses the EnterInputValue earlier
            input value name_input

        textbutton "Done" action Return() xalign 0.5