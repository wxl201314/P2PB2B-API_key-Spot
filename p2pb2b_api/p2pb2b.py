from hmac import new as hmac_new
from hashlib import sha512
from base64 import b64encode
from json import dumps
from time import time

from requests import get
from requests import post

from .exceptions import *

class Api:
    '''
    ### Public

    - public
        - markets
            (no parameters)
        - market
            Name   | Type   | Mandatory
            ------ | ------ | ---------
            market | STRING | YES
            - kline
                Name     | Type   | Mandatory
                -------- | ------ | ---------
                market   | STRING | YES
                interval | ENUM   | YES
                offset   | INT    | NO
                limit    | INT    | NO
        - tickers
            (no parameters)
        - ticker
            Name   | Type   | Mandatory
            ------ | ------ | ---------
            market | STRING | YES
        - book
            Name   | Type   | Mandatory
            ------ | ------ | ---------
            market | STRING | YES
            side   | STRING | YES
            offset | INT    | NO
            limit  | INT    | NO
        - history
            Name   | Type   | Mandatory
            ------ | ------ | ---------
            market | STRING | YES
            lastId | INT    | YES
            limit  | INT    | NO
        - depth
            - result
                Name     | Type   | Mandatory
                -------- | ------ | ---------
                market   | STRING | YES
                limit    | INT    | NO
                interval | ENUM   | NO

    ### Protected

    - account
        - balances
            (no parameters)
        - balance
            Name     | Type   | Mandatory
            -------- | ------ | ---------
            currency | STRING | YES
        - order_history
            (no parameters)
        - order
            Name    |Type | Mandatory
            ------- | --- | ---------
            orderId | INT | YES
            offset  | INT | NO
            limit   | INT | NO
        - executed_history
            Name   | Type   | Mandatory
            ----   | ------ | ---------
            market | STRING | YES
            offset | INT    | NO
            limit  | INT    | NO
            - all
                Name   | Type | Mandatory
                ------ | ---- | ---------
                limit  | INT  | NO
                offset | INT  | NO
    - orders
        Name   | Type   | Mandatory
        ------ | ------ | ---------
        market | STRING | YES
        offset | INT    | NO
        limit  | INT    | NO
        - new
            Name   | Type   | Mandatory
            ------ | ------ | ---------
            market | STRING | YES
            side   | STRING | YES
            amount | STRING | TES
            price  | STRING | YES
        - cancel
            Name    | Type   | Mandatory
            ------  |------- | ---------
            market  | STRING | YES
            orderId | INT    | YES
            - all
                Name   | Type   | Mandatory
                ------ | ------ | ---------
                market | STRING | YES

    https://github.com/P2pb2b-team/p2pb2b-api-docs
    '''

    URL = 'https://api.p2pb2b.io'
    API = '/api/v2'

    def __init__(self, key=None, secret=None, _method=''):
        self.key = key
        self.secret = secret

        self._method = _method

    def _public_request(self, endpoint, data):
        return get(self.URL + endpoint, data)

    def _protected_request(self, endpoint, data):
        data.update({
            'request': endpoint,
            'nonce': int(time())
        })

        data = dumps(data, separators=(',', ':'))
        payload = b64encode(data.encode())
        signature = hmac_new(self.secret.encode(), payload, sha512)

        headers = {
            'Content-type': 'application/json',
            'X-TXC-APIKEY': self.key,
            'X-TXC-PAYLOAD': payload.decode(),
            'X-TXC-SIGNATURE': signature.hexdigest()
        }

        return post(self.URL + endpoint, data, headers=headers)

    def _request(self, data):
        endpoint = self.API + self._method

        if 'public' in self._method:
            return self._public_request(endpoint, data)
        return self._protected_request(endpoint, data)

    def __getattr__(self, method):
        return Api(
            self.key, self.secret, self._method + '/' + method)

    def __call__(self, **kwargs):
        response = self._request(kwargs)

        if response.status_code == 404:
            raise NotFound(self._method)

        return response.json()
