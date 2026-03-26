import platform
import socket
import datetime
import os

# 🌹 Garden System Scanner V1.0 -- Monitoring Unit
def run_garden_scan():
    print("\n" + "="*40)
    print("      🌹 GARDEN SYSTEM AUDIT START 🌹")
    print("="*40)
    print(f"Timestamp: {datetime.datetime.now()}")
    
    # معلومات نظام التشغيل
    print("\n[+] Operating System Information:")
    print(f"    - System: {platform.system()}")
    print(f"    - Node Name: {platform.node()}")
    print(f"    - Release: {platform.release()}")
    print(f"    - Version: {platform.version()}")
    print(f"    - Machine: {platform.machine()}")
    
    # معلومات الشبكة
    print("\n[+] Network Fingerprint:")
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"    - Hostname: {hostname}")
        print(f"    - Local IP: {local_ip} (Internal)")
    except Exception as e:
        print(f"    - Network Info: Error retrieving [Session Logged]")

    # معلومات إضافية (اختياري، للرعب)
    print("\n[+] Environment Status:")
    print(f"    - Process ID: {os.getpid()}")
    
    print("\n" + "="*40)
    print("      🌹 SCAN COMPLETE -- LOGS SECURED 🌹")
    print("="*40 + "\n")

if __name__ == "__main__":
    # هذا الكود يُظهر لك أن المعلومات التي تظنها مخفية، هي متاحة لمن يملك المفتاح.
    run_garden_scan()
  
