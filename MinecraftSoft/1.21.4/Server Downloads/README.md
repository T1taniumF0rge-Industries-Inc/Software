# Minecraft 1.21.4 Server Downloads
## Java Server:
***Please note: This server setup is only compatible with Minecraft Java Edition. All rights reserved to Microsoft Corporation.***
#### © Microsoft Corporation: https://www.microsoft.com/

If you want to run a Minecraft multiplayer server by yourself things get kind of involved ([see this wiki article for a tutorial](https://minecraft.wiki/w/Tutorials/Setting_up_a_server)). First make sure you can use java from the command line. On Linux and macOS this should already be set up but on Windows you might have to tinker with the PATH environment variable.

*After you have downloaded the server (java_server-1.21.4.jar), run it with the following commands in the Windows Command Prompt **(make sure you have a [JDK](https://www.oracle.com/uk/java/technologies/downloads/#jdk23-windows) higher than [Java SE 17](https://www.oracle.com/java/technologies/javase/jdk17-0-13-later-archive-downloads.html)):***

`cd "the/directory/you/installed/the/server/file/to"`

`java -Xmx1024M -Xms1024M -jar java_server-1.21.4.jar nogui`

*Should you want to start the server with its graphical user interface you can leave out the "nogui" part.*

`java -Xmx1024M -Xms1024M -jar java_server-1.21.4.jar`

*To control the amount of RAM to allocate to your server, change both of the "-Xms" settings **by using binary megabytes!***

`java -Xmx9216M -Xms9216M -jar java_server-1.21.4.jar`

*It is recommended to make a batch file in your server's directory called "run.bat" and implementing the command in it so that you don't need to use Windows Command Prompt every time.*

You can convert GB into MB by multipliying your gigabytes by 1024. The result will be the amount of binary megabytes. Here is an example from 1GB to 10GB:
| Gigabytes (GB)| Binary Megabytes (M)|
| --------- | ------------ |
| 1GB | 1024M |
| 2GB | 2048M |
| 3GB | 3072M |
| 4GB | 4096M |
| 5GB | 5120M |
| 6GB | 6144M |
| 7GB | 7168M |
| 8GB | 8192M |
| 9GB | 9216M |
| 10GB | 10240M |

Just so you know, by downloading any of the software here, you agree to the [Minecraft End User License Agreement](https://www.minecraft.net/en-us/eula) and [Privacy Policy](https://www.microsoft.com/en-gb/privacy/privacystatement).

If you want to skip the setup and start exploring other 3rd party servers visit Microsoft's official [Server Listing Site](http://aka.ms/verifiedservers). Each server offers its own brand of fun and uniqueness. Find your favorite with their Server List Site, where all listed servers have been reviewed and verified as following our community standards and guidelines. Browse servers based on game type, play style, and more. Chance is there's a server listed for you – regardless of age or the way you play.
