# Monash Air Sense Device Documentation - Linkit Smart 7688
This documentation is device specific information for the Linkit Device. Much of it complements the manufacturer documentation. However, some extra tips and commonly needed information is found here.
<br/><br/>
Handy Links:

* The official documentation for the MediaTek Linkit Smart 7688 family of devices can be found here:
(https://labs.mediatek.com/en/platform/linkit-smart-7688)
* The specific device that has been developed on is the plain [device](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board), not the Duo (with Arduino).
* [Downloads](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/downloads) including firmware and the like
* [Documentaiton](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/documentation) such as PDF manual etc.
* [Tutorials](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/tutorials) - Useful for the important functions such as resetting the device, firmware upgrades, WiFi and much more. 

## Setup of a new device
Follow [this](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board/sign-in-to-the-web-ui) guide. 
<br/> Make sure to [update firmware](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board/update-your-boards-firmware) to v0.9.2 as this is the reference implementation.

## Reset WiFi Authentication
At some point you may have to put the device LinkIt 7688 from AP mode back to Station mode. To do this,
first press the MCU button to restart the device. The WiFi light will come on, and stay on while the system boots. Then the WiFi light will turn off and begin to flash. Hold down the WiFi button for 5 seconds but no more than 20 seconds. The device should change to Station Mode and will be accesible directly on its own WiFi network.
<br/> Useful related information might be [Wi-Fi LED States](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/tutorials/wi-fi-led-states) as well as the [network](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/tutorials/network) tutorials on how to [reset](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/tutorials/network/reset-wi-fi-configuration) the WiFi configuration.

## Reset Device
To factory reset the device follow [these](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/tutorials/firmware-and-bootloader/factory-reset) instructions. In summary they are:
1. Boot up the board and wait for the WiFi LED to go off.
2. Press and hold the WiFi button for at least 20 seconds then release.
3. The WiFi LED will blink fast for 1 second, and then reboot to perform a factory reset.
