"""
Events & Subscriptions
======================

The workflow for using events is this:

1. Subscribe to an event publisher, using :func:`subscribe`
    You can choose publishers (and exclusions) from the information that
    :func:`list_publisher` returns.

    Note the subscription_id, that :func:`subscribe` returns to you
2. Now call :func:`listen` in a while loop.
    The request will be open for as long as keep_alive timeout is set or an
    event happens.
    If the timeout is reached, re-send the request.
    When you receive an event, you can act upon it and re-send the request.
3. You can always add or remove subscriptions/exclusions with your
    subscription_id.
    You can also change the poll and keep-alive timeouts.
4. When your done, call :func:`unsubscribe`.
    If you do not do that, JDownloader will delete the subscription after some
    time has passed.

.. note:: If you do not want to have a loss of actuality in your application,
    subscribe _before_ you load your data. Otherwise it can happen, that there
    has been a change of content between you loading the data and then
    subscribing (especially if done over network).

"""

from .jd_types import SubscriptionResponse, PublisherResponse
from typing import Optional, Any, List


class Events:
    def __init__(self, device):
        self.device = device
        self.endpoint = "events"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def add_subscription(
        self,
        subscription_id: int,
        subscriptions: List[str] = [],
        exclusions: List[str] = [],
    ) -> SubscriptionResponse:
        """Add subscriptions/exclusions to an existing Subscription.

        :param subscription_id: Subscription ID, handed out by
            :func:`subscribe`
        :type subscription_id: int
        :param subscriptions: A list of event publishers
        :type subscriptions: List[str]
        :param exclusions: A list of excluded events
        :type exclusions: List[str]
        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscription_id, subscriptions, exclusions]
        resp = self.action("/addsubscription", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def change_subscription_timeouts(
        self, subscription_id: int, poll_timeout: int, keep_alive: int
    ) -> SubscriptionResponse:
        """Change subscription timeouts for a subcription.

        :param subscription_id: Subscription ID, handed out by
            :func:`subscribe`
        :type subscription_id: int
        :param poll_timeout: Timeout after which a request closes, if there has
            been no event
        :type poll_timeout: int
        :param keep_alive: Timeout for keeping a subscription alive
        :type keep_alive: int
        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscription_id, poll_timeout, keep_alive]
        resp = self.action("/changesubscriptiontimeouts", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def get_subscription(self, subscription_id: int) -> SubscriptionResponse:
        """Get a Subscription object by id.

        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscription_id]
        resp = self.action("/getsubscription", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def listen(self, subscription_id: int) -> List[dict]:
        """Listen for events for a subscription.

        :param subscription_id: The id for a subscription
        :type subscription_id: int
        :returns: A list of events, or if the poll_timeout is reached, nothing.
        :rtype: List[dict]
        """

        params = [subscription_id]
        resp = self.action("/listen", params)
        return resp

    def list_publisher(self) -> List[PublisherResponse]:
        """List all event publishers and their events."""

        resp = self.action("/listpublisher")

        publisher_responses = []
        for response in resp:
            publisher_response = PublisherResponse(**response)
            publisher_responses.append(publisher_response)

        return publisher_responses

    def remove_subscription(
        self,
        subscription_id: int,
        subscriptions: List[str] = [],
        exclusions: List[str] = [],
    ) -> SubscriptionResponse:
        """Remove subscriptions/exclusions to an existing Subscription.

        :param subscription_id: Subscription ID, handed out by
            :func:`subscribe`
        :type subscription_id: int
        :param subscriptions: A list of event publishers
        :type subscriptions: List[str]
        :param exclusions: A list of excluded events
        :type exclusions: List[str]
        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscription_id, subscriptions, exclusions]
        resp = self.action("/removesubscription", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def set_subscription(
        self,
        subscription_id: int,
        subscriptions: List[str] = [],
        exclusions: List[str] = [],
    ) -> SubscriptionResponse:
        """Set subscriptions/exclusions for an existing Subscription.

        :param subscription_id: Subscription ID, handed out by
            :func:`subscribe`
        :type subscription_id: int
        :param subscriptions: A list of event publishers
        :type subscriptions: List[str]
        :param exclusions: A list of excluded events
        :type exclusions: List[str]
        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscription_id, subscriptions, exclusions]
        resp = self.action("/setsubscription", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def subscribe(
        self, subscriptions: List[str] = [], exclusions: List[str] = []
    ) -> SubscriptionResponse:
        """Create a new subscription.

        :param subscriptions: A list of event publishers
        :type subscriptions: List[str]
        :param exclusions: A list of excluded events
        :type exclusions: List[str]
        :returns: A subscription object
        :rtype: Subscription
        """

        params = [subscriptions, exclusions]
        resp = self.action("/subscribe", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response

    def unsubscribe(self, subscription_id: int) -> SubscriptionResponse:
        """Create a new subscription.

        :param subscription_id: ID of the subscription that is terminated
        :type subscription_id: int
        :returns: A empty subscription object
        :rtype: Subscription
        """

        params = [subscription_id]
        resp = self.action("/unsubscribe", params)
        subscription_response = SubscriptionResponse(**resp)
        return subscription_response
