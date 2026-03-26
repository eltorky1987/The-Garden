import base64

# 🌹 This is a Cryptographic Logic for "The Garden"
def encrypt_message(message):
    encoded_bytes = base64.b64encode(message.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

print("--- System [The Garden] Initialized ---")
print("Target: Unauthorized User Detected")
print("Status: Rose Encryption Active...")

# تجربة الكود
my_message = "Your Session ID is now mine. 🌹"
print("Encrypted Result: ", encrypt_message(my_message))
