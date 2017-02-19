from pyteaser import SummarizeUrl
import itertools


url = "http://www.cnn.com/2017/02/18/politics/donald-trump-florida-campaign-rally/index.html" 
summaries = SummarizeUrl(url)
l1 = "".join(summaries)



url = "http://www.bbc.com/news/world-us-canada-39018096" 
summaries = SummarizeUrl(url)
l2 = "".join(summaries)

l1 = l1.split(" ")
l2 = l2.split(" ")
print list(set(l1) & set(l2))