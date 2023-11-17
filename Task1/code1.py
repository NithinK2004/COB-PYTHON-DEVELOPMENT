
from flask import Flask, render_template, request, redirect
import shortuuid

task1 = Flask(__name__)

# Dictionary to store the mapping of short URLs to original URLs
url_mapping = {}

@task1.route('/')
def index():
    return render_template('index.html')

@task1.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url')
    if original_url:
        # Generate a short unique ID using shortuuid
        short_id = shortuuid.uuid()[:8]
        short_url = request.url_root + short_id
        # Store the mapping in the dictionary
        url_mapping[short_id] = original_url
        return render_template('index.html', original_url=original_url, short_url=short_url)
    else:
        return render_template('index.html', error='Please enter a valid URL.')

@task1.route('/<short_id>')
def redirect_to_original(short_id):
    # Retrieve the original URL from the dictionary
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('index.html', error='Short URL not found.')

if __name__ == '__main__':
    task1.run(debug=True)￼Enter
