from lib.wpapi import WPApi
from pprint import pprint # helper to pretty print output
from bs4 import BeautifulSoup # Helper to remove unwanted HTML

target = "https://order-order.com/"

wordpress = WPApi(target)

info = wordpress.get_basic_info()
pprint(info)

# get count of all posts

total_posts = wordpress.total_posts()
print(total_posts)

# Explore categories

categories = wordpress.get_categories()
print(len(categories))

for category in categories:
    print(category['name'], category['id'])

# show authors

users = wordpress.get_users()
print(len(users))
for user in users:
    print(user['name'], user['link'])


# search posts by keyword:

europe = wordpress.total_posts(search_terms='europe')
print(europe)

# get a single post and inspect it

posts = wordpress.get_posts(num=1)
print(len(posts))

post = posts[0]
print(post.keys())

# Reformat one post and remove unwanted information

cleaned_post = {'id': post['id'],
                'link': post['link'],
                'date_published': post['date'],
                'date_modified': post['modified']}

cleaned_post['title'] = post['title']['rendered']

# remove unwanted HTML fragments from the content

content = BeautifulSoup(post['content']['rendered'])
cleaned_post['content'] = content.text

excerpt = BeautifulSoup(post['excerpt']['rendered'])
cleaned_post['excerpt'] = excerpt.text

# Resolve author IDs

users = wordpress.get_users()
authors = {}
for user in users:
    authors[user['id']] = user['name']

cleaned_post['author'] = authors[post['author']]

# Resolve Category IDs
# we are using the shorthand notation here: 
# dictionary comprehension and list comprehension

categories = wordpress.get_categories()
categories = {c['id']: c['name'] for c in categories}

cleaned_post['categories'] = [categories[c] for c in post['categories']]

# Resolve Tag IDs
# If the blog has a lot of tags, this might take a while

tags = wordpress.get_tags()
tags = {t['id']: t['name'] for t in tags}

cleaned_post['tags'] = [tags[t] for t in post['tags']]

pprint(cleaned_post)