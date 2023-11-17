from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from utils import filter, dict_key_value, find_product_by_ids, record_sold_product
from config import products


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


# Add the filter to the Jinja2 environment
app.jinja_env.filters['dict_key_value'] = dict_key_value


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size_id = db.Column(db.Integer, nullable=True)
    # size = db.Column(db.String(255), nullable=True)
    color_id = db.Column(db.Integer, nullable=True)
    # color = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    items = filter(products)
    # print(items)
    if len(items):
        return render_template("index.html", items=items)
    else:
        return "All items have been sold"
        

@app.route('/process_form', methods=['POST', 'GET'])
def process_form():
    product_id = int(request.form.get('product_id'))
    name = request.form.get('product_name')
    size_id = request.form.get('sizeId')  
    size_id = int(size_id) if size_id else size_id
    color_id = request.form.get('colorId')
    color_id = int(color_id) if color_id else color_id
    price = request.form.get('product_price')

    # Add to the database
    record_sold_product(Product, db, product_id=product_id, name=name, size_id=size_id, color_id=color_id, price=price)
    
    # Update products dict
    find_product_by_ids(products, product_id, size_id=size_id, color_id=color_id)

    # flash(f"The selected product is: {name} | Color id: {color_id} | product id {product_id}", 'info')
    # return f"The selected product is: {username} | The selected size is: {size}"
    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)
