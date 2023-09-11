from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        subprocess.run(["shub", "schedule", "youtube_spider", "-a", f"query={query}"])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
