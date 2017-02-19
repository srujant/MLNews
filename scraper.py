import newspaper
url = u'http://www.cnbc.com/2017/02/18/heres-how-congress-is-handling-russia-investigations.html'
article = newspaper.Article(url)
article.download()
article.parse()
print(str(article.text.encode("ascii", "ignore").upper()))