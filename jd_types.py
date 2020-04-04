from enum import Enum
import json


# enums and constants
class Action(Enum):
    DELETE_ALL = "DELETE_ALL"
    DELETE_DISABLED = "DELETE_DISABLED"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_FINISHED = "DELETE_FINISHED"
    DELETE_DUPE = "DELETE_DUPE"
    DELETE_MODE = "DELETE_MODE"


class AvailableLinkState(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    UNKNOWN = "UNKNOWN"
    TEMP_UNKNOWN = "TEMP_UNKNOWN"


class BasicAuthType(Enum):
    FTP = "FTP"
    HTTP = "HTTP"


class Mode(Enum):
    REMOVE_LINKS_AND_DELETE_FILES = "REMOVE_LINKS_AND_DELETE_FILES"
    REMOVE_LINKS_AND_RECYCLE_FILES = "REMOVE_LINKS_AND_RECYCLE_FILES"
    REMOVE_LINKS_ONLY = "REMOVE_LINKS_ONLY"


class Priority(Enum):
    HIGHEST = "HIGHEST"
    HIGHER = "HIGHER"
    HIGH = "HIGH"
    DEFAULT = "DEFAULT"
    LOW = "LOW"
    LOWER = "LOWER"
    LOWEST = "LOWEST"


class SelectionType(Enum):
    SELECTED = "SELECTED"
    UNSELECTED = "UNSELECTED"
    ALL = "ALL"
    NONE = "NONE"


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


class AddLinksQuery:
    def __init__(self, assign_job_id=None, auto_extract=None, auto_start=None,
                 data_urls=[], deep_decrypt=None, destination_folder=None,
                 download_password=None, extract_password=None, links=None,
                 overwrite_packagizer_rules=None, package_name=None,
                 priority=Priority.DEFAULT, source_url=None):
        self.assign_job_id = assign_job_id
        self.auto_extract = auto_extract
        self.auto_start = auto_start
        self.data_urls = data_urls
        self.deep_decrypt = deep_decrypt
        self.destination_folder = destination_folder
        self.download_password = download_password
        self.extract_password = extract_password
        self.links = links
        self.overwrite_packagizer_rules = overwrite_packagizer_rules
        self.package_name = package_name
        self.priority = priority
        self.source_url = source_url

    def __repr__(self):
        return f'<AddLinksQuery ({self.package_name})>'

    def to_dict(self):
        return {
            'assignJobID': self.assign_job_id,
            'autoExtract': self.auto_extract,
            'autostart': self.auto_start,
            'dataURLs': self.data_urls,
            'deepDecrypt': self.deep_decrypt,
            'destinationFolder': self.destination_folder,
            'downloadPassword': self.download_password,
            'extractPassword': self.extract_password,
            'links': self.links,
            'overwritePackagizerRules': self.overwrite_packagizer_rules,
            'packageName': self.package_name,
            'priority': self.priority.value,
            'sourceUrl': self.source_url,
        }

    def to_json(self, pretty=False):
        if pretty:
            return json.dumps(self.to_dict(), indent=2)

        return json.dumps(self.to_dict())


class CrawledLink:
    def __init__(self, qdict):
        self.availability = AvailableLinkState(qdict['availability']) \
            if 'availability' in qdict \
            else None
        self.bytes_total = qdict['bytesTotal'] \
            if 'bytesTotal' in qdict \
            else None
        self.comment = qdict['comment'] \
            if 'comment' in qdict \
            else None
        self.download_password = qdict['downloadPassword'] \
            if 'downloadPassword' in qdict \
            else None
        self.enabled = qdict['enabled'] \
            if 'enabled' in qdict \
            else None
        self.host = qdict['host'] \
            if 'host' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None
        self.package_uuid = qdict['packageUUID'] \
            if 'packageUUID' in qdict \
            else None
        self.priority = Priority(qdict['priority']) \
            if 'priority' in qdict \
            else None
        self.url = qdict['url'] \
            if 'url' in qdict \
            else None
        self.uuid = qdict['uuid'] \
            if 'uuid' in qdict \
            else None
        self.variant = LinkVariant(qdict['variant']) \
            if 'variant' in qdict \
            else None
        self.variants = qdict['variants'] \
            if 'variants' in qdict \
            else None

    def __repr__(self):
        return f'<CrawledLink ({self.uuid})>'

    def to_dict(self):
        return {
            'availability': self.availability.value,
            'bytesTotal': self.bytes_total,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'host': self.host,
            'name': self.name,
            'packageUUID': self.package_uuid,
            'priority': self.priority.value,
            'url': self.url,
            'uuid': self.uuid,
            'variant': self.variant.to_json(),
            'variants': self.variants,
        }


class CrawledLinkQuery:
    def __init__(self, availability=True, bytes_total=True, comment=True,
                 enabled=True, host=True, job_uuids=None, max_results=-1,
                 package_uuids=None, password=True, priority=True, start_at=0,
                 status=True, url=True, variant_id=True, variant_icon=True,
                 variant_name=True, variants=True):
        self.availability = availability
        self.bytes_total = bytes_total
        self.comment = comment
        self.enabled = enabled
        self.host = host
        self.job_uuids = job_uuids
        self.max_results = max_results
        self.package_uuids = package_uuids
        self.password = password
        self.priority = priority
        self.start_at = start_at
        self.status = status
        self.url = url
        self.variant_id = variant_id
        self.variant_icon = variant_icon
        self.variant_name = variant_name
        self.variants = variants

    def __repr__(self):
        return f'<CrawledLinkQuery>'

    def to_dict(self):
        return {
            'availability': self.availability,
            'bytesTotal': self.bytes_total,
            'comment': self.comment,
            'enabled': self.enabled,
            'host': self.host,
            'jobUUIDs': self.job_uuids,
            'maxResults': self.max_results,
            'packageUUIDs': self.package_uuids,
            'password': self.password,
            'priority': self.priority,
            'startAt': self.startAt,
            'status': self.status,
            'url': self.url,
            'variantID': self.variant_id,
            'variantIcon': self.variant_icon,
            'variantName': self.variant_name,
            'variants': self.variants,
        }


class CrawledPackage:
    def __init__(self, qdict):
        self.bytes_total = qdict['bytesTotal'] \
            if 'bytesTotal' in qdict \
            else None
        self.child_count = qdict['childCount'] \
            if 'childCount' in qdict \
            else None
        self.comment = qdict['comment'] \
            if 'comment' in qdict \
            else None
        self.download_password = qdict['downloadPassword'] \
            if 'downloadPassword' in qdict \
            else None
        self.enabled = qdict['enabled'] \
            if 'enabled' in qdict \
            else None
        self.hosts = qdict['hosts'] \
            if 'hosts' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None
        self.offline_count = qdict['offlineCount'] \
            if 'offlineCount' in qdict \
            else None
        self.online_count = qdict['onlineCount'] \
            if 'onlineCount' in qdict \
            else None
        self.priority = Priority(qdict['priority']) \
            if 'priority' in qdict \
            else None
        self.save_to = qdict['saveTo'] \
            if 'saveTo' in qdict \
            else None
        self.temp_unknown_count = qdict['tempUnkownCount'] \
            if 'tempUnkownCount' in qdict \
            else None
        self.unkownCount = qdict['unknownCount'] \
            if 'unknownCount' in qdict \
            else None
        self.uuid = qdict['uuid'] \
            if 'uuid' in qdict \
            else None

    def __repr__(self):
        return f'<CrawledPackage ({self.uuid})'

    def to_dict(self):
        return {
            'bytesTotal': self.bytes_total,
            'childCount': self.child_count,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'hosts': self.hosts,
            'name': self.name,
            'offlineCount': self.offline_count,
            'onlineCount': self.online_count,
            'priority': self.priority.value,
            'saveTo': self.save_to,
            'tempUnknownCount': self.temp_unknown_count,
            'unknownCount': self.unkownCount,
            'uuid': self.uuid,
        }


class CrawledPackageQuery:
    def __init__(self, available_offline_count=True,
                 available_online_count=True,
                 available_temp_unknown_count=True,
                 available_unknown_count=True, bytes_total=True,
                 child_count=True, comment=True, enabled=True, hosts=True,
                 max_results=-1, package_uuids=None, priority=True,
                 save_to=True, start_at=0, status=True):
        self.available_offline_count = available_offline_count
        self.available_online_count = available_online_count
        self.available_temp_unknown_count = available_temp_unknown_count
        self.available_unknown_count = available_unknown_count
        self.bytes_total = bytes_total
        self.child_count = child_count
        self.comment = comment
        self.enabled = enabled
        self.hosts = hosts
        self.max_results = max_results
        self.package_uuids = package_uuids
        self.priority = priority
        self.save_to = save_to
        self.start_at = start_at
        self.status = status

    def __repr__(self):
        return '<CrawledPackageQuery>'

    def to_dict(self):
        return {
            'availableOfflineCount': self.available_offline_count,
            'availableOnlineCount': self.available_online_count,
            'availableTempUnknownCount': self.available_temp_unknown_count,
            'availableUnknownCount': self.available_unknown_count,
            'bytesTotal': self.bytes_total,
            'childCount': self.child_count,
            'comment': self.comment,
            'enabled': self.enabled,
            'hosts': self.hosts,
            'maxResults': self.max_results,
            'packageUUIDs': self.package_uuids,
            'priority': self.priority,
            'saveTo': self.save_to,
            'startAt': self.start_at,
            'status': self.status,
        }


class JobLinkCrawler:
    def __init__(self, qdict):
        self.broken = qdict['broken'] \
            if 'broken' in qdict \
            else None
        self.checking = qdict['checking'] \
            if 'checking' in qdict \
            else None
        self.crawled = qdict['crawled'] \
            if 'crawled' in qdict \
            else None
        self.crawler_id = qdict['crawledId'] \
            if 'crawledId' in qdict \
            else None
        self.crawling = qdict['crawling'] \
            if 'crawling' in qdict \
            else None
        self.filtered = qdict['filtered'] \
            if 'filtered' in qdict \
            else None
        self.job_id = qdict['jobId'] \
            if 'jobId' in qdict \
            else None
        self.unhandled = qdict['unhandled'] \
            if 'unhandled' in qdict \
            else None

    def __repr__(self):
        return f'<JobLinkCrawler ({self.crawler_id})>'

    def to_dict(self):
        return {
            'broken': self.broken,
            'checking': self.checking,
            'crawled': self.crawled,
            'crawlerId': self.crawler_id,
            'crawling': self.crawling,
            'filtered': self.filtered,
            'jobId': self.job_id,
            'unhandled': self.unhandled,
        }


class LinkCollectingJob:
    def __init__(self, qdict):
        self.id = qdict['id'] \
            if 'id' in qdict \
            else None

    def __repr__(self):
        return f'<LinkCollectingJob ({self.id})>'

    def to_dict(self):
        return {
            'id': self.id
        }


class LinkCrawlerJobsQuery:
    def __init__(self, collector_info=True, job_ids=None):
        self.collector_info = collector_info
        self.job_ids = job_ids

    def __repr__(self):
        return f'<LinkCrawlerJobsQuery>'

    def to_dict(self):
        return {
            'collectorInfo': self.collector_info,
            'jobIds': self.job_ids,
        }


class LinkVariant:
    def __init__(self, qdict):
        self.icon_key = qdict['iconKey'] \
            if 'iconKey' in qdict \
            else None
        self.id = qdict['id'] \
            if 'id' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None

    def __repr__(self):
        return f'<LinkVariant ({self.id})>'

    def to_dict(self):
        return {
            'iconKey': self.icon_key,
            'id': self.id,
            'name': self.name,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class LogFolder:
    def __init__(self, qdict):
        self.created = qdict['created'] \
            if 'created' in qdict \
            else None
        self.current = qdict['current'] \
            if 'current' in qdict \
            else None
        self.last_modified = qdict['lastModified'] \
            if 'lastModified' in qdict \
            else None

    def __repr__(self):
        return f'<LogFolder>'

    def to_dict(self):
        return {
            'created': self.created,
            'current': self.current,
            'lastModified': self.last_modified,
        }
