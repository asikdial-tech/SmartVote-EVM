from RFID_M import MFRC522
from machine import SoftSPI, SoftI2C, Pin
from time import sleep, ticks_ms
import SSD1306
import network
import urequests

# WiFi credentials
ssid = 'IoT'
password = '12345678'

# Google Sheets script URL
google_script_url = 'https://script.google.com/macros/s/AKfycbzCwMhRI3pFMXRPsvyuAHFWl66SlXE85AdtBXh-tKIIDFSlz5SVa8bd2imcjVRxpjg3/exec'

# Pin configuration
i2c_scl = Pin(22, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(21, Pin.OUT, Pin.PULL_UP)
spi_sck = Pin(18, Pin.OUT)
spi_mosi = Pin(23, Pin.OUT)
spi_miso = Pin(19, Pin.IN)
spi_cs = Pin(5, Pin.OUT)
spi_rst = Pin(4, Pin.OUT)
red_led = Pin(14, Pin.OUT)
green_led = Pin(27, Pin.OUT)
buzzer = Pin(25, Pin.OUT)
button_pins = [0, 13, 14, 15, 16]  # 4 candidates + 1 confirm/reset

# Initialize I2C and OLED with error handling
try:
    i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda, freq=400000)
    oled = SSD1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
except OSError as e:
    print("OLED init failed:", e)
    oled = None  # Fallback to no display

# Initialize SPI and RFID
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=spi_sck, mosi=spi_mosi, miso=spi_miso)
rdr = MFRC522(spi=spi, gpioRst=spi_rst, gpioCs=spi_cs)

# Initialize buttons
buttons = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in button_pins]

# RFID and candidate data
rfid_name = ["Asik Dial Kuffer", "Dip Biswas", "Student1", "Student2", "Student3"]
rfid_uid = ["0x0358ae34", "0xe7458e7a", "0x21d0fd1d", "0x29eec498", "0x59e1f097"]
candidates = ["A. Rahman", "B. Khan", "C. Ali", "D. Hossain"]
voted_rfids = set()

def word_text(msg, x, y, clear=False):
    if oled:
        if clear:
            oled.fill(0)
        lines = [msg[i:i+16] for i in range(0, len(msg), 16)]
        for i, line in enumerate(lines[:4]):
            oled.text(line, x, y + i*10)
        oled.show()

def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    timeout = 10
    while not station.isconnected() and timeout > 0:
        sleep(1)
        timeout -= 1
    if station.isconnected():
        print('Connection successful')
        word_text('WiFi Connected', 0, 10, True)
        green_led.value(1)
        sleep(2)
        green_led.value(0)
        print(station.ifconfig())
        return True
    else:
        word_text('WiFi Failed', 0, 10, True)
        return False

def get_username(uid):
    try:
        index = rfid_uid.index(uid)
        return rfid_name[index]
    except ValueError:
        print("RFID not recognized")
        return None

def beep():
    buzzer.value(1)
    sleep(0.2)
    buzzer.value(0)

def send_vote_to_google_sheets(voter_id, candidate):
    try:
        payload = {'voterID': voter_id, 'candidate': candidate}
        response = urequests.post(google_script_url, json=payload)
        if response.status_code == 200:
            print("Vote logged")
            word_text('Vote Logged', 0, 50, False)
            return True
        else:
            print("Failed to log vote:", response.status_code)
            word_text('Log Error', 0, 50, False)
            return False
    except Exception as e:
        print("Error sending vote:", e)
        word_text('Log Error', 0, 50, False)
        return False

# Boot animation
word_text('SmartVote EVM', 10, 10, True)
word_text('Mission Control', 10, 30, False)
sleep(2)

# Connect to WiFi
wifi_connected = connect_wifi(ssid, password)

print("Place NID Card")
word_text('Scan RFID', 10, 10, True)

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("UID:", card_id)
            username = get_username(card_id)

            if username and card_id not in voted_rfids:
                word_text('ID: ' + username[:10], 0, 10, True)
                word_text('Choose Candidate', 0, 20, False)
                green_led.value(1)
                red_led.value(0)
                beep()

                start_time = ticks_ms()
                selected_candidate = None
                while ticks_ms() - start_time < 10000:
                    for i in range(4):
                        if buttons[i].value():
                            selected_candidate = candidates[i]
                            while buttons[i].value():
                                sleep(0.01)
                            break
                    if selected_candidate:
                        break
                    if buttons[4].value():
                        selected_candidate = None
                        break
                    sleep(0.1)

                if selected_candidate:
                    word_text('Vote: ' + selected_candidate[:10], 0, 30, False)
                    if wifi_connected and send_vote_to_google_sheets(card_id, selected_candidate):
                        voted_rfids.add(card_id)
                        word_text('Vote Confirmed!', 0, 40, False)
                        green_led.value(1)
                        beep()
                    else:
                        word_text('Vote Failed', 0, 40, False)
                        red_led.value(1)
                    sleep(3)
                else:
                    word_text('No Vote Cast', 0, 30, False)
                    red_led.value(1)
                    sleep(2)
            else:
                word_text('Access Denied', 0, 10, True)
                if card_id in voted_rfids:
                    word_text('Already Voted', 0, 20, False)
                red_led.value(1)
                green_led.value(0)
                sleep(2)

            green_led.value(0)
            red_led.value(0)
            word_text('Scan RFID', 10, 10, True)
