from operator import itemgetter
from plotly import offline

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process information bout each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:28]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link':  f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
discussion_links, comments = [], []
for submission_dict in submission_dicts:
    discussion_url = submission_dict['hn_link']
    title = submission_dict['title']
    discussion_link = f"<a href='{discussion_url}'>{title}</a>"
    discussion_links.append(discussion_link)
    comment = submission_dict['comments']
    comments.append(comment)

# Make the bar.
data = [{'type': 'bar',
         'x': discussion_links,
         'y': comments}]
my_layout = {'title': "Most active discussions currently in Hacker News"}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="hn_most_active.html")
