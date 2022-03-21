# flask app with / route
from flask import Flask, render_template,request
import get_saved
#app 
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    # if method get

    code = request.args.get('code')
    if code != {}:
        try:
            fo = open("static/saved.txt","w")
            fo.write("")
            tracks = get_saved.liked(code)
            for i in tracks:
                f = open('static/saved.txt','a')
                f.write(i+"\n")
            return render_template('index.html',code=code,tracks=tracks,href="saved.txt")
        except:
            return render_template('index.html',code=code)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=8000)