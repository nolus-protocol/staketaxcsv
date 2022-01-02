
import time
from osmo.api_util import _query_get
OSMO_DATA_API_NETLOC = "api-osmosis-chain.imperator.co"
LIMIT = 100


def _query(netloc, uri_path, query_params):
    result = _query_get(netloc, uri_path, query_params)
    time.sleep(1)
    return result


def get_count_txs(address):
    template = "/txs/v1/tx/count/{address}"
    uri_path = template.format(address=address)
    query_params = {}

    data = _query(OSMO_DATA_API_NETLOC, uri_path, query_params)

    return sum(row["count"] for row in data)


def get_txs(address, offset):
    template = "/txs/v1/tx/address/{address}"
    uri_path = template.format(address=address)
    query_params = {"limit": LIMIT}
    if offset:
        query_params["offset"] = offset

    data = _query(OSMO_DATA_API_NETLOC, uri_path, query_params)

    # Extract "tx_response" (found to be common data across multiple APIs)
    return [row["tx_response"] for row in data]


def get_lp_tokens(address):
    """ Returns list of symbols """
    template = "/lp/v1/rewards/token/{address}"
    uri_path = template.format(address=address)
    query_params = {}

    data = _query(OSMO_DATA_API_NETLOC, uri_path, query_params)

    return [kv["token"] for kv in data]


def get_lp_rewards(address, token):
    template = "/lp/v1/rewards/historical/{address}/{token}"
    uri_path = template.format(address=address, token=token)
    query_params = {}

    data = _query(OSMO_DATA_API_NETLOC, uri_path, query_params)

    return data