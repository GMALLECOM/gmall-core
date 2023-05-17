from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Sample endpoint to retrieve product information
@csrf_exempt
def get_product(request, product_id):
    # Logic to fetch product information from database
    # Replace the code below with your actual implementation
    product = {
        'id': product_id,
        'name': 'Sample Product',
        'price': 19.99,
        'description': 'This is a sample product.',
    }
    return JsonResponse(product)

# Sample endpoint to add a product to the shopping cart
@csrf_exempt
def add_to_cart(request):
    # Extract product details from the request
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')

    # Logic to add product to the shopping cart
    # Replace the code below with your actual implementation
    cart_item = {
        'product_id': product_id,
        'quantity': quantity,
    }
    return JsonResponse(cart_item)

# Sample endpoint to place an order
@csrf_exempt
def place_order(request):
    # Extract order details from the request
    items = request.POST.get('items')
    total_amount = request.POST.get('total_amount')

    # Logic to place the order
    # Replace the code below with your actual implementation
    order = {
        'items': items,
        'total_amount': total_amount,
        'status': 'placed',
    }
    return JsonResponse(order)
