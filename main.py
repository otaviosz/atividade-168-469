from flask import Flask, render_templates
app = Flask('app')

@app.route('/')
def index():
  return render_templates('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)