# SmartVote EVM: Smart Voting System

## Overview
SmartVote EVM is a unique IoT-based voting machine for Bangladesh, allowing users to vote for fictional brands using RFID cards. Built with an ESP32, 0.96-inch OLED, RFID reader, buttons, LEDs, and buzzer, it logs votes to Google Sheets in real-time. Designed for a science fair, it showcases secure, transparent voting with a space-themed interface.

## Features
- **RFID Authentication**: Validates users via MFRC522 reader.
- **Brand Voting**: Vote for fictional brands (ShonarLabs, NiravTextiles, PadmaCrafts, MeghnaTech).
- **OLED Display**: Shows status (e.g., “Scan RFID”, “Confirmed”) with clear text.
- **Feedback**: Green/red LEDs and buzzer indicate success/errors.
- **Cloud Logging**: Votes saved to Google Sheets with timestamp, voterID, brand ID.
- **Reset Option**: Cancel vote selection within 10 seconds.

## Hardware Requirements
- ESP32-WROOM-32
- 0.96-inch SSD1306 OLED (128x64, I2C)
- MFRC522 RFID reader
- 5 push-buttons (10kΩ pull-up resistors)
- Red and green LEDs (220Ω resistors)
- Active buzzer
- 3.3V power (USB or 3.7V or 4V battery with regulator)

## Software Requirements
- MicroPython 1.20 or later
- Thonny IDE
- Google Account for Apps Script and Sheets
- Libraries: SSD1306.py, RFID_M.py, urequests.py

## Setup Instructions
1. **Hardware**:
   - Wire components as per `connections.txt`.
   - Ensure 10kΩ pull-up resistors for buttons and 4.7kΩ for I2C.
2. **Firmware**:
   - Install MicroPython on ESP32.
   - Upload `SmartVote_EVM.py`, `SSD1306.py`, `RFID_M.py`, `urequests.py` using Thonny.
3. **Google Sheets**:
   - Create a Google Sheet with headers: Timestamp, VoterID, Brand, Status.
   - Deploy `Code.gs` in Google Apps Script (Execute as: Me, Access: Anyone).
   - Update `google_script_url` in `SmartVote_EVM.py` with the deployed URL.
4. **WiFi**:
   - Set SSID (`IoT`) and password (`12345678`) in `SmartVote_EVM.py`.
5. **Run**:
   - Power on ESP32.
   - Scan RFID, select brand, check OLED/LEDs/buzzer, verify Sheet.

## Files
- `SmartVote_EVM.py`: Main program.
- `SSD1306.py`: OLED driver.
- `RFID_M.py`: RFID driver (use your version).
- `urequests.py`: HTTP library (use standard version).
- `Code.gs`: Google Apps Script.
- `connections.txt`: Wiring diagram.
- `project_report.md`: Project overview and rules.
- `technical_specs.md`: Hardware/software specs.

## Demo
1. Scan RFID card (e.g., 0x0358ae34).
2. Press brand button (e.g., ShonarLabs).
3. Press reset to cancel.
4. Check OLED (“Confirmed”), green LED, buzzer.
5. View Google Sheet for vote (e.g., B0x01).

## Troubleshooting
- **Blurry OLED**: Adjust `oled.contrast(0xFF)` or reduce `scale=1` in `word_text`.
- **Buttons**: Verify 10kΩ pull-ups; test with Serial Monitor.
- **WiFi**: Check SSID/password; use hotspot.
- **Sheet**: Ensure URL and script match; check Apps Script logs.
- Contact: asikdial.tech@gmail.com

## License
MIT License

## Author
Asik Dial Kuffer, Bangladesh
