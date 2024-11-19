from flask import Flask, render_template, request, redirect

app = Flask(__name__)
books = []  # List to store books

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    status = request.form['status']
    books.append({'title': title, 'author': author, 'status': status})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
