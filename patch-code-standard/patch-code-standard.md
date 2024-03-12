# Ableton Patch Code Standard for Max Devices

The patch code standard that Ableton uses in the Max devices that come bundled with Live 12 and higher.

## Philosophy
To ensure that our devices continue to work, they need to be easy to maintain, and therefore easy to understand. This also makes them easy to copy from for our users.

Using a single approach to patching across all our devices means internal and external readers need to become accustomed to our style only once.

That is why we use a patch code standard, that optimizes for being easy to read. Our built-in devices[^1] demonstrate this standard.

## Context
General thoughts about the scope and intention of this document:

* For now these guidelines are only applied to the devices that are built into Live and to the [Building Max Devices Pack](https://www.ableton.com/en/packs/building-max-devices/). In the future we might also apply them to Packs.
* These guidelines apply only to devices we publish. When prototyping, none of this applies, everything goes.
* Standards are subjective. This standard is based on the opinions of various experienced Max users.
* None of these guidelines are absolute, they can be deviated from if there is a good reason.
* Max is an environment for experimentation and invention. Our patches, end-user products that need long-term support, are not typical uses of Max. That is why these guidelines may be more strict than for most use cases of Max.
* We try to keep this standard as brief as possible.

## Testability
To make sure we don't break existing features when we make changes, we use the following testing criteria:

* Devices come with a test set which uses all features of a device. This test is used for regression testing, i.e. when refactoring or adding features, it allows the developer to guarantee that existing functionality does not change by comparing the sound of the published version (the baseline) with the new version.
* After any significant change of the patch code, we check if the test set still works the same.
* Whenever addressing a bug, we first reproduce it in the test set, then fix it, then verify in the test set that it is fixed.
* Devices come with a test set which is an example of a typical heavy use of one or more copies of a device so that our CPU measuring tools can determine the average and peak usage. After any significant change of the patch code, we test if the CPU usage went up.
* The load time of a device is monitored by manual testing and by counting objects, including in duplicate and nested abstractions, and keeping the total as low as possible.
* Before a device is published, it has to adhere to [these user-facing guidelines](../m4l-production-guidelines/m4l-production-guidelines.md).

## Version control and file management
To make it easy to collaborate, we manage our patch and dependency versions with [git](https://git-scm.com/), using the following approach:

* We never store frozen devices. The device code and all its dependencies live unfrozen in their repository.
* There are never files in a general Max search path, such as the `~/Documents/Max 8/Max for Live Devices/` folder. In the unlikely event we unfreeze a device, we move any files away from this folder.
* Dependencies are found by Max by a) being next to the device file, b) by having the device use a relative project [Development Path Type](https://docs.cycling74.com/max8/vignettes/projects_settings), or c) by adding a local entry in the global Max [File Preferences](https://docs.cycling74.com/max8/vignettes/file_preferences_window?q=File%20Preferences).
* We follow the same pattern as other code: development happens on a branch. When done, a PR is created, the branch is reviewed and merged and the branch is then deleted.
* All dependencies of the device are in the same repository. i.e. nothing in the device refers to files outside of the repository unless this is explicitly mentioned. 
* Dependencies are only included in the repository once. If dependencies are used by multiple devices, they live in a shared folder.
* Commits contain isolated changes as much as possible so they are easy to review individually.
* Commits change as little as possible, so they are easy to review using [maxdiff](../maxdiff).
* Every commit leaves the device in a working state, as verified by its test set.
* Don't leave unused code in the patch. Code from previous versions can always be brought back with git.

## Code review
All patch code changes are reviewed by another experienced Max developer before being published.

## Patch code
Below is the approach we use to format and structure Max patches consistently:

### General guidelines
* The more complex the functionality of a device, the more important that its patch is as simple as possible. 
* Simple here means easy to understand, not necessarily easy to build.
* Don't have too many objects in one patcher.
* Don’t over-abstract.
* Only make code reusable if it is actually being reused.
* Only use an abstraction that is bundled with Max if it does exactly what you need and not more. If you need something slightly different, de-encapsulate or change it.
* Don't deviate from Max' defaults.
* Use the latest mature features of Max where applicable.
* If you're missing a feature or run into a bug in Max, contact C74 and postpone the functionality you want to build. Don't use a workaround unless it is well-understood and appropriate to share.

### Functionality
* Make sure there can be no audio clicks when changing parameters. For example, check all places where events go to DSP and see if they need to be faded (e.g. using `[$1 5]` > `[line~]`).
* Persistent ids are only used when necessary, so only when storing a mapping. Turn them off for all `[live.object]`s and `[live.observer]`s that are just intermediates, among others because this prevents creating unnecessary undos.
* [Any logic related to UI updates doesn't happen in the scheduler thread](no-ui-updates-in-scheduler/).
* For polyphonic patches, `[poly~]`s only contain the calculations that are different per voice, e.g. conversions and smoothing that are the same for all voices can be done outside. This doesn't apply when `[poly~]` is used for different purposes, e.g. to resample parts of the audio chain or muting DSP.
* For muting parts of DSP processing, when there are no other demands, using `[poly~]` is preferable over `[mute~]` or using `[pcontrol]`. Even though using `[mute~]` would be easier to read, `[poly~]` has Cycling '74's preference.
* For multichannel/polyphonic processing, if it is possible to use the `[mc.x]` features, this is preferable over using `[poly~ ]`.
* Going from DSP to events is only done when there is no way things can stay in DSP.
* Be aware that if there are parameters in repeated abstractions, including in bpatchers, those parameters are auto-renamed by Max. This can be taken addressed in the View -> Parameters window.
* For parameter objects that trigger expensive calculations but do not have to be applied in exact sync with other events, `defer automation output` needs to be enabled.

### Initialization
* There is no need to use a single `[live.thisdevice]` or `[loadbang]` in your patch, except if the order of initialization is important, similar to the criterium for when to use `[trigger]`.
* When choosing between `[loadbang]` and `[live.thisdevice]`, choose `[live.thisdevice]` only when the initialization actually depends on the connection with Live, i.e. live API queries or initial parameter values. When that is not the case, use `[loadbang]`, which fires when all patch code is loaded but before the connection with Live is working.
* There shouldn't be data saved in the patch that is also stored in the Live set (parameter data) or depend fully on Live (like sample rate). This is not always possible, for example the points of the function object or the sample rate of live.scope~ are always stored with the patch.
* Devices are published in their default state. They need to be committed in the state they have after freshly being dragged into a Live set. This also prevents unneeded diffs.

### Comments and prints
* If it is clear what a patch does, it doesn't need comments. Comments can easily go out of date.
* Comments should describe intent or reason, not action. e.g. not "loadbang to 6.283", but "Initialize to 2 x PI to ensure the sine completes a full cycle". Ideally, code should tell the "what" and "how", comments should tell the "why" if that is not clear from the code.
* In devices that are not aimed primarily at learning Max for Live, basics of Max for Live don't need to be explained, e.g. "Audio coming from Live" next to `[plugin~]` is not needed.
* If a patch is suboptimal but can't be changed because of backward compatibility, add a comment saying so.
* All regular Max comments have theme-following colors, otherwise they're not readable in the dark themes. Note: this is only the default for live.comment objects, so for normal comments this needs to be changed.
* Optional: all inlets and outlets of subpatchers, including in `[poly~]`, have their `comment` attribute set according to [this naming scheme](describing-in-and-outlets/).
* There are no comment objects that repeat the in/outlet comment texts.
* Optional: comment texts are checked by a native speaker.

### Object colors, fonts and sizes
* For objects, no color and font information is saved in the patch, as when [setting the default in the Inspector](https://docs.cycling74.com/max8/vignettes/attributes_inspecting#Working_with_Attribute_Default_Values).
* For patchers, no default color and font information is set in the patch, as can be controlled in the [patcher inspector](https://docs.cycling74.com/max8/vignettes/patcher_inspector).
* Grid size: 8 x 8 in a Max for Live root patch, 15 x 15 in subpatchers and abstractions.
* All non-UI objects have a default font and color, resulting in Arial 10 bold in root and Arial 12 regular in subpatchers.
* Patcher background / grid / default font settings are all set to default.
* Patches have Show Grid on Open and Snap to Grid on Open set to 0 and Snap to Objects on Open set to 1, which are the Max defaults
* Patchers contain no unused styles.
* Patchers uses no subpatcher templates.
* Objects are not longer than their content needs except if this is required to better align patch cords.
* Things added and laid out in presentation view (e.g. panels) have a related position in patching view. For example, neighboring UI elements they are presented in proximity of each other, and in the same order as in the UI.
* Optional: standardize the vertical spacing between objects: 1 grid size if only connected with vertical patch cords, 3 grid sizes otherwise.

## Patch cords
* By default, patch cords are not segmented. There can be exceptions, for example if they go back up or travel a long distance across the patch. [Here is the reasoning](segmented-patch-cords/).
* All objects have integer positions.
* For patch cords that go straight down, out- and inlets are aligned to that the connections travel purely vertical.
* If there are any patch cords vertically misaligned by 1 pixel, position rounding may have moved one of the two connected objects different from the other.
* We try to limit alternative patch cord colors, but these can be used if they add meaning that cannot conveniently be conveyed otherwise.
* Never rely on right-to-left execution order of patch cords. If execution order matters, use a trigger object instead.
* If execution order does *not* matter, don't use a trigger object.
* For send/receive pairs or other invisible connections like with `[v]` or a `[coll]` name, always use the `---` prefix to make them local to the device.

## Subpatchers and abstractions
* There are no subpatchers with the same name as abstractions or externals.
* There are no abstractions with the same name as any other commonly used abstraction, because dependency caching might replace the abstraction with another.
* There are no abstractions with the same name as an external.
* Externals work on Mac, Windows and Push 3 Linux.
* (Sub)patcher windows are not much larger than the patch they contain.
* (Sub)patcher windows ideally fit within 1400 x 807 pixels (the resolution of a 13" MacBook with a default-sized dock and a menu bar), and they are not less than 24 pixels (mac menu) from the top of the screen.
* With parameter objects in a bpatcher, always edit parameter properties directly in the bpatcher, not from the parameter list available via menu > View > Parameters, unless multiple instances of the same bpatcher are in use.
* With multiple instances of bpatchers that contain parameter objects, parameter names need to be edited in the list available via menu > View > Parameters. Be aware that names might revert back if the bpatcher is temporarily removed and the top level device is subsequently saved.
* The Push banks subpatcher is always called [p PushBanks] and is colored the same way.
* Optional: we add [colors to the box borders of objects that contain more patching or code](object-border-colors/).

### Freezing and dependencies
* Devices are only frozen when distributing, because of the risk involved in unfreezing.
* Frozen devices do not contain externals or abstractions that are bundled with Max.
* Unfreezing a device does not result in a `discarded` folder.
* Ideally it should never be necessary to unfreeze a device while developing, instead you should work on the unfrozen source in the git repo.
* Whenever it's necessary to unfreeze something, after you're done, make sure to remove everything from the `~/Documents/Max 8/Max for Live Devices/` folder to reduce the risk of editing the wrong dependency.
* Don't include any dependencies in the device projects. It has a risk of leaving files in the device that it no longer uses. Since everything is in the same repository, and the source folder is in the Max search path, Max should be able to find only one copy of every dependency in all of its search paths.
* For embedded bpatchers, make sure the original abstractions used before the embed are deleted to prevent the risk from these obsolete abstractions being edited instead of the embedded ones.
* Optional: to help with version control and working on a patch with several people at once, large subpatchers or embedded bpatchers can be saved as abstractions instead, even though they are used only once. Note though that this conflicts with the wish to use abstractions only when code is actually re-used, so this should only be done when there is a good reason.

### Cleaning up
* Devices don't contain `[dac~]`s or `[adc~]`s.
* There are no `[print]`s in the device.
* In final versions of devices, ideally there are no comments with "TODO" in them, todos should be done.
* There is no unused patch code or out-of-date comment in the device. Keeping something around for future use is not needed since we work in git where we can always get back previous code.
* When opening the device for editing but not changing anything, closing it should not prompt a save dialog. This means e.g. that there should not be message boxes that get their content changed when the device is used. Exception: when live.banks is in use and banks are allocated dynamically.

### Naming (subpatchers, scripting names, etc)
* Use [CamelCase](https://en.wikipedia.org/wiki/Camel_case) (not snake_case).
* Subpatcher and script file names start upper case: InputSelector (not inputSelector).
* When the names contains abbreviations, capitalize only the first letter: FlowLcd, MpeMonitor (not FlowLCD, MPEMonitor).

## Text-based code
This does not cover general best practices for text-based code, as there is a lot of information available about this already. These are the standards specific to Ableton's projects.

### Javascript in Max
* Use `"use strict";`.
* Use two-space indentation.
* Have a newline at the end of each file.
* Prevent trailing spaces.

## See also

* Some inspiration for this guide comes from the [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) and the [Go style](https://google.github.io/styleguide/go/guide.html) guide.
* These guidelines and some more detailed choices are demonstrated in the [Building Max Devices](https://www.ableton.com/en/packs/building-max-devices/) pack and Live's built-in Max devices.
* Some background about the science of readability and simplicity:
	* [The Source of Readability](https://loup-vaillant.fr/articles/source-of-readability)
	* [Don't be clever](https://stitcher.io/blog/dont-be-clever)
	* [Connascence](https://connascence.io/)
	* [The Grand Unified Theory of Software Design by Jim Weirich](https://vimeo.com/10837903) (video)
	* [The Grug Brained Developer](https://grugbrain.dev/) (or its more readable [common english translation](https://reidjs.github.io/grug-dev-translation/)).

[^1]: All except the DS devices, which are scheduled for a different update.
