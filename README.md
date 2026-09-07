AIRCHAT
# AirChat

Offline P2P Chat tool for Android. Chat with 2 mobiles using WiFi Hotspot. No Internet needed.

## Installation

```bash
git clone https://github.com/masimmirzaisi100/AIRCHAT.git
cd AirChat
pkg install python -y
run for your server "python me.py"
run for your friend server "python friend. py"
## Procedure After Running

### For Server - Step 1
1.  Run `python me.py`
2.  You will see: `Server Started on 192.168.43.1:9999`
3.  Keep Hotspot ON and note down the IP

### For Client - Step 2  
1.  Connect to Server's Hotspot
2.  Run `python friend.py`
3.  It will ask: `Enter Server IP:`
4.  Type Server's IP: `192.168.43.1` and press Enter
5.  You will see: `Connected to Server`

### How to Chat - Step 3
1.  After connecting, you will see `You:` on both sides
2.  Type anything and it will send to the other mobile
3.  To exit chat, type `exit` and press Enter

### If You Get Error
`Connection Refused` = Wrong IP or Hotspot is OFF
`Timeout` = Both mobiles are not on same Hotspot
