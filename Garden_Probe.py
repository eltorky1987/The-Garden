import time
import sys
import random

# 🌹 Garden Monitoring Unit - Probe Sequence
def garden_illusion():
    print("--- [INITIALIZING GARDEN PROBE V2.1] ---")
    print("Target: Unauthorized Connection Detected.")
    time.sleep(1)
    
    # رسائل وهمية لزوم الهيبة
    sequences = [
        "Scanning local ports...",
        "Identifying User OS Fingerprint...",
        "Bypassing standard firewall protocols...",
        "Injecting Rose_Signature.bin...",
        "Establishing persistent link to The Garden... 🌹"
    ]

    for step in sequences:
        sys.stdout.write(f"\r[PROCESSING] {step}")
        sys.stdout.flush()
        # وقت عشوائي عشان يبان إنه بيحمل بجد
        time.sleep(random.uniform(0.7, 2.0))
        sys.stdout.write(f"\r[SUCCESS] {step}\n")
        
    print("\n" + "!"*40)
    print("STATUS: TARGET MARKED & LOGGED")
    print(f"SESSION_ID: {random.randint(100000, 999999)}")
    print("Welcome to the Garden. We see you. 🌹")
    print("!"*40 + "\n")

if __name__ == "__main__":
    garden_illusion()
