from .jd import make_request
from .jd_types import AddLinksQuery, CrawledLink, CrawledLinkQuery, \
    CrawledPackage, CrawledPackageQuery, JobLinkCrawler, LinkCollectingJob, \
    LinkCrawlerJobsQuery, LinkVariant

endpoint = 'linkgrabberv2'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def abort(job_id=None):
    """Abort one or all jobs.

    :param job_id: If this is given, only the job `job_id` will be aborted.
    :type job_id: int
    :return: Success
    :rtype: bool
    """

    params = None
    if job_id:
        params = [job_id]

    resp = action("/abort", params)
    return resp


def add_container(container_type, content):
    """Add a container of type and content.

    :param container_type: The type of the container
    :type container_type: str
    :param content: The content of the container
    :type content: str
    :return: A link collecting job
    :rtype: LinkCollectingJob
    """

    params = [container_type, content]
    resp = action('/addContainer', params)
    job = LinkCollectingJob(resp)
    return job


def add_links(add_links_query=AddLinksQuery()):
    """
    Add links to the linkcollector

    :param add_links_query: An AddLinksQuery object
    :type params: AddLinksQuery
    :return: A link collecting job
    :rtype: LinkCollectingJob
    """

    params = [add_links_query.to_dict()]
    resp = action("/addLinks", params)
    job = LinkCollectingJob(resp)
    return job


def add_variant_copy(link_id,
                     destination_after_link_id,
                     destination_package_id,
                     variant_id):
    """Unkown."""

    params = [link_id, destination_after_link_id, destination_package_id,
              variant_id]
    resp = action("/addVariantCopy", params)
    return resp


def cleanup(action,
            mode,
            selection_type,
            link_ids=[],
            package_ids=[]):
    """Clean packages and/or links of the linkgrabber list.

    Requires at least a ``package_ids`` or ``link_ids`` list, or both.

    :param package_ids: Package UUIDs.
    :type package_ids: List[int]
    :param link_ids: Link UUIDs.
    :type link_ids: List[int]
    :param action: Action to be done on cleanup.
    :type action: jd_types.Action
    :param mode: Mode to use.
    :type mode: jd_types.Mode
    :param selection_type: Type of selection to use.
    :type selection_type: jd_types.SelectionType
    """

    params = [link_ids, package_ids]
    params += [action.value, mode.value, selection_type.value]
    resp = action("/cleanup", params)
    return resp


def clear_list():
    """Clears Linkgrabbers list."""

    resp = action("/clearList", http_action="POST")
    return resp


def get_children_changed(structure_watermark):
    """Unkown."""

    params = [structure_watermark]
    resp = action("/getChildrenChanged", params)
    return resp


def get_download_folder_history_selection_base():
    """Returns the download folder selection.

    :return: List of strings with paths to available download folders.
    :rtype: List[str]
    """

    resp = action('/getDownloadFolderHistorySelectionBase')
    return resp


def get_download_urls(link_ids, package_ids, url_display_types=['ORIGIN']):
    """Gets download urls from Linkgrabber.

    :param package_ids: Package UUIDs.
    :type package_ids: List[int]
    :param link_ids: link UUIDs.
    :type link_ids: List[int]
    :param url_display_types: No clue. Not documented
    :type url_display_types: List
    """

    params = [link_ids, package_ids, url_display_types]
    resp = action("/getDownloadUrls", params)
    return resp


def get_package_count():
    """Get package count in linkgrabber"""

    resp = action("/getPackageCount")
    return resp


def get_variants(link_id):
    """Gets the variants of a url/download (not package)

    For example a youtube link gives you a package with three downloads,
    the audio, the video and a picture, and each of those downloads have
    different variants (audio quality, video quality, and picture quality).

    :param params: The UUID of the download you want the variants.
    :type params: List[int]
    :rtype: Variants in a list with dictionaries like this one:

        .. code-block :: json

            [
                {
                    "id": "M4A_256",
                    "name": "256kbit/s M4A-Audio"
                },
                {
                    "id": "AAC_256",
                    "name": "256kbit/s AAC-Audio"
                }
            ]

    """

    params = [link_id]
    resp = action("/getVariants", params)

    link_variants = []
    for variant in resp:
        link_variant = LinkVariant(variant)
        link_variants.append(link_variant)

    return link_variants


def is_collecting():
    """Bool status query about the collecting process"""

    resp = action("/isCollecting")
    return resp


def move_links(link_ids, after_link_id, dest_package_id):
    """Unkown."""

    params = [link_ids, after_link_id, dest_package_id]
    resp = action("/moveLinks", params)
    return resp


def move_packages(package_ids, after_dest_package_id):
    """Unkown."""

    params = [package_ids, after_dest_package_id]
    resp = action("/movePackages", params)
    return resp


def move_to_downloadlist(link_ids, package_ids):
    """Moves packages and/or links to download list.

    :param link_ids: Link UUIDs.
    :type link_ids: List[int]
    :param package_ids: Package UUIDs.
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    resp = action("/moveToDownloadlist", params)
    return resp


def move_to_new_package(link_ids, package_ids, new_pkg_name, download_path):
    """Moves packages and/or links to a new package

    :param link_ids: Link UUIDs.
    :type link_ids: List[int]
    :param package_ids: Package UUIDs.
    :type package_ids: List[int]
    :param new_pkg_name: The name of the new package
    :type new_pkg_name: str
    :param download_path: Download path for the new package
    :type download_path: str
    """

    params = [link_ids, package_ids, new_pkg_name, download_path]
    resp = action("/movetoNewPackage", params)
    return resp


def query_link_crawler_jobs(link_crawler_jobs_query=LinkCrawlerJobsQuery()):
    """Query link crawler jobs.

    :param crawled_link_query: Query to filter by
    :type crawled_link_query: jd_types.LinkCrawlerJobsQuery
    :return: List of crawled packages
    :rtype: List[jd_types.JobLinkCrawler]
    """

    params = [link_crawler_jobs_query.to_dict()]
    resp = action("/queryLinkCrawlerJobs", params)

    crawler_jobs = []
    for job in resp:
        crawler_job = JobLinkCrawler(job)
        crawler_jobs.append(crawler_job)

    return crawler_jobs


def query_links(crawled_link_query=CrawledLinkQuery()):
    """Get the links in the linkcollector/linkgrabber

    :param params: A CrawledLinkQuery object with options.
    :type params: CrawledLinkQuery
    :return: List of CrawledLink objects
    :rtype: List[CrawledLink]

    """

    params = [crawled_link_query.to_dict()]
    resp = action("/queryLinks", params)

    crawled_links = []
    for link in resp:
        crawled_link = CrawledLink(link)
        crawled_links.append(crawled_link)

    return crawled_links


def query_packages(crawled_package_query=CrawledPackageQuery()):
    """Get the crawled packages in the linkgrabber

    :param params: A dictionary of parameters to pass.
    :type params: jd_types.CrawledPackageQuery
    :return: A list of crawled packages:
    """

    params = [crawled_package_query.to_dict()]
    resp = action('/queryPackages', params)

    crawled_packages = []
    for package in resp:
        crawled_package = CrawledPackage(package)
        crawled_packages.append(crawled_package)

    return crawled_packages


def remove_links(link_ids, package_ids):
    """Unknown."""

    params = [link_ids, package_ids]
    resp = action("/removeLinks", params)
    return resp


def rename_link(link_id, new_name):
    """Unknown."""

    params = [link_id, new_name]
    resp = action("/renameLink", params)
    return resp


def rename_package(package_id, new_name):
    """Unknown."""

    params = [package_id, new_name]
    resp = action("/renamePackage", params)
    return resp


def set_download_directory(directory, package_ids):
    """Unknown."""

    params = [directory, package_ids]
    resp = action("/setDownloadDirectory", params)
    return resp


def set_download_password(link_ids, package_ids, password):
    """Unknown."""

    params = [link_ids, package_ids, password]
    resp = action("/setDownloadPassword", params)
    return resp


def set_enabled(enabled, link_ids, package_ids):
    """Sets the UUIDs as enabled

    :param enabled: Enable or disable the IDs
    :type enabled: bool
    :param link_ids: List of link UUIDs
    :type link_ids: List[int]
    :param package_ids: List of package UUIDs
    :type package_ids: List[int]
    """

    params = [enabled, link_ids, package_ids]
    resp = action("/setEnabled", params=params)
    return resp


def set_priority(priority, link_ids, package_ids):
    """Sets the priority of links or packages.

    :param package_ids: Package UUIDs.
    :type package_ids: List[int]
    :param link_ids: link UUIDs.
    :type link_ids: List[int]
    :param priority: Priority to set.
        Priorities: HIGHEST, HIGHER, HIGH, DEFAULT, LOWER
    :type priority: str
    """

    params = [priority, link_ids, package_ids]
    resp = action("/setPriority", params)
    return resp


def set_variant(link_id, variant_id):
    """Unknown."""

    params = [link_id, variant_id]
    resp = action("/setVariant", params)
    return resp


def split_package_by_hoster(link_ids, pkg_ids):
    """Unknown."""

    params = [link_ids, pkg_ids]
    resp = action("/splitPackageByHoster", params)
    return resp


def start_online_check(link_ids, package_ids):
    """Unknown."""

    params = [link_ids, package_ids]
    resp = action("/startOnlineStatusCheck", params)
    return resp


def help():
    """Returns the API help."""

    resp = action("/linkgrabberv2/help", http_action="GET")
    return resp
