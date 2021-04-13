from flask import Flask, render_template, request, redirect
import dbm
import random, string

def shorten_url(inpt, url):
    urls = dbm.open('urls.db','c')
    shortened_url = ''.join(random.choice(string.ascii_letters) for _ in range(10)) 
    urls[shortened_url] = inpt
    urls.close()
    return f"{ url }url/{ shortened_url }"

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/url", methods=['GET','POST'])
def url():
    if request.method == "POST":
        shortened_url = shorten_url(request.form['url'], request.url_root)
        return render_template('url.html', shortened_url=shortened_url)
    else: 
        return render_template('url.html')
    
@app.route("/url/<string:shortened_url>")
def lengthen_url(shortened_url=""):
    url = ""
    try:
        urls = dbm.open('urls.db','c')
        url = urls[shortened_url]
        print(shortened_url)
        print(url)
        urls.close()
    except KeyError:
        return render_template('error.html')
    return redirect(f"https://{url.decode('utf-8')}")
    

if __name__ == "__main__":
    app.run(debug=True)
