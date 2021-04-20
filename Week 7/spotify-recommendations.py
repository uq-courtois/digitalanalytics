import requests
import json

# Setting headers 
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQB6s7wihW42D6Lgfr8bOEKdGc3XNHzl2t9SBFq4u7UJ3Wj4Q8VcVll8JClldfiECyYQifsu9NsCE62FNR-l4n6KJUf6oI4NVQivfu3kyjjsQH--G7nhMHraknjWjVEpCbW0ataOieXTn6zV87seXaiRZ3qsQEnAZdyVb9BjfU-AvswswMDyu7AF1kMt_q2iW8TMRqwM7oTyRMyIlawN3D8a2n0Qv2lAjYcZ15MGmKFDzrpzlcjIi5WNba16CvBsLop_qRPpTFhHsBWcaA',
}
# You need to change the Authorization code each into your own fresh API Token, e.g., at the bottom of this page:
# https://developer.spotify.com/console/get-recommendations/

# Setting parameters
params = (
    ('market', 'US'), # This is optional, it restricts the responses to tracks available on the US market
    ('seed_artists', '2NjfBq1NflQcKSeiDooVjY'),
    ('seed_tracks', '0UywfDKYlyiu1b38DRrzYD'),
    ('min_energy', '0.4'), # This is optional, it restricts the responses to tracks with a minimum energy level - Spotify analyses tracks for their characteristics
    ('min_popularity', '50'), # This is optional, it restricts the responses to tracks with higher popularity stats
)

response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params) # Making request
print(response) # Optional, informs on whether call was successful (Code [200])
json_data = json.loads(response.text) # Converting response into Python data structure

# Printing the tracks by artists, one by one
for track in json_data['tracks']:
	print(,track['name'],'by',track['album']['artists'][0]['name'])
