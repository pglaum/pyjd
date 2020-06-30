from .jd import make_request
from .jd_types import SubscriptionResponse, PublisherResponse

endpoint = 'events'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def add_subscription(subscription_id, subscriptions, exclusions):

    params = [subscription_id, subscriptions, exclusions]
    resp = action("/addsubscription", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def change_subscription_timeouts(subscription_id, poll_timeout, keep_alive):

    params = [subscription_id, poll_timeout, keep_alive]
    resp = action("/changesubscriptiontimeouts", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def get_subscription(subscription_id):

    params = [subscription_id]
    resp = action("/getsubscription", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def listen(subscription_id):

    params = [subscription_id]
    resp = action("/listen", params)
    return resp


def list_publisher():

    resp = action("/listpublisher")

    publisher_responses = []
    for response in resp:
        publisher_response = PublisherResponse(response)
        publisher_responses.append(publisher_response)

    return publisher_responses


def remove_subscription(subscription_id, subscriptions, exclusions):

    params = [subscription_id, subscriptions, exclusions]
    resp = action("/removesubscription", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def set_subscription(subscription_id, subscriptions, exclusions):

    params = [subscription_id, subscriptions, exclusions]
    resp = action("/setsubscription", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def subscribe(subscriptions, exclusions):

    params = [subscriptions, exclusions]
    resp = action("/subscribe", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response


def unsubscribe(subscription_id):

    params = [subscription_id]
    resp = action("/unsubscribe", params)
    subscription_response = SubscriptionResponse(resp)
    return subscription_response
