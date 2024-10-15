# gmv2bin - Python Version

A version of [Mercury's "gmv2bin" conversion tool](https://intheshadeofawave.blogspot.com/p/hacking-tools.html#gmv2bin), which converts a movie recorded by Gens Rerecording/KMod to a .bin file suitable for Sonic 1 and 2. This allows you to record your own demo sequences and insert them into your Sonic hack!

I made this because the original tool was written in Game Maker, and running under WINE it just spits a bunch of errors when converting a file. Mercifully, the source code was included so I could make a cross-platform version! It lacks the GUI of the original, but the program is so simple I didn't feel like adding one.

## Usage

It couldn't be simpler:

``python3 gmv2bin.py <input file> <output file>``

...where the input file is the .gmv file recorded with Gens, and the output file is a .bin file containing the demo data.

## Recording a demo

This is covered on the tool's page, but I'll put it here for convenience! The current game mode is stored in RAM address **$FFF600**, so in Gens, you'll want to add a watcher for that address. Start the game as usual, but when the title card appears, pause the emulator and skip frame-by-frame until the value becomes **$0C**. While still paused, start recording the GMV, and then unpause. The demo is now recording, so just play as usual. It's only half a minute long, so once the in-game time reaches 0:30, you can stop recording, though you can always record for longer, it'll just be ignored. Then you can convert the .gmv and add it to the demo folder of your disassembly! For the special stage, the value won't change, so start recording as soon as Sonic appears.

I've only tested this with Sonic 1 since it's what I know best, but if your demo seems out-of-sync (even when recording on the value change) that's no fault of the converter! Gens' frame skipping will sometimes skip more than one frame for some reason, and I had to try a few times for some demos.

## Credits

Full credit goes to Mercury, who actually wrote the program. I just adapted it to work in Python instead!