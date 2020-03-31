import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQB6s7wihW42D6Lgfr8bOEKdGc3XNHzl2t9SBFq4u7UJ3Wj4Q8VcVll8JClldfiECyYQifsu9NsCE62FNR-l4n6KJUf6oI4NVQivfu3kyjjsQH--G7nhMHraknjWjVEpCbW0ataOieXTn6zV87seXaiRZ3qsQEnAZdyVb9BjfU-AvswswMDyu7AF1kMt_q2iW8TMRqwM7oTyRMyIlawN3D8a2n0Qv2lAjYcZ15MGmKFDzrpzlcjIi5WNba16CvBsLop_qRPpTFhHsBWcaA',
}

params = (
    ('market', 'US'),
    ('seed_artists', '2NjfBq1NflQcKSeiDooVjY'),
    ('seed_tracks', '0UywfDKYlyiu1b38DRrzYD'),
    ('min_energy', '0.4'),
    ('min_popularity', '50'),
)

response = requests.get('https://api.spotify.com/v1/recommendations', headers=headers, params=params)

json_data = json.loads(response.text)

for track in json_data['tracks']:
	print(track['name'],'by',track['album']['artists'][0]['name'])
