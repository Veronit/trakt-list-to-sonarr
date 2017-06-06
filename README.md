Small script that adds trakt lists to sonarr.

You need:
- Python 2.7 or 3 (haven't tested on 3)
- Requests- library (http://docs.python-requests.org/en/master/user/install/)
- Trakt API key. Create one from here: https://trakt.tv/oauth/applications
- Trakt list to be imported to sonarr
- Sonarr installed (duh.)
- Sonarr API key. Get your from here: http://-sonarr address:port-/settings/general
- Wanted quality profile id. Get it from here: https://github.com/Sonarr/Sonarr/wiki/Profile
- Root folder path

Change nessessary lines from skript and run it.
It logs something to file trakt_list_to_sonarr.log, make sure that the skript can write to the location.

Notes:
- Doesn't clear trakt list after importing series. Now it just skips existing ones.
  - I might work on that at somepoint
- All shows and seasons are automatically unmonitored
- Script doesn't search for missing episodes automatically.  
