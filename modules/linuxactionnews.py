import web

def get_episode_link(css_item):
    paths = css_item.cssselect("a")

    if len(paths) > 0:
        return paths[0].attr["href"]

    raise web.UrlError("No URL for the episode", "0")

def get_resource(url):
    return LANDownload(url)

class LANDownload(web.WebResource):

    def __init__(self, url):
        web.WebResource.__init__(self, url)

    def getEpisodeUrls(self):
        dom = self.getDomObject()

        items = dom.cssselect("ul li div")

        elinks = []

        for item in items:
            episode_link = get_episode_link(item)
            elinks.append( web.urljoin(self.url, episode_link) )
        return elinks

    def getEpisodeMeta(self, url):
        pass

    def getEpisodeData(self, url):
        pass
