import time
import network
import urequests

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)

# Reset WiFi interface
wifi.active(False)
time.sleep(1)

wifi.active(True)
time.sleep(1)



if not wifi.isconnected():
    print("Connecting to WiFi...")
    wifi.connect(SSID, PASSWORD)

    # Wait for connection
    timeout = 15
    while not wifi.isconnected() and timeout > 0:
        print(".")
        time.sleep(1)
        timeout -= 1

# Check connection
if wifi.isconnected():
    print("Connected!")
    print("IP Address:", wifi.ifconfig()[0])

    # Send HTTP GET request
    url = "http://httpbin.org/get"

    try:
        response = urequests.get(url)

        print("Status:", response.status_code)
        print("Response:")
        print(response.text)

        response.close()

    except Exception as e:
        print("HTTP request failed:", e)

else:
    print("WiFi connection failed")



