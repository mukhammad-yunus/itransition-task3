from flask import Flask
from flask import request, make_response
from math import gcd
app = Flask(__name__)
def generate_response(value):
  res = make_response(value, 200)
  res.mimetype = "text/plain"
  return res

@app.route("/app/mukhammadyunus_sh_gmail_com")
def index():
  x = request.args.get("x", type=int)
  y = request.args.get("y", type=int)
  if(x is None or y is None):
    return generate_response("NaN")
  if(x < 0 or y < 0):
    return generate_response("NaN")
  if(x == 0 or y == 0):
    return generate_response("0")
  lcm = abs(x*y)//gcd(x, y)

  return generate_response(f"{lcm}")