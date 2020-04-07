from enum import Enum
import json


# enums and constants
class AbstractType(Enum):
    BOOLEAN = "BOOLEAN"
    INT = "INT"
    LONG = "LONG"
    STRING = "STRING"
    OBJECT = "OBJECT"
    OBJECT_LIST = "OBJECT_LIST"
    STRING_LIST = "STRING_LIST"
    ENUM = "ENUM"
    BYTE = "BYTE"
    CHAR = "CHAR"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    SHORT = "SHORT"
    BOOLEAN_LIST = "BOOLEAN_LIST"
    BYTE_LIST = "BYTE_LIST"
    SHORT_LIST = "SHORT_LIST"
    LONG_LIST = "LONG_LIST"
    INT_LIST = "INT_LIST"
    FLOAT_LIST = "FLOAT_LIST"
    ENUM_LIST = "ENUM_LIST"
    DOUBLE_LIST = "DOUBLE_LIST"
    CHAR_LIST = "CHAR_LIST"
    UNKNOWN = "UNKNOWN"
    HEX_COLOR = "HEX_COLOR"
    HEX_COLOR_LIST = "HEX_COLOR_LIST"
    ACTION = "ACTION"


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


class Reason(Enum):
    CONNECTION_UNAVAILABLE = "CONNECTION_UNAVAILABLE"
    TOO_MANY_RETRIES = "TOO_MANY_RETRIES"
    CAPTCHA = "CAPTCHA"
    MANUAL = "MANUAL"
    DISK_FULL = "DISK_FULL"
    NO_ACCOUNT = "NO_ACCOUNT"
    INVALID_DESTINATION = "INVALID_DESTINATION"
    FILE_EXISTS = "FILE_EXISTS"
    UPDATE_RESTART_REQUIRED = "UPDATE_RESTART_REQUIRED"
    FFMPEG_MISSING = "FFMPEG_MISSING"
    FFPROBE_MISSING = "FFPROBE_MISSING"


class SelectionType(Enum):
    SELECTED = "SELECTED"
    UNSELECTED = "UNSELECTED"
    ALL = "ALL"
    NONE = "NONE"


class SkipRequest(Enum):
    SINGLE = "SINGLE"
    BLOCK_HOSTER = "BLOCK_HOSTER"
    BLOCK_ALL_CAPTCHAS = "BLOCK_ALL_CAPTCHAS"
    BLOCK_PACKAGE = "BLOCK_PACKAGE"
    REFRESH = "REFRESH"
    STOP_CURRENT_ACTION = "STOP_CURRENT_ACTION"
    TIMEOUT = "TIMEOUT"


class Status(Enum):
    NA = "NA"
    PENDING = "PENDING"
    FINISHED = "FINISHED"


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


class AdvancedConfigAPIEntry:
    def __init__(self, qdict):
        self.abstract_type = AbstractType(qdict['abstractType']) \
            if 'abstract_type' in qdict \
            else None
        self.default_value = qdict['defaultValue'] \
            if 'defaultValue' in qdict \
            else None
        self.docs = qdict['docs'] \
            if 'docs' in qdict \
            else None
        self.enum_label = qdict['enumLabel'] \
            if 'enumLabel' in qdict \
            else None
        self.enum_options = qdict['enumOptions'] \
            if 'enumOptions' in qdict \
            else None
        self.interface_name = qdict['interfaceName'] \
            if 'interfaceName' in qdict \
            else None
        self.key = qdict['key'] \
            if 'key' in qdict \
            else None
        self.storage = qdict['storage'] \
            if 'storage' in qdict \
            else None
        self.config_type = qdict['type'] \
            if 'type' in qdict \
            else None
        self.value = qdict['value'] \
            if 'value' in qdict \
            else None

    def __repr__(self):
        return f'<AdvancedConfigAPIEntry ({self.key})>'

    def to_dict(self):
        result = {
            'defaultValue': self.default_value,
            'docs': self.docs,
            'enumLabel': self.enum_label,
            'enumOptions': self.enum_options,
            'interfaceName': self.interface_name,
            'key': self.key,
            'storage': self.storage,
            'type': self.config_type,
            'value': self.value,
        }

        if self.abstract_type:
            result['abstractType'] = self.abstract_type.value

        return result


class AdvancedConfigQuery:
    def __init__(self, config_interface=None, default_values=True,
                 description=True, enum_info=True, include_extensions=True,
                 pattern=None, values=True):
        self.config_interface = config_interface
        self.default_values = default_values
        self.description = description
        self.enum_info = enum_info
        self.include_extensions = include_extensions
        self.pattern = pattern
        self.values = values

    def __repr__(self):
        return f'<AdvancedConfigQuery ({self.config_interface})>'

    def to_dict(self):
        return {
            'configInterface': self.config_interface,
            'defaultValues': self.default_values,
            'description': self.description,
            'enumInfo': self.enum_info,
            'includeExtensions': self.include_extensions,
            'pattern': self.pattern,
            'values': self.values,
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


class CaptchaJob:
    def __init__(self, qdict):
        self.captcha_category = qdict['captchaCategory'] \
            if 'captchaCategory' in qdict \
            else None
        self.created = qdict['created'] \
            if 'created' in qdict \
            else None
        self.explain = qdict['explain'] \
            if 'explain' in qdict \
            else None
        self.hoster = qdict['hoster'] \
            if 'hoster' in qdict \
            else None
        self.captcha_id = qdict['id'] \
            if 'id' in qdict \
            else None
        self.link = qdict['link'] \
            if 'link' in qdict \
            else None
        self.timeout = qdict['timeout'] \
            if 'timeout' in qdict \
            else None
        self.captcha_type = qdict['type'] \
            if 'type' in qdict \
            else None

    def __repr__(self):
        return f'<CaptchaJob ({self.captcha_id})>'

    def to_dict(self):
        return {
            'captchaCategory': self.captcha_category,
            'created': self.created,
            'explain': self.explain,
            'hoster': self.hoster,
            'id': self.captcha_id,
            'link': self.link,
            'timeout': self.timeout,
            'type': self.captcha_type,
        }


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
        result = {
            'availability': self.availability.value,
            'bytesTotal': self.bytes_total,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'host': self.host,
            'name': self.name,
            'packageUUID': self.package_uuid,
            'url': self.url,
            'uuid': self.uuid,
            'variants': self.variants,
        }

        if self.priority:
            result['priority'] = self.priority.value

        if self.variant:
            result['variant'] = self.variant.to_json()

        return result


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
            'startAt': self.start_at,
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
        result = {
            'bytesTotal': self.bytes_total,
            'childCount': self.child_count,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'hosts': self.hosts,
            'name': self.name,
            'offlineCount': self.offline_count,
            'onlineCount': self.online_count,
            'saveTo': self.save_to,
            'tempUnknownCount': self.temp_unknown_count,
            'unknownCount': self.unkownCount,
            'uuid': self.uuid,
        }

        if self.priority:
            result['priority'] = self.priority.value

        return result


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


class DownloadLink:
    def __init__(self, qdict):
        self.added_date = qdict['addedDate'] \
            if 'addedDate' in qdict \
            else None
        self.bytes_loaded = qdict['bytesLoaded'] \
            if 'bytesLoaded' in qdict \
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
        self.eta = qdict['eta'] \
            if 'eta' in qdict \
            else None
        self.extraction_status = qdict['extractionStatus'] \
            if 'extractionStatus' in qdict \
            else None
        self.finished = qdict['finished'] \
            if 'finished' in qdict \
            else None
        self.finished_date = qdict['finishedDate'] \
            if 'finishedDate' in qdict \
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
        self.running = qdict['running'] \
            if 'running' in qdict \
            else None
        self.skipped = qdict['skipped'] \
            if 'skipped' in qdict \
            else None
        self.speed = qdict['speed'] \
            if 'speed' in qdict \
            else None
        self.status = qdict['status'] \
            if 'status' in qdict \
            else None
        self.status_icon_key = qdict['statusIconKey'] \
            if 'statusIconKey' in qdict \
            else None
        self.url = qdict['url'] \
            if 'url' in qdict \
            else None
        self.uuid = qdict['uuid'] \
            if 'uuid' in qdict \
            else None

    def __repr__(self):
        return f'<DownloadLink ({self.uuid})>'

    def to_dict(self):
        result = {
            'addedDate': self.added_date,
            'bytesLoaded': self.bytes_loaded,
            'bytesTotal': self.bytes_total,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'eta': self.eta,
            'extractionStatus': self.extraction_status,
            'finished': self.finished,
            'finishedDate': self.finished_date,
            'host': self.host,
            'name': self.name,
            'packageUUID': self.package_uuid,
            'running': self.running,
            'skipped': self.skipped,
            'speed': self.speed,
            'status': self.status,
            'statusIconKey': self.status_icon_key,
            'url': self.url,
            'uuid': self.uuid,
        }

        if self.priority:
            result['priority'] = self.priority.value

        return result


class EnumOption:
    def __init__(self, qdict):
        self.label = qdict['label'] \
            if 'label' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None

    def __repr__(self):
        return f'<EnumOption ({self.name})>'

    def to_dict(self):
        return {
            'label': self.label,
            'name': self.name,
        }


class Extension:
    def __init__(self, qdict):
        self.config_interface = qdict['configInterface'] \
            if 'configInterface' in qdict \
            else None
        self.description = qdict['description'] \
            if 'description' in qdict \
            else None
        self.enabled = qdict['enabled'] \
            if 'enabled' in qdict \
            else None
        self.icon_key = qdict['iconKey'] \
            if 'iconKey' in qdict \
            else None
        self.extension_id = qdict['id'] \
            if 'id' in qdict \
            else None
        self.installed = qdict['installed'] \
            if 'installed' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None

    def __repr__(self):
        return f'<Extension ({self.extension_id})>'

    def to_dict(self):
        return {
            'configInterface': self.config_interface,
            'description': self.description,
            'enabled': self.enabled,
            'iconKey': self.icon_key,
            'id': self.extension_id,
            'installed': self.installed,
            'name': self.name,
        }


class ExtensionQuery:
    def __init__(self, config_interface=True, description=True, enabled=True,
                 icon_key=True, installed=True, name=True, pattern=None):
        self.config_interface = config_interface
        self.description = description
        self.enabled = enabled
        self.icon_key = icon_key
        self.installed = installed
        self.name = name
        self.pattern = pattern

    def __repr__(self):
        return '<ExtensionQuery>'

    def to_dict(self):
        return {
            'configInterface': self.config_interface,
            'description': self.description,
            'enabled': self.enabled,
            'iconKey': self.icon_key,
            'installed': self.installed,
            'name': self.name,
            'pattern': self.pattern,
        }


class FilePackage:
    def __init__(self, qdict):
        self.active_task = qdict['activeTask'] \
            if 'activeTask' in qdict \
            else None
        self.bytes_loaded = qdict['bytesLoaded'] \
            if 'bytesLoaded' in qdict \
            else None
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
        self.eta = qdict['eta'] \
            if 'eta' in qdict \
            else None
        self.finished = qdict['finished'] \
            if 'finished' in qdict \
            else None
        self.hosts = qdict['hosts'] \
            if 'hosts' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None
        self.priority = Priority(qdict['priority']) \
            if 'priority' in qdict \
            else None
        self.running = qdict['running'] \
            if 'running' in qdict \
            else None
        self.save_to = qdict['saveTo'] \
            if 'saveTo' in qdict \
            else None
        self.speed = qdict['speed'] \
            if 'speed' in qdict \
            else None
        self.status = qdict['status'] \
            if 'status' in qdict \
            else None
        self.status_icon_key = qdict['statusIconKey'] \
            if 'statusIconKey' in qdict \
            else None
        self.uuid = qdict['uuid'] \
            if 'uuid' in qdict \
            else None

    def __repr__(self):
        return f'<FilePackage ({self.uuid})>'

    def to_dict(self):
        result = {
            'activeTask': self.active_task,
            'bytesLoaded': self.bytes_loaded,
            'bytesTotal': self.bytes_total,
            'childCount': self.child_count,
            'comment': self.comment,
            'downloadPassword': self.download_password,
            'enabled': self.enabled,
            'eta': self.eta,
            'finished': self.finished,
            'hosts': self.hosts,
            'name': self.name,
            'running': self.running,
            'saveTo': self.save_to,
            'speed': self.speed,
            'status': self.status,
            'statusIconKey': self.status_icon_key,
            'uuid': self.uuid,
        }

        if self.priority:
            result['priority'] = self.priority.value

        return result


class IconDescriptor:
    def __init__(self, qdict):
        self.icon_cls = qdict['cls'] \
            if 'cls' in qdict \
            else None
        self.key = qdict['key'] \
            if 'key' in qdict \
            else None
        self.prps = qdict['prps'] \
            if 'prps' in qdict \
            else None
        self.rsc = [IconDescriptor(x) for x in qdict['rsc']] \
            if 'rsc' in qdict \
            else None

    def __repr__(self):
        return f'<IconDescriptor ({self.key})>'

    def to_dict(self):
        result = {
            'cls': self.cls,
            'key': self.key,
            'prps': self.prps,
        }

        if self.rsc:
            result['rsc'] = [x.to_dict() for x in self.rsc]

        return result


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


class LinkCheckResult:
    def __init__(self, qdict):
        self.links = [LinkStatus(x) for x in qdict['links']] \
            if 'links' in qdict \
            else None
        self.status = Status(qdict['status']) \
            if 'status' in qdict \
            else None

    def __repr__(self):
        return f'<LinkCheckResult>'

    def to_dict(self):
        return {
            'links': [x.to_dict() for x in self.links],
            'status': self.status.value,
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


class LinkQuery:
    def __init__(self, added_date=True, bytes_loaded=True, bytes_total=True,
                 comment=True, enabled=True, eta=True,
                 extraction_status=True, finished=True, finished_date=True,
                 host=True, job_uuids=None, max_results=-1, package_uuids=None,
                 password=True, priority=True, running=True, skipped=True,
                 speed=True, start_at=0, status=True, url=True):
        self.added_date = added_date
        self.bytes_loaded = bytes_loaded
        self.bytes_total = bytes_total
        self.comment = comment
        self.enabled = enabled
        self.eta = eta
        self.extraction_status = extraction_status
        self.finished = finished
        self.finished_date = finished_date
        self.host = host
        self.job_uuids = job_uuids
        self.max_results = max_results
        self.package_uuids = package_uuids
        self.password = password
        self.priority = priority
        self.running = running
        self.skipped = skipped
        self.speed = speed
        self.start_at = start_at
        self.status = status
        self.url = url

    def __repr__(self):
        return '<LinkQuery>'

    def to_dict(self):
        return {
            'addedDate': self.added_date,
            'bytesLoaded': self.bytes_loaded,
            'bytesTotal': self.bytes_total,
            'comment': self.comment,
            'enabled': self.enabled,
            'eta': self.eta,
            'extractionStatus': self.extraction_status,
            'finished': self.finished,
            'finishedDate': self.finished_date,
            'host': self.host,
            'jobUUIDs': self.job_uuids,
            'maxResults': self.max_results,
            'packageUUIDs': self.package_uuids,
            'password': self.password,
            'priority': self.priority,
            'running': self.running,
            'skipped': self.skipped,
            'speed': self.speed,
            'startAt': self.start_at,
            'status': self.status,
            'url': self.url,
        }


class LinkStatus:
    def __init__(self, qdict):
        self.host = qdict['host'] \
            if 'host' in qdict \
            else None
        self.link_check_id = qdict['linkCheckID'] \
            if 'linkCheckID' in qdict \
            else None
        self.name = qdict['name'] \
            if 'name' in qdict \
            else None
        self.size = qdict['size'] \
            if 'size' in qdict \
            else None
        self.status = AvailableLinkState(qdict['status']) \
            if 'status' in qdict \
            else None
        self.url = qdict['url'] \
            if 'url' in qdict \
            else None

    def __repr__(self):
        return f'<LinkStatus ({self.link_check_id})>'

    def to_dict(self):
        result = {
            'host': self.host,
            'linkCheckID': self.link_check_id,
            'name': self.name,
            'size': self.size,
            'url': self.url,
        }

        if self.status:
            result['status'] = self.status.value

        return result


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


class PackageQuery:
    def __init__(self, bytes_loaded=True, bytes_total=True, child_count=True,
                 comment=True, enabled=True, eta=True, finished=True,
                 hosts=True, max_results=-1, package_uuids=None, priority=True,
                 running=True, save_to=True, speed=True, start_at=0,
                 status=True):
        self.bytes_loaded = bytes_loaded
        self.bytes_total = bytes_total
        self.child_count = child_count
        self.comment = comment
        self.enabled = enabled
        self.eta = eta
        self.finished = finished
        self.hosts = hosts
        self.max_results = max_results
        self.package_uuids = package_uuids
        self.priority = priority
        self.running = running
        self.save_to = save_to
        self.speed = speed
        self.start_at = start_at
        self.status = status

    def __repr__(self):
        return '<PackageQuery>'

    def to_dict(self):
        return {
            'bytesLoaded': self.bytes_loaded,
            'bytesTotal': self.bytes_total,
            'childCount': self.child_count,
            'comment': self.comment,
            'enabled': self.enabled,
            'eta': self.eta,
            'finished': self.finished,
            'hosts': self.hosts,
            'maxResults': self.max_results,
            'packageUUIDs': self.package_uuids,
            'priority': self.priority,
            'running': self.running,
            'saveTo': self.save_to,
            'speed': self.speed,
            'startAt': self.start_at,
            'status': self.status,
        }
