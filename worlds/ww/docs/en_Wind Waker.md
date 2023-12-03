# Wind Waker Setup Tutorial
This will hopefully get you raring to go on a run of Wind Waker

To get the bad news out of the way. Right now this is WINDOWS ONLY
As someone who owns a Mac, I apologize.

# Credit
This uses a FORK of the already made '[wwrando](https://github.com/LagoLunatic/wwrando)' created by Lago Lunatic! 
My Fork of it is mostly comments; This just simply wouldn't be possible without his work.

This is also inspired by CrainWWR's Multiworld that he made.
[CrainWWR](https://github.com/Crain-32) was a very kind and helpful lad for helped get me started with tips and permission to use some code
I didn't end up using a lot of his stuff, but I did use a lot of ideas that I saw him use.

# How it Works
Wind Waker's memory system is the devil. To avoid major problems I used a kinda cheesy, but handy solution.
(Which CrainWWR kindly suggested).
Each Check in your actual game will have either a Green/Red Rupee.
Green meaning the check is supported.
Red meaning the check is NOT supported.
This works as a neat little 'Should I expect the Client to give me an item now' system based on the color.
It is also a tiny little reward for doing something not required.

# Download the WWRANDO fork
This being the case, you actually don't need to generate a NEW ROM everytime.
The same original Green/Red Rupee ROM works all the time (as long as you start a new save file)

The wwrando for can be found [here](https://github.com/Dev5ter/wwrando/releases).

There is a guide on how to install it via source code [here](https://github.com/Dev5ter/wwrando).
Now though, you can run the wwrando via an .exe on the latest release!

# Running the WWRANDO
The settings options on this are NOT going to affect what Archipelago Server cares about MOSTLY. The item checks boxes aren't really affecting anything.
This is where you can pick your sprite. A list of downloadable sprites can be found [here](https://github.com/Sage-of-Mirrors/Custom-Wind-Waker-Player-Models).
I did not make any of these. This is a collective of a community effort.

IMPORTANT: It is also worth noting that if you move anything to your starting items, you WILL start with that BUT Archipelago will not recognize that.
Therefore, the items you start with will still techincally be in the game, so just leave them all alone for smooth results.

# Dolphin
The emulator you have to use is [Dolphin](https://dolphin-emu.org).
I've heard some issues about older versions of Dolphin crash while running Wind Waker, so I recommend getting one of the latest Dev Versions.

# IMPORTANT
Dolphin MUST be running with the game open and loaded BEFORE you start the client.
The Client will not be able to interact with the game if you do not have Dolphin loaded and ready FIRST.

# WW.apworld
There is now an .apworld file for Wind Waker! It can be found [here](https://github.com/Dev5ter/ww-apworld/releases).
To run this you need to drop the dolphin-memory-engine folder in [Arch Install]/lib folder. You also need to drop the .apworld file itself in the [Arch Install]/lib/worlds folder. 

# The WW Client
This means the client is really responsible for giving the player all the items, since the chests just have rupees.
The client is still in early development, but it technically works. It needs some full game tests though.
As far as how the user interacts with the client it is exactly the same as the CommonClient.
I didn't add any extra commands or things such as that.

# Victory
As of now the only way to win is to Beat Ganondorf.
This means logically you need at least the following items first
- All 8 Triforce Shards (Triforce of Courage)
- All 3 Progressive Bows (Light Arrows)
- All 4 Progressive Swords (Fully Restored Master Sword)
- 1 of the 2 Progressive Shields
- Hookshot
- Grappling Hook
- Boomerang

