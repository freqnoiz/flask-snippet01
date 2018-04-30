from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xe71\r+\x1d\xd2\xec!3q&B\xa8\x02\x01\x9f\xec@E\x98\xe1\xb4\x1f\xc7'
  
@app.route('/')
def home():
    return render_template('index.html')

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
