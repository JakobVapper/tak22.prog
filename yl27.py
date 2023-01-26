import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='8qiSdCJgNsw9vd34B0mAWw', \
                     client_secret='7DLe8FsO8PEspzdLsagEsZIycvfzDg', \
                     user_agent='Scraper', \
                     username='5467hfyhfh', \
                     password='abc123456')

subredditname = "Eesti"

subreddit = reddit.subreddit(subredditname)

top_subbreddit = subreddit.top()
count = 0
max = 10000
print('success')
words = []
wordCount = {}
commonWords = {'ja','aga','ei','ok','kas','mina','millal','kuidas','that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even','välja','oleks','veel','ära',
'said','only','want','other','into','He','what','i','That','thought','et','nii','seda','pole','mis','oli','ma','ka','siis','kui','kui',
'think',"that's",'Is','much','Eesti','nagu','See','ikka','selle','kes','Ma','oma','või','väga','ta','mingi','Kui','juba','seal'}

for submission in subreddit.top(limit=500):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    if(count == max):
            break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

labels = keyWords
sizes = keyCount

plt.title('Top comments for: r/' + subredditname)
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')

plt.show()