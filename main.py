from flask import Flask
from flask import request, escape

app = Flask(__name__)

@app.route("/")
def index():
  celsius = str(escape(request.args.get("celsius", "")))
  if (celsius):
    fahrenheit = fahrenheit_from(celsius)
  else:
    fahrenheit = ""
  return(
    """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
              </form>"""
            + "Celsius: " + celsius
            + "<br>Fahrenheit: " + fahrenheit
  )

#@app.route("/<celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
