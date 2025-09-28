import ssl
import base64
import hashlib

from ssl import Purpose
from socket import create_connection
from socket import _GLOBAL_DEFAULT_TIMEOUT
from OpenSSL.crypto import dump_publickey
from OpenSSL.crypto import load_certificate
from OpenSSL.crypto import FILETYPE_ASN1

def _get_server_certificate_pubkey(hostname: str, port=443):
    """
    Description:
        Helper function to get the public key from server certificate.
    """
    context = ssl.create_default_context(
        purpose=Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None
    )
    
    conn = context.wrap_socket(
        sock=create_connection(
            address=(hostname, port), timeout=_GLOBAL_DEFAULT_TIMEOUT,
            source_address=None, all_errors=False
        ),
        server_side=False, do_handshake_on_connect=True, 
        suppress_ragged_eofs=True, server_hostname=hostname, session=None
    )
    
    der_cert = conn.getpeercert(binary_form=True)
    conn.close()

    x509 = load_certificate(type=FILETYPE_ASN1, buffer=der_cert)
    pubkey_der = dump_publickey(type=FILETYPE_ASN1, pkey=x509.get_pubkey())
    
    return pubkey_der


def _calculate_public_key_hash(pubkey_der: str):
    """
    Description:
        Calculate the SHA256 hash of the public key in base64 format.
    """
    return base64.b64encode(
        hashlib.sha256(string=pubkey_der, usedforsecurity=True).digest()
    ).decode(encoding="utf-8", errors="strict")


def get_pinned_key():
    """
    Description:
        Get a pinned key to be used in certificate pinning.
    """
    pubkey_der = _get_server_certificate_pubkey(
        hostname="api.binance.com", port = 443)
    return _calculate_public_key_hash(pubkey_der)


PINNED_PUBLIC_KEY = get_pinned_key()
CA_CERT_PATH = None


def verify_certificate(hostname: str, port: int = 443):
    """
    Description:
        Retrieve the certificate, extract the public key, and verify its hash.
    """
    pubkey_der = _get_server_certificate_pubkey(hostname, port)
    public_key_hash = _calculate_public_key_hash(pubkey_der)

    if public_key_hash != PINNED_PUBLIC_KEY:
        raise ssl.SSLError(
            OSError=f"Certificate pinning validation failed: \
                expected {PINNED_PUBLIC_KEY}, got {public_key_hash}"
        )

class PinnedSSLContext:
    def __init__(self, hostname: str):
        # Primeiro verifica o pinning do certificado
        verify_certificate(hostname)
        
        # Depois cria o contexto SSL normal
        self._context = ssl.create_default_context()
        if CA_CERT_PATH:
            self._context.load_verify_locations(
                cafile = None, capath = CA_CERT_PATH, cadata = None)
    
    # Delegate para o contexto real
    def __getattr__(self, name):
        return getattr(self._context, name)


ssl_context = PinnedSSLContext("api.binance.com")
