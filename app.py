from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__, static_folder='static')

DEALS = [
  {
    'id': 1,
    'title': 'PHONES',
    'description': "IPHONE'S",
    'sales': '90% off',
    'image': 'phones1.jpg'
  },
  {
    'id': 2,
    'title': 'LAPTOPS',
    'description': "del",
    'sales': '50% off',
    'image': 'laptop1.jpg'
  },
  {
    'id': 3,
    'title': 'HEAD PHONES',
    'description': "sony",
    'sales': '40% off',
    'image': 'laptop2.jpg'
  },
  {
    'id': 4,
    'title': 'TVs',
    'description': "sony",
    'sales': '80% off',
    'image': 'tv.jpg'
  },
]


@app.route('/')
def Affliate_website():
  for deal in DEALS:
    print(deal['image'])
  return render_template("index.html", deals=DEALS, abdi='Affiliates')


@app.route("/apideal")
def list_deals():
  return jsonify(DEALS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
