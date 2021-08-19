# hass-petkit-feeder
This is a work in progress but wanted to get it out since I have it working. This is how to get basic sensors at this point in time from PetKit Feeders into Home Assistant using the command line sensor and parsing out the JSON response with Template Sensors. I Might work on a custom component but someone else is free to take what i've done and go from there. 

# SETUP
1) Follow the instructions to get the X-Session ID from the app found here: https://github.com/elfive/homebridge-petkit-feeder-mini
2) Change the `cookie` variable in `petkit-hass.py` 
3) Create a new folder on HASSIO in `/config` called `scripts`. If you want to place it somewhere else, go for it just change the command in the yaml
4) Edit your configuration Yaml with the data from `configuration.yaml` in this repo 
5) Restart HASSIO 

Other things to note, the full json is stored, so you can get the feeding information, like when the next feeding is, how much will be dispenced and create your own sensors for those. These are pretty easy to do and I will likely add them in the near future to the yaml example. 
