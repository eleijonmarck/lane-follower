# Lane-follower
A replication of https://wroscoe.github.io/keras-lane-following-autopilot.html with the aim of education and FUN

## Downloading training data

Data from wroscoe [s3-indoor_lanes](https://s3.amazonaws.com/donkey_resources/indoor_lanes.pkl). # 450 MB

# Welcome to Lane-follower!

Build a model using keras / tensorflow for outputing a int between -70 : 70 for the steering wheels 
based on a streamed image from the RC.

* Each have their own team ( hopefully )
* Build the model and output a pickle file in the /models directory with your team name like so: /models/team_name.pkl
* Each team will push the models to ```git push origin master team_name```
* We estimate that training with regular CPU takes about ~30 min
* Dedicated time for testing the models will be at
 * time
 * time
 * some other time
* We have made it so that the driving lane will get harder and harder. And see who makes it the furtherest
* Winning 3 teams will present their model and thoughtprocess

TODO:
[ ] sponsor
[x] estimate the number of needed participants for the event - around 40 people
[ ] USB-sticks for loading the models through /usb/model.pkl 
[x] ~~git server for cars~~ - Would have been cool. Nice to have feature
[ ] might need GPU credits for the event. ~ anyone know how much?
[ ] venue?
[ ] see what framerate is needed for input to model