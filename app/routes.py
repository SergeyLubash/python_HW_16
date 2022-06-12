from app import models, db
from flask import current_app as app, jsonify, abort, request
from datetime import datetime


@app.route('/users', methods=['GET'])
def get_users():
    """ Возвращает список пользователей"""
    users = db.session.query(models.User).all()
    return jsonify([user.serialize() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """ Возвращает пользователя по id"""
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@app.route('/orders', methods=['GET'])
def get_orders():
    """ Возвращает заказы"""
    orders = db.session.query(models.Order).all()

    return jsonify([order.serialize() for order in orders])


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """ Возвращает заказ по id"""
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())


@app.route('/offers', methods=['GET'])
def get_offers():
    """ Возвращает предложения"""
    offers = db.session.query(models.Offer).all()

    return jsonify([offer.serialize() for offer in offers])


@app.route('/offers/<int:offer_id>', methods=['GET'])
def get_offer(offer_id):
    """ Возвращает предложение по id"""
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


@app.route('/users', methods=['POST'])
def create_user():
    """ Добавляем пользователя """
    data = request.json

    db.session.add(models.User(**data))

    db.session.commit()

    return "Пользователь создан в базе данных"


@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    """ Изменяем данные пользователя по id"""
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()

    return "Данные пользователя изменены в базе данных"


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ Удаляем пользователя по id"""

    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return "Пользователь удален из базы данных"


@app.route('/orders', methods=['POST'])
def create_order():
    """ Добавляем заказ """
    data = request.json
    for field_name, field_value in data.items():
        if isinstance(field_value, str) and field_value.count('/') == 2:
            data[field_name] = datetime.strptime(field_value, '%m/%d/%Y')

    db.session.add(models.Order(**data))

    db.session.commit()

    return "Заказ добавлен в базу данных"


@app.route('/orders/<int:order_id>', methods=['PUT'])
def edit_order(order_id):
    """ Изменяем заказ по id"""
    data = request.json

    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)
    db.session.commit()

    return "Заказ изменен в базе данных"


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """ Удаляем заказ по id"""

    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return "Заказ удален из базы данных"


@app.route('/offers', methods=['POST'])
def create_offer():
    """ Добавляем предложение """
    data = request.json

    db.session.add(models.Offer(**data))

    db.session.commit()

    return "Предложение добавлено в базу данных"


@app.route('/offers/<int:offer_id>', methods=['PUT'])
def edit_offer(offer_id):
    """ Изменяем предложение по id"""
    data = request.json

    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    if offer is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)
    db.session.commit()

    return "Предложение изменено в базе данных"


@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    """ Удаляем предложение по id"""

    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return "Предложение удалено из базы данных"
