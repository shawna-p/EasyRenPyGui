## Adjust Attributes ###########################################################
##
## This is a special configuration value which can be used to easily create
## shorthand for layered images. This code is adapted slightly from Ren'Py Tom's
## article on the topic:
## https://patreon.renpy.org/dev-2021-04.html#adjust-attribute-example
##
## You can learn more about config.adjust_attributes here:
## https://www.renpy.org/doc/html/config.html#var-config.adjust_attributes
##
## As per usual, if you do not need it, you may freely remove this file.
##

init -100 python:

    class Aliases(object):
        """
        Expands attributes into other attributes.
        """

        def __init__(self, **aliases):

            # A map from an attribute name to a tuple of
            # attributes it expands to.
            self.aliases = { }

            for k, v in aliases.items():
                self.aliases[k] = tuple(v.split())

        def __call__(self, name):

            # The image tag
            rv = [ name[0] ]

            # The remaining attributes
            for i in name[1:]:
                ## Also remove the provided attributes, if negated
                if i.startswith("-"):
                    prefix = "-"
                    i = i[1:]
                else:
                    prefix = ""

                for attr in self.aliases.get(i, ( i, )):
                    rv.append(prefix + attr)

            # Turn the results back into a tuple
            return tuple(rv)

## A possible use case:
# define config.adjust_attributes['eileen'] = Aliases(
#     happy="eyes_happy mouth_happy",
#     concerned="eyes_concerned mouth_concerned",
# )