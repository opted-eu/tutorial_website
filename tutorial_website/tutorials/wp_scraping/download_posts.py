from pathlib import Path
import json
from lib.wpapi import WPApi
from bs4 import BeautifulSoup # Helper to remove unwanted HTML

p = Path.cwd() # get current working directory
output_dir = p / 'output' / 'order-order.com'

if not output_dir.exists():
    output_dir.mkdir(parents=True)

target = "https://order-order.com/"

wordpress = WPApi(target)

info = wordpress.get_basic_info()

users = wordpress.get_users()
authors = {user['id']: user['name'] for user in users}

categories = wordpress.get_categories()
categories = {c['id']: c['name'] for c in categories}

tags = wordpress.get_tags()
tags = {t['id']: t['name'] for t in tags}

for post in wordpress.yield_posts(num=100):
    post_id = post['id']
    print(post_id)

    cleaned_post = {'id': post_id,
                    'link': post['link'],
                    'date_published': post['date'],
                    'date_modified': post['modified']}

    title = BeautifulSoup(post['title']['rendered'])
    cleaned_post['title'] = post['title']['rendered']

    content = BeautifulSoup(post['content']['rendered'])
    cleaned_post['content'] = content.text

    excerpt = BeautifulSoup(post['excerpt']['rendered'])
    cleaned_post['excerpt'] = excerpt.text

    cleaned_post['author'] = authors[post['author']]
    cleaned_post['categories'] = [categories[c] for c in post['categories']]
    cleaned_post['tags'] = [tags[t] for t in post['tags']]

    with open(output_dir / f'{post_id}.json', 'w', encoding="utf8") as f:
        json.dump(cleaned_post, f, ensure_ascii=False)

print('Done!')