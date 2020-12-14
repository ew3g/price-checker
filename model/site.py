from model.siteType import SiteType


class Site:

    def __init__(self, site_type: SiteType, url):
        self._site_type = site_type
        self._url = url

    @property
    def site_type(self):
        return self._site_type

    @site_type.setter
    def site_type(self, value: SiteType):
        self._site_type = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
