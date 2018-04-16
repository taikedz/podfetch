# PodFetch : Bulk Download From Feeds and Sites

An extensible tool for downloading podcasts' media artifacts - or any part you're interested in.

## Commands

Initialize a new podcast configuration in the local directory

	podfecth init URL

Set preferences: `MEDIAPREF` determines what the preferred format should be where multiple are available ; `NAMEPREF` specifies the naming pattern (see Naming Patterns below); `SHORTNAME` is the short name of the podcast for quick reference.

	podfetch pref DIR [-m MEDIAPREF] [-n NAMEPREF] [-s SHORTNAME] [-t {true|false}]

Download all "unread" items in the podcast directory, or the specified episodes; as each is succesfully downloaded, mark the item as "read". Preferences can be adjusted by specifying them directly, with the same format as for the `pref` command. Changes to the preferences are for the imediate run only, and do not affect the defaults set with `pref`

	podfetch download DIR [PREFS ...] [EPISODEID ...]

Mark all episodes, or the specified episodes, in the database as being "read" or "unread".

	podfecth mark {read | unread} DIR [EPISODEID ...]

List read, unread or all episodes; or list media formats supported by the specific podcast module

	podfetch list {read | unread | all | formats} DIR

## Naming Patterns

### Properties

Any podcast should have the following properties:

* URL - where the main page for the podcast can be found, from which the podcast-specific module derives a list of episodes
* Podcast Name : a string giving the name of the podcast
* Episode Identifier : a short episode identifier, ususally numerical, but sometimes a string of season number and episode number, or just a date.
* Publishing date : the date the episode was published - typically `YYYY-MM-DD` , though sometimes with a time portion in which case `YYYY-MM-DD-hh:mm:ss` would be usual.

Any podcast is assumed to be able to provide the following additional properties:

* Podcast Shortname : a short name for the podcast
* Episode name : optional title of the episode

### Pattern

By default, an episode file name pattern would be generated using the podcast shortname, and episode identifier (pattern `$s-$i`). It is possible however to specify a different pattern:

* `$n` - the podcast full name
* `$s` - the podcast short name
* `$i` - the episode identifier
* `$e` - the episode full name
* `$d` - the episode date

For example, to generate a file name pattern using the podcast full name, followed by the word `episode` and the identifier, specify a mediaspec like so

    podfetch pref -m '$e episode $i'


## Media priority preference

Podcasts publish in various media formats - MP3, OGG, Theora, MOV, YouTube ... Use the `podfetch list formats DIR` command to list the modes for the supported podcast-specific module.

## Podcast Engine

PodFetch itself takes care of managing configuration and lists ; individual podcasts are supported by writing extension modules.
