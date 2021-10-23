from decouple import config

TRACKING_URI = config('TRACKING_URI', default='')
SERVER_IP = config('SERVER_IP', default='')
SERVER_PORT = config('SERVER_PORT', default='')
HOUSE_PRICES_PORT_STAGE = config('HOUSE_PRICES_PORT_STAGE', default='')
HOUSE_PRICES_PORT_PRODUCTION = config(
    'HOUSE_PRICES_PORT_PRODUCTION', default=''
)
