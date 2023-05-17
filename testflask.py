from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample endpoint to retrieve product information
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Logic to fetch product information from database
    # Replace the code below with your actual implementation
    product = {
        'id': product_id,
        'name': 'Sample Product',
        'price': 19.99,
        'description': 'This is a sample product.',
    }
    return jsonify(product)

# Sample endpoint to add a product to the shopping cart
@app.route('/api/cart', methods=['POST','OPTIONS'])
def add_to_cart():
    # Extract product details from the request
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    # Logic to add product to the shopping cart
    # Replace the code below with your actual implementation
    cart_item = {
        'product_id': product_id,
        'quantity': quantity,
    }
    return jsonify(cart_item)

# Sample endpoint to place an order
@app.route('/api/orders', methods=['POST'])
def place_order():
    # Extract order details from the request
    items = request.json.get('items')
    total_amount = request.json.get('total_amount')

    # Logic to place the order
    # Replace the code below with your actual implementation
    order = {
        'items': items,
        'total_amount': total_amount,
        'status': 'placed',
    }
    return jsonify(order)

if __name__ == '__main__':
    app.run(debug=True)
