from enum import Enum
import json

# enums and constants


class BasicAuthType(Enum):
    FTP = "FTP"
    HTTP = "HTTP"


# structures and objects

class Account:
    def __init__(self, query_result):
        self.enabled = query_result['enabled'] \
            if 'enabled' in query_result \
            else None
        self.error_string = query_result['errorString'] \
            if 'errorString' in query_result \
            else None
        self.error_type = query_result['errorType'] \
            if 'errorType' in query_result \
            else None
        self.hostname = query_result['hostname'] \
            if 'hostname' in query_result \
            else None
        self.traffic_left = query_result['trafficLeft'] \
            if 'trafficLeft' in query_result \
            else None
        self.traffic_max = query_result['trafficMax'] \
            if 'trafficMax' in query_result \
            else None
        self.username = query_result['username'] \
            if 'username' in query_result \
            else None
        self.uuid = query_result['uuid'] \
            if 'uuid' in query_result \
            else None
        self.valid = query_result['valid'] \
            if 'valid' in query_result \
            else None
        self.valid_until = query_result['validUntil'] \
            if 'validUntil' in query_result \
            else None

    def __repr__(self):
        return f'<Account ({self.uuid})>'

    def to_dict(self):
        return {
            'enabled': self.enabled,
            'errorString': self.error_string,
            'errorType': self.error_type,
            'hostname': self.hostname,
            'trafficLeft': self.traffic_left,
            'trafficMax': self.traffic_max,
            'username': self.username,
            'uuid': self.uuid,
            'valid': self.valid,
            'validUntil': self.valid_until,
        }

    def to_json(self, pretty=False):
        if pretty:
            return json.dumps(self.to_dict(), indent=2)

        return json.dumps(self.to_dict())


class AccountQuery:
    def __init__(self, enabled=True, error=True, max_results=-1, start_at=0,
                 traffic_left=True, traffic_max=True, username=True,
                 uuid_list=None, valid=True, valid_until=True):
        self.enabled = enabled
        self.error = error
        self.max_results = max_results
        self.start_at = start_at
        self.traffic_left = traffic_left
        self.traffic_max = traffic_max
        self.username = username
        self.uuid_list = uuid_list
        self.valid = valid
        self.valid_until = valid_until

    def __repr__(self):
        return f'<AccountQuery ({self.uuid_list})>'

    def to_dict(self):
        return {
            'enabled': self.enabled,
            'error': self.error,
            'maxResults': self.max_results,
            'startAt': self.start_at,
            'trafficLeft': self.traffic_left,
            'trafficMax': self.traffic_max,
            'userName': self.username,
            'uuidlist': self.uuid_list,
            'valid': self.valid,
            'validUntil': self.valid_until,
        }


class BasicAuth:
    def __init__(self, qdict):
        self.created = qdict['created'] \
            if 'created' in qdict \
            else None
        self.enabled = qdict['enabled'] \
            if 'enabled' in qdict \
            else None
        self.hostmask = qdict['hostmask'] \
            if 'hostmask' in qdict \
            else None
        self.id = qdict['id'] \
            if 'id' in qdict \
            else None
        self.last_validated = qdict['lastValidated'] \
            if 'lastValidated' in qdict \
            else None
        self.password = qdict['password'] \
            if 'password' in qdict \
            else None
        self.auth_type = BasicAuthType(qdict['type']) \
            if 'type' in qdict \
            else None
        self.username = qdict['username'] \
            if 'username' in qdict \
            else None

    def __repr__(self):
        return f'<BasicAuth ({self.id})>'

    def to_dict(self):
        return {
            'created': self.created,
            'enabled': self.enabled,
            'hostmask': self.hostmask,
            'id': self.id,
            'lastValidated': self.last_validated,
            'password': self.password,
            'type': self.auth_type.value,
            'username': self.username,
        }
