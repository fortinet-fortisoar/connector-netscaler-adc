"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json

import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('netscaler-adc')


class Netscaler:
    def __init__(self, config):
        self.server_url = config.get('server_url')
        if not (self.server_url.startswith('https://') or self.server_url.startswith('http://')):
            self.server_url = 'https://' + self.server_url
        self.server_url = self.server_url.strip('/')
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None):
        try:
            url = self.server_url + endpoint
            logger.info('Executing url {}'.format(url))
            headers = {'Cookie': f"NITRO_AUTH_TOKEN={self.api_key}", 'Content-Type': 'application/json'}

            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl)
            if response.ok:
                logger.info('Successfully got response for url {}'.format(url))
                if method.upper() == 'DELETE':
                    return response
                else:
                    return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 401:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 404:
                error_response = response.json()
                raise ConnectorError(error_response)
            else:
                logger.error(response.json())
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            raise ConnectorError(str(err))
        raise ConnectorError(response.text)


def create_acl_resource(config: dict, params: dict):
    try:
        ns = Netscaler(config)
        params = _build_payload(params)
        endpoint = '/nitro/v1/config/nsacl'

        return ns.make_request(endpoint=endpoint, method='POST', data=json.dumps({"nsacl":params}))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_acl_resource(config: dict, params: dict):
    try:
        ns = Netscaler(config)
        params = _build_payload(params)
        endpoint = f"/nitro/v1/config/nsacl/{params.pop('aclname')}" if params.get(
            'aclname') is not None else '/nitro/v1/config/nsacl'

        return ns.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def delete_acl_resource(config: dict, params: dict):
    try:
        ns = Netscaler(config)
        params = _build_payload(params)
        endpoint = f"/nitro/v1/config/nsacl/{params.pop('aclname')}"

        return ns.make_request(endpoint=endpoint, method='DELETE', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def change_acl_resource_state(config: dict, params: dict):
    try:
        ns = Netscaler(config)
        params = _build_payload(params)
        endpoint = "/nitro/v1/config/nsacl"

        return ns.make_request(endpoint=endpoint, method='POST', data=json.loads({"nsacl": params}))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _check_health(config):
    try:
        tg = Netscaler(config)
        endpoint = '/nitro/v1/config/nsacl'
        response = tg.make_request(endpoint=endpoint, params={'pageno': 1})
        if response:
            logger.info("NetScaler ADC Connector Available")
            return True
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _build_payload(params: dict) -> dict:
    if params.get('other_fields') is not None:
        params.update(params.pop('other_fields'))

    return {key: val for key, val in params.items() if isinstance(val, (bool, int)) or val}


operations = {
    "create_acl_resource": create_acl_resource,
    "get_acl_resource": get_acl_resource,
    "delete_acl_resource": delete_acl_resource,
    "change_acl_resource_state": change_acl_resource_state
}