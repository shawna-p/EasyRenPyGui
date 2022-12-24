# Easy Ren'Py GUI

A template project intended to make it easier to replace the default GUI. This project has ripped out most of the gui properties so that you are left only with the defaults and simplifies styles so that they are easier to understand and modify.

The project is created for a 1920x1080 game resolution. You may adjust the dimensions in `gui.init`, but you will likely have to change many of the hardcoded style values to suit the new resolution.

## How to Use

If you would like to quickly create a GitHub repository of your own using this template, simply click GitHub's "Use this template" button in green on the repository. The template is not a fork of this repository or connected to it, so you can then just use it like a regular repository. For more on using template repositories, see <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template/>.

Otherwise, you can use the "Code" dropdown next to the "Use this template" button and either download a ZIP of the repository or use GitHub Desktop to do so.

Once you've got the repository downloaded onto your computer, unzip it if necessary and relocate the outermost EasyRenPyGui folder to your Ren'Py project folder and rename it to whatever your project name is.

Finally, open `options.rpy` and change the top three values (config.name, build.name, and config.save_directory) to something unique for your project. You can then start the Ren'Py launcher and launch your new game template and begin adding to and modifying it.

## Features

### Styles

Styles have been greatly simplified not only by relocating and removing unused inheritance but also by substituting most gui values directly into the styles to make them easier to adjust. For example:

```renpy
style nvl_dialogue is say_dialogue

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
```

Has been turned into:

```renpy
# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885
```

This reduces how often it's necessary to flip back and forth between different `.rpy` files to find the correct values, and also reduces the instances where changing one gui value can have a cascading effect changing multiple other styles across different screens.

### Structural Changes

The screens usually found in `screens.rpy` have been split off into their own folder in mostly-individual files. Some shorter or related screens have been grouped together - e.g. the `popup_screens.rpy` file contains the `confirm`, `notify`, `skip_indicator`, and a new `auto_indicator` screen which functions the same as the `skip_indicator` screen but for auto-forward mode. The `auto_indicator` code may be easily removed if you don't wish to have an auto indicator.

In particular, due to the immense reduction of code in `screens.rpy` and `gui.rpy`, this project only has a single file with the remainder of the code from both files, called `styles.rpy`. Some code previously located in `options.rpy` has also been relocated to be next to the relevant screens e.g. `gui.about` is now declared in `other_screens.rpy` above the `about` screen.

You can find the default screens in the following files:

* choice_screen.rpy
  * screen choice
* dialogue_screens.rpy
  * screen say
  * screen quick_menu
  * screen nvl
    * screen nvl_dialogue
* game_menu.rpy
  * screen game_menu
* history_screen.rpy
  * screen history
* input.rpy
  * screen input
* main_menu.rpy
  * screen main_menu
* other_screens.rpy
  * screen about
  * screen help
    * screen keyboard_help
    * screen mouse_help
    * screen gamepad_help
* popup_screens.rpy
  * screen confirm
  * screen skip_indicator
  * screen auto_indicator (custom)
  * screen notify
* preferences.rpy
  * screen preferences
* save_load.rpy
  * screen save
  * screen load
  * screen file_slots

### game_menu and main_menu

The `game_menu` screen, which is normally reused across every menu screen in a default Ren'Py project, has been heavily modified to only require a title and does not `transclude` contents. Thus it is only useful insofar as it includes the contents of the `navigation` screen (and the screen title).

This change means that most screens require a container of some kind inside which to organize their contents, rather than the containers provided by the default `game_menu` screen. This is intended to improve the flexibility of various menu screens, which no longer need to rely on the `game_menu` screen to organize their contents.

The `main_menu` screen also includes its own copy of what was originally `screen navigation`, so that changing the main menu will not affect every other menu screen. `screen navigation` has been entirely omitted and instead `game_menu` largely takes that role for menu screens which aren't the main menu.

### Omissions

All of the code which changes styles for variants, such as the "touch" variant of the quick_menu screen and the gui value updates for small screens, has been omitted. Thus, aside from some minor checks like the preferences not including windowed/fullscreen options, mobile builds will look identical to their desktop counterpart. The `gui/phone` folder has also been removed in accordance with this.

The history screen is set up for variable-height entries only and differs the greatest from its default counterpart, using an `hbox` instead of positioning and labels. I have no plans to include the ability to have a fixed-height history log in this template, though you are of course free to adapt it to your own needs; this template is intended to be easy to modify.

### Additions

The following features are included in this template:

* An auto-forward indicator, which displays similarly to the skip indicator while the player has auto-forward activated
* A special_labels.rpy file with blank labels for `splashscreen` and `after_load`, which are often used in various projects. You may delete this file if you do not use these labels, or relocate the code elsewhere.
* A section called **Custom Options** in `options.rpy` with defined configuration values for several configuration options I use frequently in my own projects.
* Basic archiving code is added to `options.rpy` under the Build configuration section

I have not included any further code for screens not included with Ren'Py by default, such as templates for gallery screens or accessibility options, though I may consider adding those down the line if it is requested.

## Terms of Use

You are free to clone and use this template however you wish. Credit as `Feniks` is not required but it is appreciated if you found the template useful. You can also check out my website, https://feniksdev.com/ which will refer to the template as a starting point for learning screen language.
