import base64
import secrets
import Authenticator

def generate_random_base32_secret(length):
    """
    Generates a random Base32 encoded secret.

    Args:
        length (int): The length of the desired secret. This should be a multiple of 8.

    Returns:
        str: A Base32 encoded secret string without padding.
    """
    random_bytes = secrets.token_bytes(length // 8 * 5)
    secret = base64.b32encode(random_bytes).decode('utf-8').rstrip('=')
    return secret

if __name__ == "__main__":
    length = 32
    secret_key = generate_random_base32_secret(length)
    print("Generated Base32 Secret Key:", secret_key)
    Authenticator.main(secret_key)
