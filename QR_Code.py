import qrcode
import base64


def generate_qr_code(secret, account_name, issuer_name):
    """
    Generates and displays a QR code for a given secret, account name, and issuer name.
    Args:
        secret (str): The secret key used for generating the OTP.
        account_name (str): The name of the account associated with the OTP.
        issuer_name (str): The name of the issuer providing the OTP.
    Returns:
        None
    """

    otpauth_url = f"otpauth://totp/{issuer_name}:{account_name}?secret={secret}&issuer={issuer_name}"

    qr = qrcode.make(otpauth_url)

    qr.show()

if __name__ == "__main__":
    secret_key = "DWRWFILCRXZ3IX4YQSCC2PF2RWXE2OZ5" 
    account_name = "name"
    issuer_name = "name"

    generate_qr_code(secret_key, account_name, issuer_name)
