from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
    0: {
        'post_id': 0,
        'title': 'Namaste!',
        'content': 'How are you amigo!?'
    }
}


@app.route('/')
def home():
    return 'Hello world!! Chomu!'


@app.route('/post/<int:post_id>')   # integer : post id (means which post) #/post/0
def post(post_id):
    post = posts.get(post_id)
    if not post:   # post will br None if not found, None => True
        return render_template('error.jinja2', message=f'A post with Id No. {post_id} was not found.')
    return render_template('post.jinja2', post=post)


@app.route('/post/form')
def form():
    return render_template('form.jinja2')


@app.route('/post/create', methods=['POST'])
def create():
    title = request.form.get('title') # args in request attaches the data with url address bar so data is not hidden but form and POST creates
    content = request.form.get('content') # a hidden payload which secures the data instead of attaching the data in the address bar
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}
    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
