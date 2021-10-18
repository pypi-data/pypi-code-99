import os

GRPC_ENDPOINT = os.getenv('GRPC_ENDPOINT', '127.0.0.1:9090')
MEMO = os.getenv('MEMO', 'Sent from Hanchon\'s faucet')
FEE = os.getenv('FEE', '20')
GAS_LIMIT = os.getenv('GAS_LIMIT', '200000')
CHAIN_ID = os.getenv('CHAIN_ID', 'evmos_9000-1')
DENOM = os.getenv('DENOM', 'aphoton')
