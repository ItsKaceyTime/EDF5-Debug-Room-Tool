# EDF5-Debug-Room-Tool
This is a tool to make lightweight changes to my Earth Defense Force 5 debug room without the user having to learn (and change) the code themselves.

EDF5 mission modding, currently, requires a solid amount of understanding and effort. My goal is to both create a tool to broaden the usage of a debug room I've created for the average user, as well as to lower the barrier to entry for modifying missions, hopefully encouraging more people to look deeper into modding the game. I'm also hoping that my work here will be setting the groundwork for more user friendly modding tools.



HOW TO USE:

Install BlueAmulet's ModLoader: https://github.com/BlueAmulet/EDFModLoader

Download Kittopia's Unnamed EDF Tools: https://gitlab.com/kittopiacreator/edf-tools

After downloading, find EDF Tools.exe, located in the Release folder, and copy it to my tool's directory.

Run debugroomtool.exe

With the tool open you'll see a handful of dropdown menus. Look for the enemy you wish to spawn in here. The second column of dropdown menus are for variations of the enemy type you selected. Once you've finished selecting an enemy, text will display above the second dropdown menus, showing you the exact .SGO file being loaded.

You can also set the radius around the spawnpoints that enemies are spawned, the amount of enemies spawned at a time, their health multiplier, and if they're aggro on-spawn or not.

Once you're done, select where you'd like to output the file. (if you leave this field blank, it will leave your mission file in the same directory as the tool)

Click confirm and your file should be output to the set destination. You're going to want to move both the MISSION.bvm file and the MISSION.rmpa file to the corresponding mission folder you wish to replace. A lot of EDF modding currently replaces M003, aka Crisis in Base 228: Part 1. In order to accomplish this, go to your EDF5 root directory, and in your Mods folder create a new folder named MISSION. Then, within MISSION, create a new folder named M003. Copy your MISSION.bvm file as well as the MISSION.rmpa file that you can find in the tools directory into your newly created M003 folder.

And you're done! Launch the game and load into the mission to ensure you installed the custom mission correctly.

There are four Shooting Targets with functions upon being destroyed. 3 of them are tied to spawning the enemies you've selected, with the fourth tied to completing the mission.

Enjoy! Please feel free to ping me in the EDF Discord server's modding channel to ask questions or offer suggestions and requests for this tool! 



FOR MODDERS:

If you wish to include your own custom SGO files it's very easy. Open up enemylist.json and follow the same structure as the rest of the file to create your own category and/or entry. 

If you wish to expand functionality of this tool, please feel free. I eventually wish to make this tool able to read and edit vanilla BVM files in this same style. 
