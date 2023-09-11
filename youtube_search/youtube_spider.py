import scrapy


class YouTubeSpider(scrapy.Spider):
    name = 'youtube'

    def __init__(self, query='', *args, **kwargs):
        super(YouTubeSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.youtube.com/results?search_query={query}']

    def parse(self, response):
        video_titles = response.css('yt-formatted-string.style-scope.ytd-video-renderer::text').getall()[:10]

        for title in video_titles:
            yield {
                'title': title.strip()
            }
