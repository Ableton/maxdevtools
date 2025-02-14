# Diffing patches

## Description

A way to diff condensed representations of Max patches and Max for Live devices, so the diff is more readable when working with the version control tool [git](https://git-scm.com/). This tool also allows diffing the XML content of `.als` files, regardless of whether they are gzipped.

In a git client like Tower, this is how it looks.

Adding a new Max MIDI Effect without changes:

![Adding](add-midi-effect.png)

Removing the comments from the new MIDI Effect:

![Removing](remove-comments.png)

> :pushpin: the condensed summary shows all the patch information and connections between objects. Any objects or data that cannot be parsed will be included as raw json. The summary only shows object properties that don't have a default value.

For `.amxd` files:
* The scripts will also tell you what device type it is. 
* If a device is frozen, you will see an overview and statistics of the content frozen into the device. NOTE: We recommend never to commit frozen devices to a git repository, instead to include the dependencies as separate files.

### Why?

Readable diffs are very useful for patch code review, or for a sanity check before committing (did I really change nothing else expect removing all my debug messages and prints?).

### Using the frozen device statistics

For frozen devices, `maxdiff` reports statistics. This feature can compared to [`git diff --stat`](https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---statltwidthgtltname-widthgtltcountgt) to indicate the amount of change in a commit.

Currently, it reports the number of object instances and connections of a device in two different ways:

* Total - Counting every abstraction instance - Indicates loading time
  * This recursively counts the contents of all subpatchers and abstraction instances
* Unique - Counting abstractions once - Indicates maintainability
  * This counts the contents once of every dependency frozen into the device.

Apart from that it reports the amount of times dependencies are used.

We typically don't commit frozen devices to a repo, so the typical way to use this feature is:

1. Commit the device and its dependencies in **un**frozen state.
2. Temporarily freeze the device.
3. Run `python3 ./maxdiff/amxd_textconv.py <path/to/device.amxd>` to get the statistics or view the file in your git client.
4. Discard the freezing.

The reason this only works with frozen devices is that frozen devices unambiguously capture all dependencies.

### What does not work

Typical things you can do with text-based code that will not work with Max patches or devices:
* Resolving merge conflicts
* Staging or discarding lines or chunks

Note that `git-format-patch` (see [man](https://git-scm.com/docs/git-format-patch)) does still work, since by default it ignores the `textconv` setting.

## Installing

### Prerequisites

Requires Python 3.10 or higher to be installed, and assumes it is aliased as `python3`. For example on Mac, [Homebrew](https://brew.sh/) should automatically set this up when installing with:

```bash
brew install python
```

### Setup

1. In a `.gitattributes` file in the root of your repository, apply diff attributes for `.maxpat`, `.amxd` and `.als` files:
```text
*.maxpat              diff=maxpat
*.amxd                diff=amxd
*.als                 diff=als
```

2. To make the repository use the custom text converter scripts, add them to your local git configuration: in your `.git` folder, you'll find the `config` file. Assuming this repository is checked out in your home folder, you can add these lines:

   ```text
   [diff "maxpat"]
     textconv = python3 ~/maxdevtools/maxdiff/maxpat_textconv.py
   [diff "amxd"]
     textconv = python3 ~/maxdevtools/maxdiff/amxd_textconv.py
     binary = true
   [diff "als"]
    textconv = python3 ~/maxdevtools/maxdiff/als_textconv.py
    binary = true
   ```

3. Now `git diff` will show you changes in max patch and device files in a condensed format.

## Troubleshooting

If you see or know that a file is modified but your git interface does not show any diff, there might be an error in a maxdiff script. To verify this, you can get a summary outside of git:

* Open Terminal / Command Prompt, navigate to this repository.
* From the repository root, run the appropriate python script with your file as an argument:
  * `python3 ./maxdiff/amxd_textconv.py <path/to/your/device.amxd>` for a device, or
  * `python3 ./maxdiff/maxpat_textconv.py <path/to/your/patch.maxpat>` for an abstraction.
* If this doesn't print a patch summary, or if this throws an error, please [get in touch](CONTRIBUTING.md).

## Reporting issues and contributing

Reports and contributions are welcome, please see the [contributing guidelines](CONTRIBUTING.md).