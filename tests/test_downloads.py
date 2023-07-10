from . import get_jdownloader
from time import sleep


class TestDownloads:
    @classmethod
    def setup_class(cls):
        cls.jdownloader = get_jdownloader()

    def test_cleanup(self):
        assert self.jdownloader.downloads.cleanup() is True

    def test_force_download(self):
        self.jdownloader.downloads.force_download()

    def test_get_download_urls(self):
        # self.jdownloader.downloads.get_download_urls()
        pass

    def test_get_stop_mark(self):
        self.jdownloader.downloads.get_stop_mark()

    def test_get_stop_marked_link(self):
        self.jdownloader.downloads.get_stop_marked_link()

    def test_get_structure_change_counter(self):
        self.jdownloader.downloads.get_structure_change_counter()

    def test_move_links(self):
        self.jdownloader.downloads.move_links()

    def test_move_packages(self):
        self.jdownloader.downloads.move_packages()

    def test_move_to_new_package(self):
        self.jdownloader.downloads.move_to_new_package()

    def test_package_count(self):
        self.jdownloader.downloads.package_count()

    def test_query_links(self):
        self.jdownloader.downloads.query_links()

    def test_query_packages(self):
        self.jdownloader.downloads.query_packages()

    def test_remove_links(self):
        self.jdownloader.downloads.remove_links()

    def test_remove_stop_mark(self):
        self.jdownloader.downloads.remove_stop_mark()

    def test_rename_link(self):
        self.jdownloader.downloads.rename_link()

    def test_rename_package(self):
        self.jdownloader.downloads.rename_package()

    def test_reset_links(self):
        self.jdownloader.downloads.reset_links()

    def test_resume_links(self):
        self.jdownloader.downloads.resume_links()

    def test_set_download_directory(self):
        self.jdownloader.downloads.set_download_directory()

    def test_set_download_password(self):
        self.jdownloader.downloads.set_download_password()

    def test_set_enabled(self):
        self.jdownloader.downloads.set_enabled()

    def test_set_priority(self):
        self.jdownloader.downloads.set_priority()

    def test_set_stop_mark(self):
        self.jdownloader.downloads.set_stop_mark()

    def test_split_package_by_hoster(self):
        self.jdownloader.downloads.split_package_by_hoster()

    def test_start_online_status_check(self):
        self.jdownloader.downloads.start_online_status_check()

    def test_unskip(self):
        self.jdownloader.downloads.unskip()
