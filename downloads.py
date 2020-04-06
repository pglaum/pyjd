from pyjd import make_request
from pyjd.jd_types import DownloadLink, FilePackage, LinkQuery, PackageQuery

endpoint = 'downloadsV2'


def action(route, params=None):
    route = f'{endpoint}{route}'
    return make_request(route, params)


def cleanup(link_ids, package_ids, action, mode, selection_type):

    params = [link_ids, package_ids, action.value, mode.value,
              selection_type.value]
    resp = action("/cleanup", params)
    return resp


def force_download(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/forceDownload", params)
    return resp


def get_download_urls(link_ids, package_ids, url_display_type):

    params = [link_ids, package_ids, url_display_type]
    resp = action("/getDownloadUrls", params)
    return resp


def get_stop_mark():

    resp = action("/getStopMark")
    return resp


def get_stop_marked_link():

    resp = action("/getStopMarkedLink")
    download_link = DownloadLink(resp)
    return download_link


def get_structure_change_counter(old_counter_value):

    params = [old_counter_value]
    resp = action("/getStructureChangeCounter", params)
    return resp


def move_links(link_ids, after_link_id, dest_package_id):

    params = [link_ids, after_link_id, dest_package_id]
    resp = action("/moveLinks", params)
    return resp


def move_packages(package_ids, after_dest_package_id):

    params = [package_ids, after_dest_package_id]
    resp = action("/movePackages", params)
    return resp


def move_to_new_package(link_ids, pkg_ids, new_pkg_name, download_path):

    params = [link_ids, pkg_ids, new_pkg_name, download_path]
    resp = action("/movetoNewPackage", params)
    return resp


def package_count():

    resp = action("/packageCount")
    return resp


def query_links(query_params=LinkQuery()):

    params = [query_params.to_dict()]
    resp = action("/queryLinks", params)

    download_links = []
    for link in resp:
        download_link = DownloadLink(link)
        download_links.append(download_link)

    return download_links


def query_packages(query_params=PackageQuery()):

    params = [query_params.to_dict()]
    resp = action("/queryPackages", params)

    download_packages = []
    for package in resp:
        download_package = FilePackage(package)
        download_packages.append(download_package)

    return download_packages


def remove_links(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/removeLinks", params)
    return resp


def remove_stop_mark():

    resp = action("/removeStopMark")
    return resp


def rename_link(link, new_name):

    params = [link, new_name]
    resp = action("/renameLink", params)
    return resp


def rename_package(package_id, new_name):

    params = [package_id, new_name]
    resp = action("/renamePackage", params)
    return resp


def reset_links(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/resetLinks", params)
    return resp


def resume_links(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/resumeLinks", params)
    return resp


def set_download_directory(directory, package_ids):

    params = [directory, package_ids]
    resp = action("/setDownloadDirectory", params)
    return resp


def set_download_password(link_ids, package_ids, password):

    params = [link_ids, package_ids, password]
    resp = action("/setDownloadPassword", params)
    return resp


def set_enabled(enabled, link_ids, package_ids):

    params = [enabled, link_ids, package_ids]
    resp = action("/setEnabled", params)
    return resp


def set_priority(priority, link_ids, package_ids):

    params = [priority.value, link_ids, package_ids]
    resp = action("/setPriority", params)
    return resp


def set_stop_mark(link_id, package_id):

    params = [link_id, package_id]
    resp = action("/setStopMark", params)
    return resp


def split_package_by_hoster(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/splitPackageByHoster", params)
    return resp


def start_online_status_check(link_ids, package_ids):

    params = [link_ids, package_ids]
    resp = action("/startOnlineStatusCheck", params)
    return resp


def unskip(package_ids, link_ids, filter_by_reason):

    params = [package_ids, link_ids, filter_by_reason.value]
    resp = action("/unskip", params)
    return resp
