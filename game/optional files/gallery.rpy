## Gallery #####################################################################
##
## A basic setup for a gallery screen, using Ren'Py's built-in Gallery
## system. More information here:
## https://www.renpy.org/doc/html/rooms.html#image-gallery
##

init python:

    ## First, some constants to speed up declarations

    ## The size of gallery buttons/thumbnails
    gallery_thumb_size = (400, 225)
    ## For convenience's sake: list off all the gallery image
    ## names we're going to use in this gallery
    gallery_buttons = [
        'xia_cg_1', 'ashwin_cg_1', 'zoran_cg_1'
    ]

    ## Set up the gallery
    g = Gallery()
    g.locked_button = Transform("#333", xysize=gallery_thumb_size)

    ## And declare the various gallery images
    ## This file doesn't assume the presence of any GUI files, so I'm
    ## just using basic squares, declared as images below, but you will
    ## replace these with actual images.
    ## These use the names declared in the gallery_buttons list
    g.button("xia_cg_1")
    g.unlock_image("cg xia1")

    g.button("ashwin_cg_1")
    g.unlock_image("cg ashwin1")

    g.button("zoran_cg_1")
    g.unlock_image("cg zoran1")

## Declarations for the images used in the gallery. May or may not
## be needed if you're using Ren'Py's automatic image names.
image cg xia1 = Transform("#bd580a", xysize=(config.screen_width, config.screen_height))
image cg ashwin1 = Transform("#127151", xysize=(config.screen_width, config.screen_height))
image cg zoran1 = Transform("#8157b9", xysize=(config.screen_width, config.screen_height))

## This is just the button name + _thumb to make it easier to iterate
image xia_cg_1_thumb = Transform("#bd580a", xysize=gallery_thumb_size)
image ashwin_cg_1_thumb = Transform("#127151", xysize=gallery_thumb_size)
image zoran_cg_1_thumb = Transform("#8157b9", xysize=gallery_thumb_size)

screen gallery():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Gallery"))


    fixed:
        style_prefix 'gal'
        ## Organize the gallery images into a grid
        grid 2 2:
            for btn in gallery_buttons:
                add g.make_button(btn, "{}_thumb".format(btn))
            ## If you're not using the loop, this will look instead like:
            # add g.make_button("button_name", "button_thumbnail.png")

style gal_fixed:
    yfill True
    xsize config.screen_width-420
    align (1.0, 0.5)

style gal_grid:
    align (0.5, 0.5)
    xsize config.screen_width-420
    ysize config.screen_height-200
    spacing 50