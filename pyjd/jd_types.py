"""
These are the types and constants that are defined in JDownloader.

For more information, see here:
    https://my.jdownloader.org/developers/index.html#tag_342
"""

from __future__ import annotations

from enum import Enum
from pydantic import BaseModel, Field
from typing import Any, List, Optional


#
# enums and constants
#


class AbstractType(str, Enum):
    """Abstract types that are used for config entries."""

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


class DeleteAction(str, Enum):
    """Delete actions, that can be executed.

    This corresponds to the "Action" enum of JDownloader.
    """

    DELETE_ALL = "DELETE_ALL"
    DELETE_DISABLED = "DELETE_DISABLED"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_FINISHED = "DELETE_FINISHED"
    DELETE_DUPE = "DELETE_DUPE"
    DELETE_MODE = "DELETE_MODE"


class AvailableLinkState(str, Enum):
    """The availability of a link."""

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    UNKNOWN = "UNKNOWN"
    TEMP_UNKNOWN = "TEMP_UNKNOWN"


class BasicAuthType(str, Enum):
    """Types of basic auth protocols."""

    FTP = "FTP"
    HTTP = "HTTP"


class Context(str, Enum):
    """Contextmenu selection."""

    LGC = "LGC"  # linkgrabber rightclick
    DLC = "DLC"  # downloadlist rightclick


class MenuType(str, Enum):
    """Menu types"""

    CONTAINER = "CONTAINER"
    ACTION = "ACTION"
    LINK = "LINK"


class Mode(str, Enum):
    """Modes for package deletion."""

    REMOVE_LINKS_AND_DELETE_FILES = "REMOVE_LINKS_AND_DELETE_FILES"
    REMOVE_LINKS_AND_RECYCLE_FILES = "REMOVE_LINKS_AND_RECYCLE_FILES"
    REMOVE_LINKS_ONLY = "REMOVE_LINKS_ONLY"


class Priority(str, Enum):
    """Download priority for packages."""

    HIGHEST = "HIGHEST"
    HIGHER = "HIGHER"
    HIGH = "HIGH"
    DEFAULT = "DEFAULT"
    LOW = "LOW"
    LOWER = "LOWER"
    LOWEST = "LOWEST"


class Reason(str, Enum):
    """Reasons for exceptions."""

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


class SelectionType(str, Enum):
    """Types for selection"""

    SELECTED = "SELECTED"
    UNSELECTED = "UNSELECTED"
    ALL = "ALL"
    NONE = "NONE"


class SkipRequest(str, Enum):
    """Captcha skip request"""

    SINGLE = "SINGLE"
    BLOCK_HOSTER = "BLOCK_HOSTER"
    BLOCK_ALL_CAPTCHAS = "BLOCK_ALL_CAPTCHAS"
    BLOCK_PACKAGE = "BLOCK_PACKAGE"
    REFRESH = "REFRESH"
    STOP_CURRENT_ACTION = "STOP_CURRENT_ACTION"
    TIMEOUT = "TIMEOUT"


class Status(str, Enum):
    """Status"""

    NA = "NA"
    PENDING = "PENDING"
    FINISHED = "FINISHED"


#
# structures and objects
#


class Account(BaseModel):
    """This is a premium hoster account

    Initializes itself from a query result (dict)
    """

    enabled: Optional[bool]
    errorString: Optional[str]
    errorType: Optional[str]
    hostname: Optional[str]
    trafficLeft: Optional[int]
    trafficMax: Optional[int]
    username: Optional[str]
    uuid: Optional[int]
    valid: Optional[bool]
    validUntil: Optional[int]

    def __repr__(self) -> str:
        return f"<Account ({self.uuid})>"


class AccountQuery(BaseModel):
    """Query for premium host accounts.

    The fields are booleans, that can be turned on or off, if you want to have
    query for the information or not.
    By default all possible data is queried.
    """

    enabled: bool = True
    error: bool = True
    maxResults: int = -1
    startAt: int = 0
    trafficLeft: bool = True
    trafficMax: bool = True
    userName: bool = True
    uuidlist: Optional[List[int]]
    valid: bool = True
    validUntil: bool = True

    def __repr__(self):
        return f"<AccountQuery ({self.uuidlist})>"

    @staticmethod
    def default():
        return AccountQuery(
            enabled=True,
            error=True,
            maxResults=-1,
            startAt=0,
            trafficLeft=True,
            trafficMax=True,
            userName=True,
            uuidlist=None,
            valid=True,
            validUntil=True,
        )


class AdvancedConfigAPIEntry(BaseModel):

    abstractType: Optional[AbstractType]
    defaultValue: Optional[Any]
    docs: Optional[str]
    enumLabel: Optional[str]
    enumOptions: Optional[Any]
    interfaceName: Optional[str]
    key: Optional[str]
    storage: Optional[str]
    type: Optional[str]
    value: Optional[Any]

    def __repr__(self):
        return f"<AdvancedConfigAPIEntry ({self.key})>"


class AdvancedConfigQuery(BaseModel):

    configInterface: Optional[str]
    defaultValues: bool
    description: bool
    enumInfo: bool
    includeExtensions: bool
    pattern: Optional[str]
    values: bool

    def __repr__(self):
        return f"<AdvancedConfigQuery ({self.configInterface})>"

    @staticmethod
    def default():
        return AdvancedConfigQuery(
            configInterface=None,
            defaultValues=True,
            description=True,
            enumInfo=True,
            includeExtensions=True,
            pattern=None,
            values=True,
        )


class BasicAuth(BaseModel):

    created: Optional[int]
    enabled: Optional[bool]
    hostmask: Optional[str]
    id: Optional[int]
    lastValidated: Optional[int]
    password: Optional[str]
    type: Optional[BasicAuthType]
    username: Optional[str]

    def __repr__(self):
        return f"<BasicAuth ({self.id})>"


class AddLinksQuery(BaseModel):

    assignJobID: Optional[bool]
    autoExtract: Optional[bool]
    autostart: Optional[bool]
    dataURLs: List[str] = []
    deepDecrypt: Optional[bool]
    destinationFolder: Optional[str]
    downloadPassword: Optional[str]
    extractPassword: Optional[str]
    links: Optional[str]
    overwritePackagizerRules: Optional[bool]
    packageName: Optional[str]
    priority: Optional[Priority] = Priority.DEFAULT
    sourceUrl: Optional[str]

    def __repr__(self):
        return f"<AddLinksQuery ({self.packageName})>"


class APIQuery(BaseModel):
    """A standard api query.

    Most endpoint use a specialized version.
    """

    empty: bool
    forNullKey: Optional[str]
    maxResults: int
    startAt: int

    def __repr__(self):
        return "<APIQuery>"

    @staticmethod
    def default():
        return APIQuery(empty=False, forNullKey="", maxResults=-1, startAt=0)


class CaptchaJob(BaseModel):

    captchaCategory: Optional[str]
    created: Optional[int]
    explain: Optional[str]
    hoster: Optional[str]
    id: Optional[int]
    link: Optional[int]
    timeout: Optional[int]
    type: Optional[str]

    def __repr__(self):
        return f"<CaptchaJob ({self.id})>"


class LinkVariant(BaseModel):

    iconKey: Optional[str]
    id: Optional[str]
    name: Optional[str]

    def __repr__(self):
        return f"<LinkVariant ({self.id})>"


class CrawledLink(BaseModel):

    availability: Optional[AvailableLinkState]
    bytesTotal: Optional[int]
    comment: Optional[str]
    downloadPassword: Optional[str]
    enabled: Optional[bool]
    host: Optional[str]
    name: Optional[str]
    packageUUID: Optional[int]
    priority: Optional[Priority]
    url: Optional[str]
    uuid: Optional[int]
    variant: Optional[LinkVariant]
    variants: Optional[bool]

    def __repr__(self):
        return f"<CrawledLink ({self.uuid})>"


class CrawledLinkQuery(BaseModel):

    availability: Optional[bool]
    bytesTotal: Optional[bool]
    comment: Optional[bool]
    enabled: Optional[bool]
    host: Optional[bool]
    jobUUIDs: Optional[List[int]]
    maxResults: Optional[int]
    packageUUIDs: Optional[List[int]]
    password: Optional[bool]
    priority: Optional[bool]
    startAt: Optional[int]
    status: Optional[bool]
    url: Optional[bool]
    variantID: Optional[bool]
    variantIcon: Optional[bool]
    variantName: Optional[bool]
    variants: Optional[bool]

    def __repr__(self):
        return "<CrawledLinkQuery>"

    @staticmethod
    def default():
        return CrawledLinkQuery(
            availability=True,
            bytesTotal=True,
            comment=True,
            enabled=True,
            host=True,
            jobUUIDs=None,
            maxResults=-1,
            packageUUIDs=None,
            password=True,
            priority=True,
            startAt=0,
            status=True,
            url=True,
            variantID=True,
            variantIcon=True,
            variantName=True,
            variants=True,
        )


class CrawledPackage(BaseModel):

    bytesTotal: Optional[int]
    childCount: Optional[int]
    comment: Optional[str]
    downloadPassword: Optional[str]
    enabled: Optional[bool]
    hosts: Optional[List[str]]
    name: Optional[str]
    offlineCount: Optional[int]
    onlineCount: Optional[int]
    priority: Optional[Priority]
    saveTo: Optional[str]
    tempUnknownCount: Optional[int]
    unknownCount: Optional[int]
    uuid: Optional[int]

    def __repr__(self):
        return f"<CrawledPackage ({self.uuid})"


class CrawledPackageQuery(BaseModel):

    availableOfflineCount: Optional[bool]
    availableOnlineCount: Optional[bool]
    availableTempUnknownCount: Optional[bool]
    availableUnknownCount: Optional[bool]
    bytesTotal: Optional[bool]
    childCount: Optional[bool]
    comment: Optional[bool]
    enabled: Optional[bool]
    hosts: Optional[bool]
    maxResults: Optional[int]
    packageUUIDs: Optional[List[int]]
    priority: Optional[bool]
    saveTo: Optional[bool]
    startAt: Optional[int]
    status: Optional[bool]

    def __repr__(self):
        return "<CrawledPackageQuery>"

    @staticmethod
    def default():
        return CrawledPackageQuery(
            availableOfflineCount=True,
            availableOnlineCount=True,
            availableTempUnknownCount=True,
            availableUnknownCount=True,
            bytesTotal=True,
            childCount=True,
            comment=True,
            enabled=True,
            hosts=True,
            maxResults=-1,
            packageUUIDs=None,
            priority=True,
            saveTo=True,
            startAt=0,
            status=True,
        )


class DialogInfo(BaseModel):
    properties: Optional[dict[str, str]]
    type: Optional[str]

    def __repr__(self):
        return f"<DialogInfo ({self.type})>"


class DialogTypeInfo(BaseModel):
    in_: Optional[dict[str, str]] = Field(..., alias="in")
    out: Optional[dict[str, str]]

    def __repr__(self):
        return "<DialogTypeInfo>"


class DownloadLink(BaseModel):

    addedDate: Optional[int]
    bytesLoaded: Optional[int]
    bytesTotal: Optional[int]
    comment: Optional[str]
    downloadPassword: Optional[str]
    enabled: Optional[bool]
    eta: Optional[int]
    extractionStatus: Optional[str]
    finished: Optional[bool]
    finishedDate: Optional[int]
    host: Optional[str]
    name: Optional[str]
    packageUUID: Optional[int]
    priority: Optional[Priority]
    running: Optional[int]
    skipped: Optional[int]
    speed: Optional[int]
    status: Optional[str]
    statusIconKey: Optional[str]
    url: Optional[str]
    uuid: Optional[int]

    def __repr__(self):
        return f"<DownloadLink ({self.uuid})>"


class EnumOption(BaseModel):

    label: Optional[str]
    name: Optional[str]

    def __repr__(self):
        return f"<EnumOption ({self.name})>"


class Extension(BaseModel):

    configInterface: Optional[str]
    description: Optional[str]
    enabled: Optional[bool]
    iconKey: Optional[str]
    id: Optional[str]
    installed: Optional[bool]
    name: Optional[str]

    def __repr__(self):
        return f"<Extension ({self.id})>"


class ExtensionQuery(BaseModel):

    configInterface: Optional[bool]
    description: Optional[bool]
    enabled: Optional[bool]
    iconKey: Optional[bool]
    installed: Optional[bool]
    name: Optional[bool]
    pattern: Optional[str]

    def __repr__(self):
        return "<ExtensionQuery>"

    @staticmethod
    def default():
        return ExtensionQuery(
            configInterface=True,
            description=True,
            enabled=True,
            iconKey=True,
            installed=True,
            name=True,
            pattern=None,
        )


class FilePackage(BaseModel):

    activeTask: Optional[str]
    bytesLoaded: Optional[int]
    bytesTotal: Optional[int]
    childCount: Optional[int]
    comment: Optional[str]
    downloadPassword: Optional[str]
    enabled: Optional[bool]
    eta: Optional[int]
    finished: Optional[bool]
    hosts: Optional[List[str]]
    name: Optional[str]
    priority: Optional[Priority]
    running: Optional[bool]
    saveTo: Optional[str]
    speed: Optional[int]
    status: Optional[str]
    statusIconKey: Optional[str]
    uuid: Optional[int]

    def __repr__(self):
        return f"<FilePackage ({self.uuid})>"


class IconDescriptor(BaseModel):

    cls: Optional[str]
    key: Optional[str]
    prps: Optional[Any]
    rsc: Optional[List[IconDescriptor]]

    def __repr__(self):
        return f"<IconDescriptor ({self.key})>"


class JobLinkCrawler(BaseModel):

    broken: Optional[int]
    checking: Optional[bool]
    crawled: Optional[int]
    crawledId: Optional[int]
    crawling: Optional[bool]
    filtered: Optional[int]
    jobId: Optional[int]
    unhandled: Optional[int]

    def __repr__(self):
        return f"<JobLinkCrawler ({self.crawledId})>"


class LinkStatus(BaseModel):

    host: Optional[str]
    linkCheckID: Optional[str]
    name: Optional[str]
    size: Optional[int]
    status: Optional[AvailableLinkState]
    url: Optional[str]

    def __repr__(self):
        return f"<LinkStatus ({self.linkCheckID})>"


class LinkCheckResult(BaseModel):

    link: Optional[List[LinkStatus]]
    status: Optional[Status]

    def __repr__(self):
        return "<LinkCheckResult>"


class LinkCollectingJob(BaseModel):

    id: Optional[int]

    def __repr__(self):
        return f"<LinkCollectingJob ({self.id})>"


class LinkCrawlerJobsQuery(BaseModel):

    collectorInfo: Optional[bool]
    jobIds: Optional[List[int]]

    def __repr__(self):
        return "<LinkCrawlerJobsQuery>"

    @staticmethod
    def default():
        return LinkCrawlerJobsQuery(collectorInfo=True, jobIds=None)


class LinkQuery(BaseModel):

    addedDate: Optional[bool]
    bytesLoaded: Optional[bool]
    bytesTotal: Optional[bool]
    comment: Optional[bool]
    enabled: Optional[bool]
    eta: Optional[bool]
    extractionStatus: Optional[bool]
    finished: Optional[bool]
    finishedDate: Optional[bool]
    host: Optional[bool]
    jobUUIDs: Optional[List[int]]
    maxResults: Optional[int]
    packageUUIDs: Optional[List[int]]
    password: Optional[bool]
    priority: Optional[bool]
    running: Optional[bool]
    skipped: Optional[bool]
    speed: Optional[bool]
    startAt: Optional[int]
    status: Optional[bool]
    url: Optional[bool]

    def __repr__(self):
        return "<LinkQuery>"

    @staticmethod
    def default():
        return LinkQuery(
            addedDate=True,
            bytesLoaded=True,
            bytesTotal=True,
            comment=True,
            enabled=True,
            eta=True,
            extractionStatus=True,
            finished=True,
            finishedDate=True,
            host=True,
            jobUUIDs=None,
            maxResults=-1,
            packageUUIDs=None,
            password=True,
            priority=True,
            running=True,
            skipped=True,
            speed=True,
            startAt=0,
            status=True,
            url=True,
        )


class LogFolder(BaseModel):

    created: Optional[int]
    current: Optional[bool]
    lastModified: Optional[int]

    def __repr__(self):
        return "<LogFolder>"


class MenuStructure(BaseModel):

    children: Optional[List[MenuStructure]]
    icon: Optional[str]
    id: Optional[str]
    name: Optional[str]
    type: Optional[MenuType]

    def __repr__(self):
        return f"<MenuStructure ({self.id})>"


class PackageQuery(BaseModel):

    bytesLoaded: Optional[bool]
    bytesTotal: Optional[bool]
    childCount: Optional[bool]
    comment: Optional[bool]
    enabled: Optional[bool]
    eta: Optional[bool]
    finished: Optional[bool]
    hosts: Optional[bool]
    maxResults: Optional[int]
    packageUUIDs: Optional[List[int]]
    priority: Optional[bool]
    running: Optional[bool]
    saveTo: Optional[bool]
    speed: Optional[bool]
    startAt: Optional[int]
    status: Optional[bool]

    def __repr__(self):
        return "<PackageQuery>"

    @staticmethod
    def default():
        return PackageQuery(
            bytesLoaded=True,
            bytesTotal=True,
            childCount=True,
            comment=True,
            enabled=True,
            eta=True,
            finished=True,
            hosts=True,
            maxResults=-1,
            packageUUIDs=None,
            priority=True,
            running=True,
            saveTo=True,
            speed=True,
            startAt=0,
            status=True,
        )


class Plugin(BaseModel):

    abstractType: Optional[AbstractType]
    className: Optional[str]
    defaultValue: Optional[Any]
    displayName: Optional[str]
    docs: Optional[str]
    enumLabel: Optional[str]
    enumOptions: Optional[Any]
    interfaceName: Optional[str]
    key: Optional[str]
    pattern: Optional[str]
    storage: Optional[str]
    type: Optional[str]
    value: Optional[Any]
    version: Optional[str]

    def __repr__(self):
        return f"<Plugin ({self.className})>"


class PluginsQuery(BaseModel):

    pattern: Optional[str]
    version: Optional[str]

    def __repr__(self):
        return f"<PluginsQuery ({self.pattern})>"

    @staticmethod
    def default():
        return PluginsQuery(pattern="", version=None)


class PublisherResponse(BaseModel):

    eventids: Optional[List[str]]
    publisher: Optional[str]

    def __repr__(self):
        return f"<PublisherResponse ({self.publisher})>"


class SubscriptionResponse(BaseModel):

    exclusions: Optional[List[str]]
    maxKeepalive: Optional[int]
    maxPolltimeout: Optional[int]
    subscribed: Optional[bool]
    subscriptionid: Optional[int]
    subscriptions: Optional[List[str]]

    def __repr__(self):
        return f"<SubscriptionResponse ({self.subscriptionid})>"


class IPandPort(BaseModel):

    port: int
    ip: str


class DirectConnectionInfos(BaseModel):

    infos: Optional[List[IPandPort]]
    rebindProtectionDetected: Optional[bool]
    mode: Optional[str]
