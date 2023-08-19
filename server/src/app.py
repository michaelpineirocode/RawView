from flask import Flask, render_template, request
import os
import time
import dropbox

app = Flask(__name__)

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route('/')
def index():
    context = { 'server_time': format_server_time() }
    return render_template('index.html', context=context)

@app.route('/get')
def getPhotos():
    url = request.args.get('url') 
    # ACCESS_TOKEN = 'sl.BkeZ7J0Lafyig8A-RkyyHqgKRKUl585pyHIpW8PG65y___aAziC8s0BN4aXWYzgYruktqKScLPmXC6bWNqlxaPsaeTsNSN58wBmXZGEQ72Ugk4xvC6GVRlndUBgdFyP-8xHKhogMkhpe'
    # dbx = dropbox.Dropbox(ACCESS_TOKEN)
    # directLink = url[:-1] + '1'
    # response = dbx.sharing_get_shared_link_file(url=directLink)

    # # Read the file data
    # file_data = response.content

    # Process the file data as needed
    return "Success", 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))