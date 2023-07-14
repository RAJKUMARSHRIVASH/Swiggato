from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Dish, Order

@app.route('/menu')
def menu():
    dishes = Dish.query.all()
    return render_template('menu.html', dishes=dishes)

@app.route('/')
def menu_home():
    return render_template('base.html')

@app.route('/new_order')
def new_order():
    return render_template('new_order.html')

@app.route('/edit_dish')
def edit_dish():
    return render_template('edit_dish.html')

@app.route('/review_orders')
def get_review_orders():
    return render_template('review_orders.html')

@app.route('/order_status')
def order_status():
    return render_template('order_status.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/add_dish')
def get_add_dish():
    return render_template('add_dish.html')

@app.route('/order')
def get_order():
    return render_template('order.html')

@app.route('/dishes/new', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        availability = bool(request.form.get('availability'))

        dish = Dish(name=name, price=price, availability=availability)
        db.session.add(dish)
        db.session.commit()

        return redirect(url_for('menu'))

    return render_template('add_dish.html')

@app.route('/dishes/<int:dish_id>/edit', methods=['GET', 'POST'])
def edit_dish_route(dish_id):
    dish = Dish.query.get_or_404(dish_id)

    if request.method == 'POST':
        dish.name = request.form['name']
        dish.price = float(request.form['price'])
        dish.availability = bool(request.form.get('availability'))

        db.session.commit()

        return redirect(url_for('menu'))

    return render_template('edit_dish.html', dish=dish)



@app.route('/dishes/<int:dish_id>/delete', methods=['POST'])
def delete_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)

    db.session.delete(dish)
    db.session.commit()

    return redirect(url_for('menu'))


@app.route('/orders/new', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_ids')

        # Validate dish IDs
        dishes = Dish.query.filter(Dish.id.in_(dish_ids)).all()
        if len(dishes) != len(dish_ids):
            flash('Invalid dish IDs')
            return redirect(url_for('new_order'))

        # Create a new order
        order = Order(customer_name=customer_name)
        for dish in dishes:
            order.dishes.append(dish)
        db.session.add(order)
        db.session.commit()

        flash('Order placed successfully!')
        return redirect(url_for('order_status', order_id=order.id))

    dishes = Dish.query.all()
    return render_template('new_order.html', dishes=dishes)


@app.route('/orders/<int:order_id>/status', methods=['GET', 'POST'])
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)

    if request.method == 'POST':
        new_status = request.form['status']
        order.status = new_status
        db.session.commit()

    return render_template('order_status.html', order=order)


@app.route('/orders/review')
def review_orders():
    orders = Order.query.all()
    return render_template('review_orders.html', orders=orders)


@app.route('/exit')
def exit_app():
    return 'Thank you for using Swiggato!'
