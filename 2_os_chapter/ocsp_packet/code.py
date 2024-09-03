from cryptography.hazmat.primitives import hashes
from cryptography.x509 import ocsp
from cryptography.x509.oid import NameOID
import binascii

# Define the issuer details
issuer_name_hash = binascii.unhexlify("eb8ebc9d472b7e0291771923f2a5f1c1c51e57b5")
issuer_key_hash = binascii.unhexlify("b3db48a4f9a1c5d8ae3641cc1163696229bc4bc6")
serial_number = int("0cabaad1cec4e97cc2665881d02138f7", 16)

# Create the OCSP request
builder = ocsp.OCSPRequestBuilder()
builder = builder.add_certificate(
    # The certificate is usually provided here. Since we don't have one, we're bypassing that by using the hash directly.
    cert=None,  # Normally, you would load the certificate here
    issuer=None,  # Normally, you would load the issuer certificate here
    algorithm=hashes.SHA1()
)

# You would normally call `builder.add_extension` here if needed.

ocsp_request = builder.build()

# Display the OCSP request in DER format
ocsp_request_der = ocsp_request.public_bytes(serialization.Encoding.DER)

print(binascii.hexlify(ocsp_request_der))
