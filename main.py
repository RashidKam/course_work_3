from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_all_posts():
    pass

app.run()
