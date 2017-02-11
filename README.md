# Welcome to Lane-follower!
Build a model using keras / tensorflow for outputing a int between -80 : 80 for the steering wheels 
based on a streamed image from the RC. Inspired by the work from
[wroscoe](https://wroscoe.github.io/keras-lane-following-autopilot.html)

## Event details
* Each participant will have their own team ( hopefully )
* Each team will build the model and output a pickle file in the /models directory with your team name like so: /models/team_name.pkl
* We estimate that training with regular CPU takes about ~30 min
* Dedicated time for testing the models will be at
 * time
 * some other time
* We have made it so that the driving lane will get harder and harder. And see who makes it the furtherest
* Winning 3 teams will present their model and thoughtprocess

## Downloading training data
Data from wroscoe [s3-indoor_lanes](https://s3.amazonaws.com/donkey_resources/indoor_lanes.pkl). # 450 MB

TODO:
- [x] sponsor - potential sponsor from Scania, they can't take any credit.
- [x] estimate the number of needed participants for the event - around 40 people
- [ ] USB-sticks for loading the models through /usb/model.pkl 
- [x] ~~git server for cars~~ - Would have been cool. Nice to have
  feature, will use the USB-sticks instead
- [x] might need GPU credits for the event. ~ anyone know how much?
  - 8sek/hour for a decent GPU in the cloud (thats full, on-demand price for a GPU comprable to a new titan) 200sek for 24h
- [ ] venue?
- [ ] see what framerate is needed for input to model
