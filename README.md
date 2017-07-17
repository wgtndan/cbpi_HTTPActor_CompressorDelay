# HTTPActor Plugin for CraftBeerPi 3.0

## Introduction
The HTTPActor plugin allows CraftBeerPi to send commands to any device that accepts HTTP requests so that devices can be controlled remotely.  It can be configured to communicate with any device where the HTTP API is known, whether local or internet based.

This plugin is based on the WiFi Socket plugin, found here: https://github.com/Manuel83/cbpi-WIFISocket

## Screenshot ##
![httpactor](https://user-images.githubusercontent.com/29404417/28288881-a9440bae-6b0e-11e7-907d-23403ecbc3b2.PNG)

## Installation
From CraftBeerPi, navigate to the **System** menu and click **Add-Ons**. Find the HTTPActor plugin and click Download.  You will then have to reboot your Pi for the plugin to become available.

## Actor Configuration
1. Add a new actor from the **Hardware Settings** screen, and select the type HTTPActor
2. Enter the following properties according to the device you wish to control:
    1. **Controller Address**: This is the IP address or hostname of the device that you wish to control. Make sure it is entered in the format `http://<ip address or hostname>:<port number if necessary>`. Do not add a trailing backslash to the end of the address.
    2. **On Command**: Enter the HTTP command that turns on this device on the controller. Do not add a slash to the beginning. *Example if using EasyESP: control?cmd=GPIO,(pin number),1*
    3. **Off Command**: Enter the HTTP command that turns off this device on the controller.  Do not add a slash to the beginning. *Example if using EasyESP: control?cmd=GPIO,(pin number),0*
    4. **Power Command**: If this device supports power states/PWM, you may enter the command used to set the power on the controller. This command is different from the others, as the power level of the actor will be inserted automatically to the end of the command. Do not add a slash to the beginning. *Example if using EasyESP: control?PWM,(pin number),*
    5. Click **Add** when done.
    
## Using the HTTPActor
You can now use the HTTPActor like you would any other actor, or assign it to any control parameters that utilize an actor. Please note however that the HTTPActor is limited by the fact that it is using HTTP, so there will most likely be a delay in processing commands. It is not recommended to use the HTTPActor for controller logic that uses quick on/off pules, such as PID, since the actor would not respond quickly enough and may cause problems. HTTPActors may also not perform well in ActorGroups, because of this same delay, but feel free to experiement!
