import ssl
import base64
import hashlib

from socket import create_connection
from OpenSSL.crypto import dump_publickey
from OpenSSL.crypto import load_certificate
from OpenSSL.crypto import FILETYPE_ASN1

def get_pinned_key():
    context = ssl.create_default_context()
    conn = context.wrap_socket(create_connection(("api.binance.com", 443)), 
                              server_hostname="api.binance.com")
    der_cert = conn.getpeercert(binary_form=True)
    conn.close()

    x509 = load_certificate(FILETYPE_ASN1, der_cert)
    pubkey_der = dump_publickey(FILETYPE_ASN1, x509.get_pubkey())
    
    return base64.b64encode(hashlib.sha256(pubkey_der).digest()).decode()

PINNED_PUBLIC_KEY = get_pinned_key()
CA_CERT_PATH = None

def verify_certificate(hostname, port=443):
    """Retrieve the certificate, extract the public key, and verify its hash."""
    # Establish an SSL connection
    context = ssl.create_default_context()
    conn = context.wrap_socket(create_connection((hostname, port)), server_hostname=hostname)
    
    # Get the certificate in DER format
    der_cert = conn.getpeercert(binary_form=True)
    conn.close()

    # Convert DER to X.509 certificate
    x509 = load_certificate(FILETYPE_ASN1, der_cert)

    # Extract public key
    pubkey_der = dump_publickey(FILETYPE_ASN1, x509.get_pubkey())

    # Compute the SHA-256 hash of the public key
    public_key_hash = base64.b64encode(hashlib.sha256(pubkey_der).digest()).decode()

    # Validate public key hash against the pinned key
    if public_key_hash != PINNED_PUBLIC_KEY:
        raise ssl.SSLError(f"Certificate pinning validation failed: expected {PINNED_PUBLIC_KEY}, got {public_key_hash}")

# CORREÇÃO: Classe corrigida
class PinnedSSLContext:
    def __init__(self, hostname):
        # Primeiro verifica o pinning do certificado
        verify_certificate(hostname)
        
        # Depois cria o contexto SSL normal
        self._context = ssl.create_default_context()
        if CA_CERT_PATH:
            self._context.load_verify_locations(CA_CERT_PATH)
    
    # Delegate para o contexto real
    def __getattr__(self, name):
        return getattr(self._context, name)

ssl_context = PinnedSSLContext("api.binance.com")
