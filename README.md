# Easy Ren'Py GUI

A template project intended to make it easier to replace the default GUI. This project has ripped out most of the gui properties so that you are left only with the defaults and simplifies styles so that they are easier to understand and modify.

The project is created for a 1920x1080 game resolution and is based off of the default game files generated for a game made with Ren'Py 7.5.3 or 8.0.3. It will also work for newer versions of Ren'Py, like 8.1.1 and 7.6.1, and may have some compatibility with older engine versions. You may adjust the dimensions in `gui.init`, but you will likely have to change many of the hardcoded style values to suit the new resolution.

## How to Use

If you would like to quickly create a GitHub repository of your own using this template, simply click GitHub's "Use this template" button in green on the repository. The resulting repository is not a fork of this repository nor connected to it, so you can then just use it like a regular repository. For more on using template repositories, see <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template/>.

Otherwise, you can use the "Code" dropdown next to the "Use this template" button and either download a ZIP of the repository or use GitHub Desktop to do so.

Once you've got the repository downloaded onto your computer, unzip it if necessary and relocate the outermost EasyRenPyGui folder (the one with the `game/` folder inside it) to your Ren'Py project folder and rename it to whatever your project name is.

Next, open `options.rpy` and change the three values at the top of the file (`config.name`, `build.name`, and `config.save_directory`) to something unique for your project.

Finally, inside the `audio/`, `fonts/`, and `images/` folders are files called `delete this.md`. These three `.md` files are included only for the purposes of ensuring those folders are added to the repository and should be deleted. You may also freely remove any file inside the `optional files/` folder that you don't need, as they are all standalone and can be removed without consequence.

You can then start the Ren'Py launcher, launch your new game template, and begin adding to and modifying it.

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

This removes the need to flip back and forth between different `.rpy` files to find the correct values, and also reduces the instances where changing one gui value can have a cascading effect changing multiple other styles across different screens.

### Structural Changes

The screens usually found in `screens.rpy` have been split off into their own folder in mostly-individual files. Some shorter or related screens have been grouped together - e.g. the `popup_screens.rpy` file contains the `confirm`, `notify`, and `skip_indicator` screens.

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

The quick_menu screen `Q.Save` and `Q.Load` buttons have been removed.

There is no navigation screen. Code which previously was found in the navigation screen is copied between the main_menu screen and the game_menu screen. These two screens have their own version of what used to be the navigation screen and thus can be modified without affecting one another. Additionally, navigation textbuttons no longer include the `size_group` property which makes them all the same size so they can be easily adapted into other containers.

### Additions

The following features not normally included in a default Ren'Py project are included in this template:

* A section called **Custom Options** in `options.rpy` with defined configuration values for several configuration options I use frequently in my own projects.
* Basic archiving code is added to `options.rpy` under the Build configuration section
* The confirm screen has been updated to allow it to be shown with only one button action, often useful for simple confirmation prompts which the player need only read and dismiss the prompt. The button text has been updated to "Confirm" and "Cancel" instead of Yes/No to facilitate this approach.

In addition, there is a folder inside `game/` called **optional files** with the following contents:

* adjust_attributes.rpy
  * This includes an Aliases class to simplify the setup of `config.adjust_attributes`.
* afm_indicator.rpy
  * Includes an auto-forward indicator screen + accompanying code. It functions like the skip indicator, but shows while the player has auto-forward activated instead of while skipping.
* confirm_action.rpy
  * Includes a custom screen action, CConfirm, which can be used to easily write confirmation prompt actions. Notably, unlike its built-in `Confirm` counterpart, if a `yes` action is not provided, the "Cancel" button will be omitted from the prompt and hitting "Confirm" will automatically dismiss the prompt.
* gallery.rpy
  * This file has a basic gallery screen setup along with template gallery definitions.
* mobile_input.rpy
  * This screen includes a custom InputValue class, `EnterInputValue`, which starts with the input disabled by default. Pressing Enter while the prompt is enabled (open for text input) will disable it again. This makes it suitable for mobile devices, where the keyboard takes up much of the screen space and needs to be dismissed.
  * An example screen using this class is also included for demonstration.
* special_labels.rpy
  * This file includes blank labels for `splashscreen` and `after_load`, which are often used in various projects.

Every file in the **optional files** folder is entirely self-contained and may be removed if it is unneeded.

## Final Notes

This template is dynamic and may grow to include other optional features or updates as they are suggested or as I think of them. At any given time, however, this template should be a suitable starting point for a new project.

## Terms of Use

You are free to clone and use this template however you wish. Credit as `Feniks` is not required but it is appreciated if you found the template useful. You can also check out my website, https://feniksdev.com/ which will refer to the template as a starting point for learning screen language.

## Like my work?

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/fen)
