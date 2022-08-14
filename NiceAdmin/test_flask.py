from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/prediction', methods=['POST']) # , 'GET'
def prediction():
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        id=request.form.get('inputText')
        return "Your ID is %s" %id
    else:
        return render_template("pages-login.html")

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(host='127.0.0.1', port=5501, debug=True)
