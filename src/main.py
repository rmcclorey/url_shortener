from flask import Flask, render_template, request, redirect

from utils import shorten_url, lengthen_url

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def url():
    #if post request, generate the shortened url 
    if request.method == "POST":
        shortened_url = shorten_url(request.form['url'], request.url_root)
        return render_template('url.html', shortened_url=shortened_url)
    else: 
        return render_template('url.html')
    

@app.route("/<string:url>")
def redirect_link(url=""):
    url = lengthen_url(url)
    if(url == ""):
        return render_template('error.html')
    else:
        return redirect(f"https://{url.decode('utf-8')}")
    

if __name__ == "__main__":
    app.run(debug=True)
