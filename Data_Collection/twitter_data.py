from TwitterAPI import TwitterAPI
import json
import _pickle as pickle

def format_tweet(json_in):
	formatted_dict = {}
	formatted_dict["name"] = json_in["user"]["name"]
	formatted_dict["text"] = json_in["text"]
	formatted_dict["hashtags"] = json_in["entities"]["hashtags"]
	formatted_dict["date"] = json_in["created_at"]

	return formatted_dict

consumer_key = "qDOiApw92OHnULVldqwF4NcUe"
consumer_secret = "powmmGUUFYEZfrXT9keJfiovHVwJ4Xh2JtPi5VaL9BXQQNORoL"
access_token_key = "1095426590236790784-F07f4ygvHKwKFuHkops9ZBcWyTqVvC"
access_token_secret = "4vlPlSPTD6cjs44i2aVhsJZ7aiSGitEHLc2sEgtSVzO58"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
json_objects = []

for i in range(0,12):
	fromDate = 201501010000 + (i*(10**6))
	toDate = 201501282359 + (i*(10**6))
	r = api.request('tweets/search/fullarchive/:twitai', {'query':'#irony lang:en', 'maxResults':'100', 'fromDate':str(fromDate), 'toDate':str(toDate)})
	for item in r:
		data_dict = json.loads(json.dumps(item))
		if data_dict['in_reply_to_status_id'] == None and data_dict['is_quote_status'] == False and data_dict["truncated"] == False and not 'retweeted_status' in data_dict:
			formatted_data = format_tweet(data_dict)
			json_objects.append(formatted_data)

f = open('twitter_irony_2015.pickle', mode='wb')
pickle.dump(json_objects, f)
f.close()
