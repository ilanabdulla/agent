import os , urllib.parse , urllib.request , render_template

gemini_api_key = "Gemini_API_Key";

def home()
 return render_template (" indexx.html;")

def create_app():
  app = Flask(_name_)
  app.register_blueprint(youtube_bp, url_)prefix ="/youtube")

@app.route("/html")
def html():
  return render_template("index.html")

return app;






