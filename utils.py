import json
from flask import Flask, request, render_template
file_posts = 'data/posts.json'
file_comments = 'data/comments.json'


def get_posts_all(file):
    '''Возвращает посты'''
    with open(file, encoding='utf8') as list_posts:
        return json.load(list_posts)


def get_posts_by_user(user_name):
    '''Возвращает посты определённого пользователя'''
    user = 0
    user_posts = []
    posts = get_posts_all(file_posts)
    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            user_posts.append(post)
            user += 1
    try:
        user >= 1
    except:
        print('ValueError')
    else:
        return user_posts


def get_comments_by_post_id(post_id):
    '''Возвращает коменты к посту'''
    comments_by_post = []
    comments = get_posts_all(file_comments)
    for comment in comments:
        if int(post_id) == int(comment['post_id']):
            comments_by_post.append(comment)
    return comments_by_post


def search_for_posts(query):
    '''возвращает посты по ключевому слову'''
    list_posts = []
    posts = get_posts_all(file_posts)
    for post in posts:
        if query.lower() in post['content'].lower():
            list_posts.append(post)
    return list_posts


def get_post_by_pk(pk):
    '''Возвращет определенный пост'''
    posts = get_posts_all(file_posts)
    for post in posts:
        if int(pk) == int(post["pk"]):
            return post


