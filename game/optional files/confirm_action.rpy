## Custom Confirm Action #######################################################
##
## This file contains an action similar to the Confirm screen action which
## it can be used for information and confirmation prompts.
## It can be removed if unneeded. In order to work, it requires that
## `no_action=None` on the confirm screen so that a second action is optional
## (this is the case by default for this template).
## You may remove this file without consequence.
## See the original Confirm action here:
## https://www.renpy.org/doc/html/screen_actions.html#Confirm
##
## It has three main use cases:
## 1) CConfirm("You haven't unlocked this image yet.")
##      This shows a prompt to the user with the provided text and a
##      "Confirm" button to dismiss the prompt. There is no "Cancel" button.
## 2) CConfirm("Purchase flower? ($10)", SetVariable('money', money-10))
##      This shows a prompt with Confirm and Cancel buttons. The Confirm
##      button dismisses the prompt and executes the action or list of
##      actions provided after the prompt, and Cancel hides the prompt without
##      executing any other actions.
## 3) CConfirm("Go to the next chapter?", yes=Jump("chapter2"), no=MainMenu())
##      This shows a prompt with Confirm and Cancel buttons. Clicking either
##      button will dismiss the prompt in addition to performing the provided
##      yes/no action.
##

init python:

    class CConfirm(Show):
        """
        A class which makes it easy to show simple confirmation prompts
        to the player.

        It also sets the default value of confirm_selected to True rather
        than False.
        """
        def __init__(self, prompt, yes=None, no=None, confirm_selected=True,
                *args, **kwargs):

            if config.confirm_screen and renpy.has_screen('confirm'):
                screen = "confirm"
            elif renpy.has_screen("yesno_prompt"):
                screen = "yesno_prompt"
            else:
                screen = None

            # Just a prompt; this only gets a Confirm button which
            # dismisses the prompt.
            if yes is None:
                yes = Hide(screen, config.exit_yesno_transition)
                no = None
            else:
                # All provided actions should hide the confirm screen
                # after they are clicked
                if isinstance(yes, list):
                    yes.insert(0, Hide(screen, config.exit_yesno_transition))
                elif yes != Hide(screen, config.exit_yesno_transition):
                    yes = [Hide(screen, config.exit_yesno_transition), yes]

                # Has both buttons, but "Cancel" should just hide the prompt
                if no is None:
                    no = Hide(screen, config.exit_yesno_transition)
                elif no is not None:
                    if isinstance(no, list):
                        no.insert(0, Hide(screen, config.exit_yesno_transition))
                    elif no != Hide(screen, config.exit_yesno_transition):
                        no = [Hide(screen, config.exit_yesno_transition), no]

            self.prompt = prompt
            self.yes = yes
            self.no = no
            self.confirm_selected = confirm_selected
            self.screen = screen

            super(CConfirm, self).__init__(screen, config.exit_yesno_transition,
                *args, message=self.prompt, yes_action=self.yes,
                no_action=self.no, **kwargs)

        def get_sensitive(self):
            if self.yes is None:
                return False

            return renpy.is_sensitive(self.yes)

        def get_selected(self):
            return renpy.is_selected(self.yes)

        def get_tooltip(self):
            return renpy.display.behavior.get_tooltip(self.yes)

        def __call__(self):

            if self.screen is None:
                return Confirm(self.prompt, self.yes, self.no, self.confirm_selected)()
            elif self.confirm_selected or not self.get_selected():
                return super(CConfirm, self).__call__()
            else:
                return renpy.run(self.yes)