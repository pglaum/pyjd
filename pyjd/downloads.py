from .jd import make_request
from .jd_types import DeleteAction, DownloadLink, FilePackage, LinkQuery, Mode, \
        PackageQuery, Priority, Reason, SelectionType
from typing import Any, Dict, List, Optional

endpoint = 'downloadsV2'


def action(route: str, params: Any = None) -> Any:
    route = f'{endpoint}{route}'
    return make_request(route, params)


# TODO: test functionality
def cleanup(link_ids: List[int], package_ids: List[int],
        delete_action: DeleteAction, mode: Mode,
        selection_type: SelectionType) -> Any:
    """Cleanup the link_ids & package_ids in the download list.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    :param action: The class:`jd_types.DeleteAction` that will be performed
    :type action: DeleteAction
    :param mode: The class:`jd_types.Mode` that is used
    :type mode: Mode
    :type selection_type: The class:`jd_types.SelectionType` that is applied
    :type selection_type: SelectionType
    :returns: resp
    :rtype: Any
    """

    params = [link_ids, package_ids, delete_action.value, mode.value,
              selection_type.value]
    resp = action("/cleanup", params)
    return resp


def force_download(link_ids: List[int], package_ids: List[int]) -> bool:
    """Force downloads for link_ids and package_ids.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    :returns: Success
    :rtype: bool
    """

    params = [link_ids, package_ids]
    resp = action("/forceDownload", params)
    return resp


def get_download_urls(link_ids: List[int], package_ids: List[int],
        url_display_type: List[str]) -> Dict[str, List[int]]:
    """Force downloads for link_ids and package_ids.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    :param url_display_type: The type of urls that should be returned.
        Example: ['ORIGIN']
    :type url_display_type: List[str]
    :returns: The download urls with their associated packages
    :rtype: Dict[str, List[int]]
    """

    params = [link_ids, package_ids, url_display_type]
    resp = action("/getDownloadUrls", params)
    return resp


def get_stop_mark() -> int:
    """Get the link id for where the stop mark is at.

    If no stop mark is set, the result it -1

    :returns: Link id for stop mark, or -1
    :rtype: int
    """

    resp = action("/getStopMark")
    return resp


def get_stop_marked_link() -> Optional[DownloadLink]:
    """Get the :class:`DownloadLink` object for the stopmark.

    :returns: Download link for stop mark, or None
    :rtype: DownloadLink
    """

    resp = action("/getStopMarkedLink")

    if resp:
        download_link = DownloadLink(resp)
        return download_link

    return None


def get_structure_change_counter(old_counter_value: int) -> int:
    """Get the structure change counter.

    Update the application layout, if the structure_change_counter is higher
    than the last.

    :returns: Structure change counter, or -1 if there is no newer change.
    :rtype: int
    """

    params = [old_counter_value]
    resp = action("/getStructureChangeCounter", params)
    return resp


# TODO: test functionality
def move_links(link_ids: List[int], after_link_id: int,
        dest_package_id: int) -> Any:
    """Move links to a package.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param after_link_id: ?
    :type after_link_id: int
    :param dest_package_id: The ID of the destination package
    :type dest_package_id: int
    :returns: resp
    :rtype: Any
    """

    params = [link_ids, after_link_id, dest_package_id]
    resp = action("/moveLinks", params)
    return resp


# TODO: test functionality
def move_packages(package_ids, after_dest_package_id):
    """Move packages.

    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    :param after_dest_package_id: ?
    :type after_dest_package_id: int
    :returns: resp
    :rtype: Any
    """

    params = [package_ids, after_dest_package_id]
    resp = action("/movePackages", params)
    return resp


# TODO: test functionality
def move_to_new_package(link_ids: List[int], pkg_ids: List[int],
        new_pkg_name: str, download_path: str) -> Any:
    """Move link_ids and pkg_ids to a new package

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    :param new_pkg_name: Name of the new package
    :type new_pkg_name: str
    :param download_path: Download path for the new package
    :type download_path: str
    :returns: resp
    :rtype: Any
    """

    params = [link_ids, pkg_ids, new_pkg_name, download_path]
    resp = action("/movetoNewPackage", params)
    return resp


def package_count() -> int:
    """Get the number of packages in the download list.

    :returns: Number of packages in download list
    :rtype: int
    """

    resp = action("/packageCount")
    return resp


def query_links(query_params: LinkQuery = LinkQuery()) -> List[DownloadLink]:
    """Query the links in the download list.

    :param query_params: The parameters for the query
    :type query_params: LinkQuery
    :returns: A list of download link objects
    :rtype: List[DownloadLink]
    """

    params = [query_params.to_dict()]
    resp = action("/queryLinks", params)

    download_links = []
    for link in resp:
        download_link = DownloadLink(link)
        download_links.append(download_link)

    return download_links


def query_packages(query_params: PackageQuery = PackageQuery()
        ) -> List[FilePackage]:
    """Query the packages in the download list.

    :param query_params: The parameters for the query
    :type query_params: PackageQuery
    :returns: A list of file packages objects
    :rtype: List[FilePackage]
    """

    params = [query_params.to_dict()]
    resp = action("/queryPackages", params)

    download_packages = []
    for package in resp:
        download_package = FilePackage(package)
        download_packages.append(download_package)

    return download_packages


def remove_links(link_ids: List[int], package_ids: List[int]) -> None:
    """Remove links/packages from download list.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    action("/removeLinks", params)


def remove_stop_mark() -> None:
    """Remove the stop mark."""

    action("/removeStopMark")


def rename_link(link: int, new_name: str) -> None:
    """Rename a link.

    :param link: The ID of the link
    :type link: int
    :param new_name: The new name for the link
    :type new_name: str
    """

    params = [link, new_name]
    action("/renameLink", params)


def rename_package(package_id: str, new_name: str) -> None:
    """Rename a package.

    :param package_id: ID of the packages
    :type package_id: int
    :param new_name: New name for the package
    :type new_name: str
    """

    params = [package_id, new_name]
    resp = action("/renamePackage", params)
    return resp


def reset_links(link_ids: List[int], package_ids: List[int]) -> None:
    """Reset links/packages in the download list.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    action("/resetLinks", params)


def resume_links(link_ids: List[int], package_ids: List[int]) -> None:
    """Resume links/packages.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: Package IDs that are used
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    action("/resumeLinks", params)


def set_download_directory(directory: str, package_ids: List[int]) -> None:
    """Set the download directory for a packages.

    :param directory: Path of the download directory
    :type directory: str
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    """

    params = [directory, package_ids]
    resp = action("/setDownloadDirectory", params)
    return resp


def set_download_password(link_ids: List[int], package_ids: List[int],
        password: str) -> bool:
    """Set the download password for links/packages.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    :param password: The download password
    :type password: str
    :returns: Success
    :rtype: bool
    """

    params = [link_ids, package_ids, password]
    resp = action("/setDownloadPassword", params)
    return resp


def set_enabled(enabled: bool, link_ids: List[int], package_ids: List[int]
        ) -> bool:
    """Enable/disable links and packages.

    :param enabled: Enable on or off
    :type enabled: bool
    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    """

    params = [enabled, link_ids, package_ids]
    resp = action("/setEnabled", params)
    return resp


def set_priority(priority: Priority, link_ids: List[int],
        package_ids: List[int]) -> None:
    """Set the priority for links and packages.

    :param priority: The priority for the links/packages.
    :type priority: Priority
    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    """

    params = [priority.value, link_ids, package_ids]
    action("/setPriority", params)


def set_stop_mark(link_id: int = None, package_id: int = None) -> None:
    """Set the stop mark to the specified id.

    Only one of link_id and package_id has to be given.

    :param link_id: A link id for the stop mark
    :type link_id: int
    :param package_id: A package id for the stop mark
    :type package_id: int
    """

    params = [link_id, package_id]
    action("/setStopMark", params)


def split_package_by_hoster(link_ids: List[int],
        package_ids: List[int]) -> None:
    """Split the packages/links by hoster.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    action("/splitPackageByHoster", params)


def start_online_status_check(link_ids: List[int],
        package_ids: List[int]) -> None:
    """Start an online status check for links and packages.

    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    """

    params = [link_ids, package_ids]
    action("/startOnlineStatusCheck", params)


def unskip(link_ids: List[int], package_ids: List[int],
        filter_by_reason: Reason) -> bool:
    """Un-skip links and packages

    :param package_ids: List of package IDs that are changed.
    :type package_ids: List[int]
    :param link_ids: Link IDs that are used
    :type link_ids: List[int]
    :param filter_by_reason: Filter for the reason why they were skipped.
    :type filter_by_reason: Reason
    :returns: Success
    :rtype: bool
    """

    # package_ids and link_ids are switch for whatever reason...
    params = [package_ids, link_ids, filter_by_reason.value]
    resp = action("/unskip", params)
    return resp
