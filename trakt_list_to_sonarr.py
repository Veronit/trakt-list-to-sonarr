import json
import requests
import logging

logging.basicConfig(filename='trakt_list_to_sonarr.log',level=logging.DEBUG)

#--------------------------------------------------------------------
#Change these

traktBaseUrl = 'https://api.trakt.tv'
traktApiKey = '<your trakt api key>'
traktList = '<your trakt list to import to sonarr>'

sonarrBaseurl = 'http://<your sonarr address with port. eg 192.168.0.1:8989>'
sonarrApikey = '<your sonarr api key>'

qualityProfileId = '<wanted quality profile id, get these from api>'
rootFolderPath = '<root folder path on sonarr>'

#Stop changing things
#--------------------------------------------------------------------

#Trakt get list
headers = {
  'Content-Type': 'application/json',
  'trakt-api-version': '2',
  'trakt-api-key': traktApiKey
}

logging.info('Searching for items on list: ' + traktList)
url = traktBaseUrl + '/users/veron_/lists/'+ traktList +'/items'
response = requests.get(url, headers=headers)
response_body = json.loads(response.content)

numberOfSeries = len(response_body)
logging.info('Found '+ str(numberOfSeries) +' shows on list')

for x in range (0, numberOfSeries):
	tvdbId = response_body[x]['show']['ids']['tvdb']
	title = response_body[x]['show']['title']
	titleSlug = response_body[x]['show']['ids']['slug']

	#Sonarr post series
	headers = {
		'Content-Type': 'application/json', 
		'X-Api-Key': sonarrApikey,
		'Accept':'application/json'
		}

	post_data = {
		"monitored": 'false', 
		"tvdbId": tvdbId, 
		"title": title, 
		"titleSlug": titleSlug, 
		"seasonFolder": 'true', 
		"qualityProfileId": qualityProfileId, 
		"rootFolderPath": rootFolderPath, 
		"seasons": [{
			"monitored": 'false', 
			"seasonNumber": 1
		}],
		"addOptions": {
			"searchForMissingEpisodes": 'false', 
			"ignoreEpisodesWithFiles": 'false'
		}
	}
	url = sonarrBaseurl + '/api/series'
	logging.info('Adding show: ' + title + ' to Sonarr')
	response = requests.post(url=url, json=post_data, headers=headers)
	if response.ok:
		logging.info('Success!')
	else:
		logging.info('Problem. See log for more details')
		logging.debug('Response: ' + response.content)
