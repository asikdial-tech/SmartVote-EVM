# SmartVote EVM: Project Report

## Overview
SmartVote EVM is an innovative electronic voting machine designed for Bangladesh, allowing users to vote for fictional brands using RFID authentication and cloud-based logging. Built with an ESP32, 0.96-inch OLED, RFID reader, buttons, LEDs, and buzzer, it ensures secure, transparent voting for a science fair demonstration.

## Purpose
- Demonstrate IoT-based voting for Bangladeshi-inspired brands.
- Showcase secure RFID authentication and real-time Google Sheets logging.
- Highlight a unique, space-themed system for transparency and engagement.

## Rules and Regulations
1. **Eligibility**:
   - Users must have a registered RFID card (UIDs: 0x0358ae34, 0xe7458e7a, 0x21d0fd1d, 0x29eec498, 0x59e1f097).
   - Each user votes once per session (tracked via `voted_rfids` set).
2. **Voting Process**:
   - Scan RFID card to authenticate.
   - Select a brand (ShonarLabs, NiravTextiles, PadmaCrafts, MeghnaTech) via buttons.
   - Press reset button to cancel selection within 10 seconds.
   - Vote is logged to Google Sheets if WiFi is connected.
3. **Security**:
   - Only registered RFID UIDs are accepted.
   - Duplicate votes are blocked.
   - Data is encrypted via HTTPS to Google Sheets.
4. **Operation**:
   - OLED displays status (e.g., “Scan RFID”, “Confirmed”).
   - Green LED and buzzer signal successful votes; red LED indicates errors.
   - Votes are logged with timestamp, voterID, candidate ID, and status.

## Operation Flow
1. Power on: Displays “SmartVote”.
2. Connect to WiFi (SSID: IoT, Password: 12345678).
3. Scan RFID: Shows user ID or “Denied”.
4. Select brand or reset.
5. Log vote: Updates Google Sheet with brand ID (B0x01 to B0x04).

## Contact
- Developer: Asik Dial Kuffer
- Email: asikdial.tech@gmail.com
- GitHub: https://github.com/asikdial-tech/
