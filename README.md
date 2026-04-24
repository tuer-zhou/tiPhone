# ☎️ tiPhone – The Ultimate Retro-VoIP Side Quest

<p align="center">
  <img src="./assets/rotary_phone.jpg" alt="tiPhone Inspiration: Classic Rotary Phone" width="600">
</p>

The **tiPhone** is a modern reimagining of the classic rotary dial landline telephone. It blends the tactile nostalgia of the analog era with 21st-century tech like VoIP, wireless handsets, and video calling. 

Each user group operates its own private server, manages its own phone numbers, and communicates via encrypted channels within a closed network.

---

## 🚀 Core Concept

The tiPhone ecosystem consists of a custom 3D-printed base station and a smart wireless handset. While it looks like a vintage device, the internal logic is powered by modern microcontrollers (uC) communicating via WiFi and Bluetooth.

### Key Features
* **Mechanical Rotary Dial:** Full support for pulse dialing logic.
* **Wireless Handset:** Total freedom from cords. The handset communicates via Bluetooth with the base station.
* **Integrated Display & Camera:** A screen embedded in the handset allows for phonebook navigation and video calls (FaceTime).
* **Persistence:** Phone numbers are tied to users. If you leave the network and return later, you keep your original number.
* **Smart Charging:** The handset features a built-in battery and charges via metal contact pads (pogo pins) in the cradle, similar to modern smartwatch charging docks.

---

## 🏗 Hardware Architecture

### 1. The Base Station (The Command Center)
* **Housing:** Fully 3D-printed chassis.
* **Brain:** Microcontroller (e.g., ESP32) with WiFi connectivity.
* **Functions:**
    * **Pulse Detection:** Reads pulses from the mechanical rotary dial.
    * **Hook-Detection:** Monitors the state via the charging Pogo-Pins. 
        * *On-Hook:* Handset is charging; system is idle.
        * *Off-Hook:* Circuit break on Pogo-Pins triggers the "Answer Call" or "Dial Tone" action.
    * **Gateway:** Acts as the Bridge between the Bluetooth Handset and the WiFi VoIP Server.
* **Power:** Powered via a standard wall outlet.

### 2. The Smart Handset (The Interface)
* **Connectivity:** Bluetooth link to the Base Station.
* **Interface:**
    * **Digital Display:** For phonebook navigation and system status.
    * **Controls:** 3 buttons for menu navigation (Up, Down, Select) + 1 dedicated FaceTime/Video button.
* **Multimedia:**
    * Integrated Camera for video calls.
    * Speaker & Microphone.
    * **Hands-free Mode:** An integrated amplifier boosts the speaker volume for FaceTime/video calls. 
* **Power Management:** Internal battery with charging pads on the exterior.

---

## 📟 Dual-Dialing Logic

The tiPhone supports two seamless methods for initiating calls, managed by the Base Station:

1. **Manual Rotary Dialing (Old School):**
   - Lift handset (Base station detects "Off-Hook" and triggers dial tone).
   - Use the mechanical rotary dial.
   - The Base Station processes pulses and initiates the VoIP call via the Server.

2. **Digital Phonebook Dialing (Modern):**
   - Lift handset.
   - Use the handset buttons to navigate the integrated OLED menu.
   - Pressing 'Select' sends the contact's number via Bluetooth to the Base Station, which then bridges the call to the Server.

---

## 🌐 Server & Networking

The tiPhone does not use the public telephone network. It relies on a dedicated, private server architecture.

* **VoIP Management:** Handles 1-to-1 calls and group conferences.
* **Database:** Stores participant data, certificates, and phone number assignments.
* **Security:** Encrypted connections (TLS/SRTP). Authentication via shared keys or client certificates.
* **Web Interface:** A dashboard for easy user and number management.
* **Interoperabilität:** Optionale Kopplung verschiedener tiPhone-Server.

---

## 🛠 Features & Roadmap

- [ ] **Basic VoIP:** 1-to-1 voice calls.
- [ ] **Wireless Handset:** Audio streaming via Bluetooth between the base uC and the handset.
- [ ] **Charging System:** Implementation of physical pogo-pin contacts in the 3D design.
- [ ] **Phonebook:** Menu navigation on the handset display via physical buttons.
- [ ] **FaceTime Mode:** Video streaming and automatic toggling of the hands-free amplifier.
- [ ] **Urgent Calls:** Specialized ringtones for priority contacts.
- [ ] **Smart Mic Logic:** Evaluating a microphone solution (e.g., MEMS) that covers both close-range speech and room-filling hands-free pickup.
- [ ] **Auto-Dial:** Motorized rotary dial that moves automatically when a number is selected via the digital phonebook.
- [ ] **Fax/Printer:** Integration of a thermal receipt printer for "Text-Faxes."

---

> **"Reinventing the dial: Retro aesthetics, modern protocols."**
