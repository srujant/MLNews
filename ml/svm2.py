import pandas as pd
import numpy as np
from sklearn import datasets, svm
import sys
sys.path.append("..")
#import NLProcessor
import pprint
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords 
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import random
from sklearn import linear_model, cross_validation





file_name = './data/fake.csv'
test_file = './data/test.csv'


def clean(s):
	letters_only = re.sub("[^a-zA-Z]", " ", s) 
	words = letters_only.lower().split()
	stops = set(stopwords.words("english"))
	meaningful_words = [w for w in words if not w in stops]
	return( " ".join( meaningful_words ))




# def clean(s):
# 	letters_only = re.sub("[^a-zA-Z]", " ", s) 
# 	words = letters_only.lower().split()
# 	stops = set(stopwords.words("english"))
# 	meaningful_words = [w for w in words if not w in stops]
# 	return( " ".join( meaningful_words ))


# def get_ngrams(text, n ):
# 	n_grams = ngrams(word_tokenize(text), n)
# 	return [ ' '.join(grams) for grams in n_grams]



'''
def compute():
	df = pd.read_csv(file_name, skiprows = 0, nrows=1000)	
	train, test = train_test_split(df, test_size = 0.05)


	train = train[train["language"]=="english"]
	test = test[test["language"]=="english"]


	train["text"].fillna(" ",inplace=True)    
	train["text"] = train["text"].apply(clean)
	train["author"].fillna(" ",inplace=True)    
	train["author"] = train["author"].apply(clean)
	train["site_url"].fillna(" ",inplace=True)    
	train["site_url"] = train["site_url"].apply(clean)
	train["title"].fillna(" ",inplace=True)    
	train["title"] = train["title"].apply(clean)


	#train["thread_title"].fillna(" ",inplace=True)    
	#train["thread_title"] = train["thread_title"].apply(clean)
	
	vec = CountVectorizer(analyzer = "word", max_features = 5000) 
	train["text"] = vec.fit_transform(train["text"]).toarray()
	train["author"] = vec.fit_transform(train["author"]).toarray()
	train["site_url"] = vec.fit_transform(train["site_url"]).toarray()
	train["title"] = vec.fit_transform(train["title"]).toarray()
	#train["thread_title"] = vec.fit_transform(train["thread_title"]).toarray()

	d = np.sum(train, axis=0)

	#train["domain_rank"].fillna(train.domain_rank.median(axis=0),inplace=True)
	#test["domain_rank"].fillna(test.domain_rank.median(axis=0),inplace=True)

	train["isSpam"] = np.sign(train["spam_score"]-0.5)

	forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
	features_forest = train[["text", "author", "site_url", "title"]].values
	my_f = forest.fit(features_forest, train["isSpam"])

	

	target = train["isSpam"].values

	print(my_f.score(features_forest, target))
	

	test = [
		['Democrats who used to work on Capitol Hill are helping to disrupt Republican lawmakers town hall meetings across the country through a nationwide effort to oppose and resist President Donald Trump s agenda They call their group Indivisible Guide a name that came from an actual guide posted online telling activists how to pressure members of Congress Among topics what to say when going to town halls and calling or visiting a member s office Leaders of the organization have loose ties to George Soros the billionaire hedge fund manager who bankrolls liberal causes according to the Capital Research Center a conservative think tank that investigates nonprofits Board members of Indivisible Guide denied financial backing from Soros while the Capital Research Center argues that Indivisible Guide s board has indirect ties with left leaning groups funded by Soros as well as with other liberal organizations Indivisible Guide boasts that it has disrupted town halls held by Republican lawmakers in Utah California Pennsylvania Indiana Michigan and Nebraska And the group which amplifies its message over Twitter and other social media promises it isn t finished Politico reported that local activists shouted down Rep Justin Amash R Mich Police had to escort Rep Tom McClintock R Calif at a town hall meeting because of protesters One CNN report presented the disruption of a town hall meeting held Thursday night by Rep Jason Chaffetz R Utah as a sign of a grassroots reaction to Trump such as the taxpayer based tea party movement was against the Washington establishment The website of Indivisible Guide also known simply as Indivisible provides scripts for what activists should say when calling the office of their House or Senate members on various issues among them opposing senior Trump adviser Steve Bannon s role in the White House Trump s nomination of Neil Gorsuch to the Supreme Court his refugee policy and most other policy positions The website says More than 4 500 local groups have signed up to resist the Trump agenda in nearly every congressional district in the country What s more you all are putting the guide into action showing up en masse to congressional district offices and events and flooding the congressional phone lines You re resisting and it s working we want to demystify the heck out of Congress and build a vibrant community of angelic troublemakers Longstanding liberal groups MoveOn the Working Families Party and the ACLU have joined Indivisible Guide s effort Just two days after Trump s Jan 20 inauguration Indivisible Guide MoveOn org and the Working Families Party organized a teleconference for activists that attracted 60 000 listeners Politico reported Indivisible did another call with the ACLU focusing on Trump s executive order aimed at increasing the vetting of immigrants from seven terrorism prone Middle Eastern countries it drew about 35 000 listeners MoveOn org is conducting Resist Trump rallies across the country The ACLU issued pamphlets about how to demonstrate including for protesters who attempted to disrupt Washington during Trump s inauguration In running for the Democratic presidential nomination Sen Bernie Sanders I Vt called the Working Families Party the closest thing there is to a political party that believes in my vision of democratic socialism ',
		'Fred Lucas',
		'http://dailysignal.com/',
		"POLITICSNEWS Indivisible With Ties to George Soros Sows Division Against Trump GOP Lawmakers"

		]
	]

	#print forest.predict(test)


	
	input = get_ngrams(input, 4)
	

	

	pipeline = Pipeline([
	    ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
	    ('classifier',       MultinomialNB())
	])

	ngram_counter = CountVectorizer(ngram_range=(1, 4), analyzer='word')
	X_train = ngram_counter.fit_transform((input))
	#X_test  = ngram_counter.transform(df_goal)
	goal = ["bias"] * 88
	print X_train

	

	
	from sklearn.utils import shuffle
	X_train, goal = shuffle(X_train, goal)
	classifier = LinearSVC()
	model = classifier.fit(X_train, goal)


	
	#output = NLProcessor.getMLP(input)
	#del output[-1]
	#pprint.pprint(output)

	#labels = ['entities', 'ngrams', 'sentiment']
	#df = pd.DataFrame.from_records(output, columns=labels)
	#labels = ['entities', 'ngrams']
	#df = pd.DataFrame.from_records(output, columns=labels)
	#print df
	
	#clf = svm.SVC(gamma=0.001, C=100.)
	#clf.fit(df[:-1],df_goal[:-1]) 
	
	'''


def read():
	
	global df
	
	df = pd.read_csv(file_name)	
	
	df_goal = df['type']

	df = df[df['type'].isin(['bias', 'fake', 'conspiracy', 'real'])]
	df["text"].fillna(" ",inplace=True)  
	df["type"].fillna(" ",inplace=True)  
	global input
	df['text'] = df['text'].str.replace(r'[^\w]', ' ')

	

	#input = df.loc['text']
	#input = re.sub(r'[^\w]', ' ', input)
	
	#input = df_bias.loc[0]['text']
	
	#return


def compute():
	

	'''
	read()
	preds = []
	count_vectorizer = CountVectorizer()
	counts = count_vectorizer.fit_transform(df['text'].values)

	classifier = MultinomialNB()
	targets = df['type'].values
	classifier.fit(counts, targets)


	text = count_vectorizer.transform(text)
	preds.append(classifier.predict(text))

	return preds
	'''


	
	read()
	preds = []
	v = CountVectorizer(ngram_range=(1,3), stop_words='english')
	
	
	
	
	X = v.fit_transform(df['text'].values)
	y = df['type']
	
	logreg = linear_model.LogisticRegression(C=1, penalty='l1')
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

	model = logreg.fit(X_train, y_train)
	df_test = pd.read_csv(test_file, skiprows = 0)	


	

	df_test2 = pd.read_csv(file_name, skiprows = 0, nrows=20, usecols=['type', 'text'])	
	X_test=v.transform(df_test['text'].values)
	X_test_2=v.transform(df_test2['text'].values)


	print df_test2

	df_test = pd.read_csv(test_file, skiprows = 0)
	
	
	prediction = model.predict_proba(X_test)
	print prediction

	prediction = model.predict_proba(X_test_2)
	print prediction
	
	
compute()
