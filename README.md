the biggest side quest
# tiPhone
the tiPhone is device that looks like a land line rotary telephone to call your friends, each with a different phone number

the plan is make the case 3d printed and use a micro controller inside to communicate with the server

<img src="images/rotaryPhone.jpeg" width="192"/>

## Client
### you should be able to make
- 1 to 1 calls
- group calls
- should be connected to power outlet and connection to server is via wifi

### further ideas
- urgent calls (just with a different ring tone)
- video calls, camera inside of the hand part
- hand free call, make speaker volume higher
- digital display to select phone number and the rotary part moves automatically
- make hand part wireless, requires wireless communication to base station and battery
- send text like a fax (a whole printer might be overkill/wasteful, receipt printer with thermo paper )

## Server
server is not public, so each friend group should have one
idea is have a shared key (probably not too secure) or make everyone have a certificate that needs to be added to the server

### Must haves
- database to save all participant's data
- secure/encrypted connection
- has web interface for easier management

### ideas
- interoperability with other servers