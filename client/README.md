# tiPhone Client
This folder contains the code for the physical hardware.
* **base-station/**: Logic for the rotary dial and WiFi/BT gateway.
* **handset/**: Logic for the wireless communication, display, and audio.

---

The idea is to use an esp32 or a raspberry pi pico w

voice data is trasmitted via webRTC and general information over websocket

when a screen is added, the name of the caller should be shown

the internal state should be handeled by a state machine  
- Idle
- Ringing
- Dialing
- Waiting
- Calling
- End


## States
### Idle
Is the default state of the device, waiting for incoming calls
can either change to:
- Ringing: when some is calling
- Dialing: when the ear piece/handset is picked up


### Ringing
In this state the ring tone is playing, waiting for the ear piece/handset to be picked up
can change to:
- Calling: when the earpiece/handset is picked up
- Idle: when the caller stops the call (or too much time passed)


### Dialing
This states waits for inputs
can change to:
- Waiting: when a valid phone number was entered
- Idle: when the handset is put back


### Waiting
Wait for the dailed participant to pick up their handset
can change to:
- Calling: when dailed participant picked up their handset
- Idle: when callee puts their handset back


### Calling
The two pariticipants are connected and can talk to each other
can change to:
- End: when the other participant end the call by putting their handset back
- Idle: when the callee puts their handset back