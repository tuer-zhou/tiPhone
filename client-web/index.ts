
enum State_t{
    IDLE,
    RINGING,
    DIALING,
    WAITING,
    CALLING,
    END
};

declare interface Window {
    localStream: MediaStream;
    localAudio: any;
}

var state : State_t = State_t.IDLE;

var handset = $("#handset");
var numberField = $("#numberField");
var numbers = $(".numbers");

var phoneNumber : string;
var ringtone = new Audio("old_ring_tone.mp3");
var callTone = new Audio("call_tone.mp3");
var endTone = new Audio("end_tone.mp3");
var callee : string;
var caller : string;
// phone number is 8 digit long

var localConnection : RTCPeerConnection;
var sendChannel : RTCDataChannel;
var sdp_offer : RTCSessionDescriptionInit;

document.addEventListener("keydown", (event) => {
    const allowedKeys: string = "0123456789";
    if (allowedKeys.includes(event.key)){
        if(numbers.prop("disabled") == false){
            handleNumberInput(event.key);
        }
    }else if(event.key == " "){
        interactHandSet();
    }
    
});

console.log(numberField);
changeUI();
const ws_url = "ws://localhost:8000/ws";
var ws : WebSocket;
/*ws.addEventListener("open", (event) => {
    
});

ws.addEventListener("message", (event) => {

});*/

fetch("http://localhost:8000/advertisement", {
    method: "POST",
    body: JSON.stringify({
        secret: "strengGeheim123!",
        name: "testWebClient"
        
    }),
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    },
    redirect: "manual"
}).then(
    x => {
        x.json().then((data) => {
            phoneNumber = data["phone_number"];
            console.log(data);
            $("#myNumber").text(phoneNumber);
            ws = new WebSocket(ws_url);
            ws.addEventListener("open", (event) => {
                ws.send(JSON.stringify({
                    msg_type: "INIT",
                    secret: "strengGeheim123!",
                    src: phoneNumber
                }));
            });
            ws.addEventListener("message", (event)=>{
                console.log(event);
                console.log(event.data);
                var json_data = JSON.parse(event.data);
                switch (json_data["msg_type"]){
                    case "CALL_REQUEST":
                        state = State_t.RINGING;
                        ringtone.currentTime = 0;
                        ringtone.play();
                        caller = json_data["src"];
                        //console.log(json_data["sdp_offer"]);
                        sdp_offer = json_data["sdp_offer"];

                        
                        break;

                    case "CALL_ACCEPT":
                        state = State_t.CALLING;
                        callTone.pause();

                        localConnection.setRemoteDescription(json_data["sdp_answer"]).then(
                            () => {
                                localConnection.onicecandidate = (e) => {
                                    if(e.candidate){
                                        console.log("sent ice candidate")
                                        ws.send(JSON.stringify({
                                            msg_type: "ICE_EXCHANGE",
                                            src: phoneNumber,
                                            dst: json_data["src"],
                                            ice_data: e.candidate
                                        }));
                                    }
                                };
                            }
                        );
                        break;

                    case "CALL_CANCEL":
                        state = State_t.IDLE;
                        ringtone.pause();
                        break;

                    case "CALL_END":
                        state = State_t.END;
                        endTone.currentTime = 0;
                        endTone.play();
                        caller = json_data["src"];
                        break;

                    case "ICE_EXCHANGE":
                        localConnection.addIceCandidate(json_data["ice_data"]);
                        break;
                }
            });
        });
    }
);

function handleNumberInput(number){
    console.log(number);
    numberField.val(numberField.val() + number);
    var dstPhoneNumber : string = String(numberField.val());
    if(dstPhoneNumber.length >= 8){
        state = State_t.WAITING;
        changeUI();
        callee = dstPhoneNumber;
        localConnection = new RTCPeerConnection();
        sendChannel = localConnection.createDataChannel("sendChannel");
        // TODO: handle connection loss
        //sendChannel.onopen
        localConnection.createOffer({offerToReceiveVideo: false, offerToReceiveAudio: true})
        .then(
            (offer) => {
                console.log("Local Description set");
                localConnection.setLocalDescription(offer).then(() => {
                    ws.send(
                        JSON.stringify(
                            {
                                msg_type: "CALL_REQUEST",
                                src: phoneNumber,
                                dst: dstPhoneNumber,
                                sdp_offer: localConnection.localDescription
                            }
                        )
                    );
                });
            }
        );
        

        callTone.play();
        getLocalStream();
    }
}

function interactHandSet(){
    switch(state){
        case State_t.IDLE:
            state = State_t.DIALING;
            break;
        case State_t.RINGING:
            ringtone.pause();
            state = State_t.CALLING;
            

            localConnection = new RTCPeerConnection();
            //sendChannel = localConnection.createDataChannel("sendChannel");
            localConnection.ondatachannel = (event) => {
                sendChannel = event.channel;
                sendChannel.onmessage = (event) => {
                    console.log(event.data);
                }
            };

            console.log("remote description set");
            console.log(sdp_offer);
            localConnection.setRemoteDescription(sdp_offer).then(
                () => {
                    localConnection.createAnswer()
                    .then((answer) => {
                        console.log("local description set");
                        localConnection.setLocalDescription(answer).then(
                            () => {
                                ws.send(JSON.stringify({
                                    msg_type: "CALL_ACCEPT",
                                    src: phoneNumber,
                                    dst: caller,
                                    sdp_answer: localConnection.localDescription
                                }));
                                localConnection.onicecandidate = (e) => {
                                    if(e.candidate){
                                        console.log("sent ice candidate")
                                        ws.send(JSON.stringify({
                                            msg_type: "ICE_EXCHANGE",
                                            src: phoneNumber,
                                            dst: caller,
                                            ice_data: e.candidate
                                        }))
                                    }
                                };
                            }
                        );
        
                    });
                }
            );
            break;
        case State_t.DIALING:
            state = State_t.IDLE;
            break;
        case State_t.WAITING:
            state = State_t.IDLE
            ws.send(JSON.stringify({
                msg_type: "CALL_CANCEL",
                src: phoneNumber,
                dst: callee
            }))
            callee = "";
            callTone.pause();
            break;
        case State_t.CALLING:
            state = State_t.IDLE
            ws.send(JSON.stringify({
                msg_type: "CALL_END",
                src: phoneNumber,
                dst: callee
            }))
            callee = "";
            break;
        case State_t.END:
            state = State_t.IDLE
            break;
    }
    changeUI();
}

function changeUI(){
    console.log("current state: " + state);
    switch(state){
        case State_t.IDLE:
            handset.text("Pick up");
            numbers.prop("disabled", true);
            numberField.val("");
            break;
        case State_t.RINGING:
            handset.text("Pick up");
            break;
        case State_t.DIALING:
            handset.text("Put down");
            numbers.prop("disabled", false);
            break;
        case State_t.WAITING:
            handset.text("Put down");
            numbers.prop("disabled", true);
            break;
        case State_t.CALLING:
            handset.text("Hang up");
            numbers.prop("disabled", true);
            break;
        case State_t.END:
            handset.text("Put down");
            numbers.prop("disabled", true);
            break;
    }
}



function phoneNumberChange(){
    console.log(numberField.html);
}

function getLocalStream(){
    navigator.mediaDevices.getUserMedia(
        {video: false, audio: true}
    ).then(
        (stream) => {
            window.localStream = stream;
            window.localAudio = new Audio();
            window.localAudio.srcObject = stream;
            window.localAudio.autoplay = true;
            window.localAudio.play().catch((err) => console.error(err));
        }
    ).catch(
        (err) => {
            console.error(err);
        }
    );
}