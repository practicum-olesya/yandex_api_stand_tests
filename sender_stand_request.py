import requests
import configuration
import data


def create_order():
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_ORDER_PATH,
        json=data.ORDER_BODY
    )


def get_order_by_track(track):
    params = {"t": track}
    return requests.get(
        configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK_PATH,
        params=params
    )
