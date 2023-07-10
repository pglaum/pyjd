from .jd_types import (
    DeleteAction,
    DownloadLink,
    FilePackage,
    LinkQuery,
    Mode,
    PackageQuery,
    Priority,
    Reason,
    SelectionType,
)
from typing import Any, Dict, List, Optional


class Downloads:
    def __init__(self, device):
        self.device = device
        self.endpoint = "downloadsV2"

    def action(self, route: str, params: Optional[Any] = None) -> Any:
        route = f"/{self.endpoint}{route}"
        return self.device.connection_helper.action(route, params)

    def cleanup(
        self,
        link_ids: List[int] = [],
        package_ids: List[int] = [],
        delete_action: DeleteAction = DeleteAction.DELETE_DISABLED,
        mode: Mode = Mode.REMOVE_LINKS_ONLY,
        selection_type: SelectionType = SelectionType.ALL,
    ) -> bool:
        """Cleanup the link_ids & package_ids in the download list.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        :param action: The class:`jd_types.DeleteAction` that will be performed
        :type action: DeleteAction
        :param mode: The class:`jd_types.Mode` that is used
        :type mode: Mode
        :type selection_type: The class:`jd_types.SelectionType` that is
            applied
        :type selection_type: SelectionType
        :returns: resp
        :rtype: Any
        """

        params = [
            link_ids,
            package_ids,
            delete_action.value,
            mode.value,
            selection_type.value,
        ]
        resp = self.action("/cleanup", params)
        if resp == "":
            return True
        return False

    def force_download(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> bool:
        """Force downloads for link_ids and package_ids.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        :returns: Success
        :rtype: bool
        """

        params = [link_ids, package_ids]
        resp = self.action("/forceDownload", params)
        return resp

    def get_download_urls(
        self,
        link_ids: List[int] = [],
        package_ids: List[int] = [],
        url_display_type: List[str] = ["ORIGIN"],
    ) -> Dict[str, List[int]]:
        """Get the download urls for link_ids and package_ids.

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
        resp = self.action("/getDownloadUrls", params)
        return resp

    def get_stop_mark(self) -> int:
        """Get the link id for where the stop mark is at.

        If no stop mark is set, the result it -1

        :returns: Link id for stop mark, or -1
        :rtype: int
        """

        resp = self.action("/getStopMark")
        return resp

    def get_stop_marked_link(self) -> Optional[DownloadLink]:
        """Get the :class:`DownloadLink` object for the stopmark.

        :returns: Download link for stop mark, or None
        :rtype: DownloadLink
        """

        resp = self.action("/getStopMarkedLink")

        if resp:
            download_link = DownloadLink(**resp)
            return download_link

        return None

    def get_structure_change_counter(self, old_counter_value: int = 0) -> int:
        """Get the structure change counter.

        Update the application layout, if the structure_change_counter is
        higher than the last.

        :returns: Structure change counter, or -1 if there is no newer change.
        :rtype: int
        """

        params = [old_counter_value]
        resp = self.action("/getStructureChangeCounter", params)
        return resp

    def move_links(
        self,
        link_ids: List[int] = [],
        after_link_id: int = -1,
        dest_package_id: int = -1,
    ) -> Any:
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
        resp = self.action("/moveLinks", params)
        return resp

    def move_packages(
        self, package_ids: List[int] = [], after_dest_package_id: int = -1
    ) -> Any:
        """Move packages.

        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        :param after_dest_package_id: ?
        :type after_dest_package_id: int
        :returns: resp
        :rtype: Any
        """

        params = [package_ids, after_dest_package_id]
        resp = self.action("/movePackages", params)
        return resp

    def move_to_new_package(
        self,
        link_ids: List[int] = [],
        pkg_ids: List[int] = [],
        new_pkg_name: str = "",
        download_path: str = "",
    ) -> Any:
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
        resp = self.action("/movetoNewPackage", params)
        return resp

    def package_count(self) -> int:
        """Get the number of packages in the download list.

        :returns: Number of packages in download list
        :rtype: int
        """

        resp = self.action("/packageCount")
        return resp

    def query_links(
        self, query_params: LinkQuery = LinkQuery.default()
    ) -> List[DownloadLink]:
        """Query the links in the download list.

        :param query_params: The parameters for the query
        :type query_params: LinkQuery
        :returns: A list of download link objects
        :rtype: List[DownloadLink]
        """

        params = [query_params.dict()]
        resp = self.action("/queryLinks", params)

        download_links = []
        for link in resp:
            download_link = DownloadLink(**link)
            download_links.append(download_link)

        return download_links

    def query_packages(
        self, query_params: PackageQuery = PackageQuery.default()
    ) -> List[FilePackage]:
        """Query the packages in the download list.

        :param query_params: The parameters for the query
        :type query_params: PackageQuery
        :returns: A list of file packages objects
        :rtype: List[FilePackage]
        """

        params = [query_params.dict()]
        resp = self.action("/queryPackages", params)

        download_packages = []
        for package in resp:
            download_package = FilePackage(**package)
            download_packages.append(download_package)

        return download_packages

    def remove_links(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> None:
        """Remove links/packages from download list.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        """

        params = [link_ids, package_ids]
        self.action("/removeLinks", params)

    def remove_stop_mark(self) -> None:
        """Remove the stop mark."""

        self.action("/removeStopMark")

    def rename_link(self, link: int = -1, new_name: str = "") -> None:
        """Rename a link.

        :param link: The ID of the link
        :type link: int
        :param new_name: The new name for the link
        :type new_name: str
        """

        params = [link, new_name]
        self.action("/renameLink", params)

    def rename_package(self, package_id: str = "", new_name: str = "") -> None:
        """Rename a package.

        :param package_id: ID of the packages
        :type package_id: int
        :param new_name: New name for the package
        :type new_name: str
        """

        params = [package_id, new_name]
        resp = self.action("/renamePackage", params)
        return resp

    def reset_links(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> None:
        """Reset links/packages in the download list.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        """

        params = [link_ids, package_ids]
        self.action("/resetLinks", params)

    def resume_links(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> None:
        """Resume links/packages.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: Package IDs that are used
        :type package_ids: List[int]
        """

        params = [link_ids, package_ids]
        self.action("/resumeLinks", params)

    def set_download_directory(
        self, directory: str = "", package_ids: List[int] = []
    ) -> None:
        """Set the download directory for a packages.

        :param directory: Path of the download directory
        :type directory: str
        :param package_ids: List of package IDs that are changed.
        :type package_ids: List[int]
        """

        params = [directory, package_ids]
        resp = self.action("/setDownloadDirectory", params)
        return resp

    def set_download_password(
        self, link_ids: List[int] = [], package_ids: List[int] = [], password: str = ""
    ) -> bool:
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
        resp = self.action("/setDownloadPassword", params)
        return resp

    def set_enabled(
        self,
        enabled: bool = True,
        link_ids: List[int] = [],
        package_ids: List[int] = [],
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
        resp = self.action("/setEnabled", params)
        return resp

    def set_priority(
        self,
        priority: Priority = Priority.DEFAULT,
        link_ids: List[int] = [],
        package_ids: List[int] = [],
    ) -> None:
        """Set the priority for links and packages.

        :param priority: The priority for the links/packages.
        :type priority: Priority
        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: List of package IDs that are changed.
        :type package_ids: List[int]
        """

        params = [priority.value, link_ids, package_ids]
        self.action("/setPriority", params)

    def set_stop_mark(
        self, link_id: Optional[int] = None, package_id: Optional[int] = None
    ) -> None:
        """Set the stop mark to the specified id.

        Only one of link_id and package_id has to be given.

        :param link_id: A link id for the stop mark
        :type link_id: int
        :param package_id: A package id for the stop mark
        :type package_id: int
        """

        params = [link_id, package_id]
        self.action("/setStopMark", params)

    def split_package_by_hoster(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> None:
        """Split the packages/links by hoster.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: List of package IDs that are changed.
        :type package_ids: List[int]
        """

        params = [link_ids, package_ids]
        self.action("/splitPackageByHoster", params)

    def start_online_status_check(
        self, link_ids: List[int] = [], package_ids: List[int] = []
    ) -> None:
        """Start an online status check for links and packages.

        :param link_ids: Link IDs that are used
        :type link_ids: List[int]
        :param package_ids: List of package IDs that are changed.
        :type package_ids: List[int]
        """

        params = [link_ids, package_ids]
        self.action("/startOnlineStatusCheck", params)

    def unskip(
        self,
        link_ids: List[int] = [],
        package_ids: List[int] = [],
        filter_by_reason: Reason = Reason.DISK_FULL,
    ) -> bool:
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
        resp = self.action("/unskip", params)
        return resp
