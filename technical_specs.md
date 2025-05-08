# SmartVote EVM: Technical Specifications

## Hardware
- **Microcontroller**: ESP32-WROOM-32
  - Dual-core, 240 MHz, WiFi-enabled
  - Power: 3.3V (USB or 3.7V or 4V battery with regulator)
- **Display**: 0.96-inch SSD1306 OLED
  - Resolution: 128x64 pixels
  - Interface: I2C (SDA: Pin 21, SCL: Pin 22)
  - Address: 0x3C
- **RFID Reader**: MFRC522
  - Interface: SPI (SCK: 18, MOSI: 23, MISO: 19, CS: 5, RST: 4)
  - Frequency: 13.56 MHz
- **Buttons**: 5 push-buttons
  - Pins: 12, 13, 15, 16 (brands), 17 (reset)
  - Pull-up: 10kΩ resistors to 3.3V
- **LEDs**:
  - Red: Pin 14 (220Ω resistor)
  - Green: Pin 27 (220Ω resistor)
- **Buzzer**: Active, Pin 25
- **Power**:
  - 3.3V for all components
  - Stable supply via USB or regulator

## Software
- **Firmware**: MicroPython 1.20 or later
- **Main Program**: SmartVote_EVM.py
  - Handles RFID, OLED, buttons, WiFi, and Google Sheets
- **Libraries**:
  - SSD1306.py: OLED driver
  - RFID_M.py: MFRC522 driver
  - urequests.py: HTTP requests
- **Google Apps Script**: Code.gs
  - Logs votes to Google Sheet (Sheet1)
  - Fields: Timestamp, VoterID, Brand, Status

## Brand Data
- ShonarLabs (B0x01): Tech innovation
- NiravTextiles (B0x02): Textile industry
- PadmaCrafts (B0x03): Artisanal goods
- MeghnaTech (B0x04): Technology solutions

## RFID Data
- UIDs: 0x0358ae34, 0xe7458e7a, 0x21d0fd1d, 0x29eec498, 0x59e1f097
- Names: Asik Dial, Dip Biswas, Student1, Student2, Student3
