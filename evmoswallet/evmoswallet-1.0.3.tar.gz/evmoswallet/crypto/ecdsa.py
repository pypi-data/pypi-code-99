try:
    from evmoswallet.crypto import ecdsa_openssl as _ecdsa
except Exception:
    from evmoswallet.crypto import ecdsa_python as _ecdsa

ECPointAffine = _ecdsa.ECPointAffine
EllipticCurve = _ecdsa.EllipticCurve
secp256k1 = _ecdsa.secp256k1
