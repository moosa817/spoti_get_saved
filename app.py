# flask app with / route
from flask import Flask, render_template,request
import get_saved
#app 
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    # if method get
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    print(ip)
    code = request.args.get('code')
    if code != None:
            print(code)
            print("im going here")
            fo = open("static/saved.txt","w")
            fo.write("")
            tracks = get_saved.liked(code)
            for i in tracks:
                f = open('static/saved.txt','a')
                f.write(i+"\n")
            return render_template('index.html',code=code,tracks=tracks,href="saved.txt")
    else:
        return render_template('index.html',code=None,tracks=None)


if __name__ == '__main__':
    app.run(debug=True,port=8000)
