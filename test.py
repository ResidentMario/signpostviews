from pageviews import PageviewsClient


p = PageviewsClient()
print(p.article_views('en.wikipedia', ['GNU/Linux naming controversy'.replace(" ", "_").replace('/', '%2F')]))
