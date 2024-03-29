# 202 Strats
202 strat collection where my inputs are recorded into TAS files.  
Small warning that the TAS files will look very weird because of a combination of InputHistory trying to convert RTA to TAS input poorly, my binds causing a bunch of useless inputs to show up, and poorly stitched segment recordings.

## Files
**202 folder**: recorded strats per chapter with notes on cues or things I focus on, and some chapters are split into multiple files on rtm or s&q

**202.tas**: combines all files together into a fullgame 202 run with menuing

**SauceDispenser.py**: makes a copy of tas files into 202_sauce folder that have all non-sauce comments removed so you can just press fast forward to next comment to receive sauce

**WatchChapter.tas**: lets you choose a chapter to watch from beginning to end and logs the chapter's file time, which is useful for chapters split into multiple files

## Why
I needed a way to keep track of my 202 strats/notes for memory purposes and the initial approach was to record checkpoint runs, put them together into IL videos with notes in the description, then add it to a [youtube playlist](https://www.youtube.com/playlist?list=PLe4H4cset3iFk3nKlbb8tro8Sx7h7TaCe). I recently found that InputHistory has an experimental way of recording human inputs to TAS files, so now I'm recording all of my strats into TAS files. I plan on recording higher quality videos of each chapter's strats using kkapture once they're finalized, then replacing each video in the youtube playlist.

#### TAS files approach
+ it's so cool
+ can review strats within the game without getting hands tired
+ perfect playback since it's literally just running from the game
+ TAS encode with kkapture is way better quality than how I recorded RTA
+ modifying strats or fixing my execution mistakes in recording is much easier than rerecording a checkpoint run
+ having a TAS file of most recent strats while they're volatile in strat iteration process is nice
- even after making some modifications, InputHistory mod is very inconvenient to use and TAS output occasionally requires manual fixes
- making adjustments to small segments can sometimes be hard because it requires starting and stopping input recording between simple states
- recording inputs to make TAS files, maintaining TAS files of strats, reuploading videos to the playlist is a lot more work

#### Checkpoint run video approach
+ contains input display in the recording
+ much simpler to do overall
- can take a lot of attempts to get clean segments that demonstrate the strat appropriately
- need to worry about quality of recording and it's doomed if I randomly lose some frames
- not nearly as cool as having TAS files with my inputs recorded
