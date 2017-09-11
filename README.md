# HTTPActor with Compressor Delay Plugin for CraftBeerPi 3.0

## Introduction
The HTTPActor with Compressor Delay plugin allows CraftBeerPi to send commands to any device that accepts HTTP requests so that devices can be controlled remotely, and can be configured with a delay timer. It can be configured to communicate with any device where the HTTP API is known, whether local or internet based.
The delay ensures that you can use this with Wifi sockets connected to compressor based cooling devices.

This plugin is based on the HTTPActor plugin, found here: https://github.com/wgtndan/cbpi_HTTPActor
This plugin also utilises logic from the GPIO Compressor plugin, found here:
https://github.com/carlallen/cbpi_GPIOCompressor

## Screenshot ##
![httpactorcompressordelay](https://user-images.githubusercontent.com/18130038/30268460-e0719af4-9739-11e7-8bdf-e097ba191223.png)

## Installation (Under Construction)
From CraftBeerPi, navigate to the **System** menu and click **Add-Ons**. Find the HTTPActor with Compressor Delay plugin and click Download.  You will then have to reboot your Pi for the plugin to become available.

## Actor Configuration
1. Add a new actor from the **Hardware Settings** screen, and select the type HTTPActor
2. Enter the following properties according to the device you wish to control:
    1. **Controller Address**: This is the IP address or hostname of the device that you wish to control. Make sure it is entered in the format `http://<ip address or hostname>:<port number if necessary>`. Do not add a trailing backslash to the end of the address.
    2. **On Command**: Enter the HTTP command that turns on this device on the controller. Do not add a slash to the beginning. *Example if using EasyESP: control?cmd=GPIO,(pin number),1*
    3. **Off Command**: Enter the HTTP command that turns off this device on the controller.  Do not add a slash to the beginning. *Example if using EasyESP: control?cmd=GPIO,(pin number),0*
    4. **Compressor Delay**: Enter the amount of time (in minutes) to force the switch to be delayed following being shut off before it is able to be turned on again.
    5. Click **Add** when done.
    
## Using the HTTPActor with Compressor Delay
You can now use the HTTPActor with Compressor Delay like you would any other actor, or assign it to any control parameters that utilize an actor. Please note however that the HTTPActor with Compressor Delay is limited by the fact that it is using HTTP, so there will most likely be a delay in processing commands. HTTPActors with Compressor Delay may also not perform well in ActorGroups, because of this same delay, but feel free to experiement!
