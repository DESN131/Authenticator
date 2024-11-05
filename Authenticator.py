import hmac
import hashlib
import time
import base64
import struct

def get_totp_token(secret, interval=30, digits=6):
    """
    Generate a Time-based One-Time Password (TOTP) token.
    Args:
        secret (str): The base32 encoded secret key.
        interval (int, optional): The time interval in seconds for which the token is valid. Defaults to 30 seconds.
        digits (int, optional): The number of digits in the generated token. Defaults to 6 digits.
    Returns:
        str: The generated TOTP token as a zero-padded string.
    """
    key = base64.b32decode(secret, casefold=True)
    timestamp = int(time.time() / interval)
    msg = struct.pack(">Q", timestamp)
    hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    binary_code = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF
    otp = binary_code % (10 ** digits)
    
    return str(otp).zfill(digits)

def main(secret_key):
    otp = get_totp_token(secret_key)
    print("Your OTP is:", otp)
    # print("Time remaining:", int(30 - time.time() % 30), "seconds")

if __name__ == "__main__":
    secret_key = "DWRWFILCRXZ3IX4YQSCC2PF2RWXE2OZ5" 
    while True:
        if int(time.time() % 30) == 0:
            main(secret_key)
            time.sleep(1)