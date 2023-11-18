import json, config



def dict_key_value(d):
    return [{"key": k, "value": v} for k, v in d.items()]


def filter(products):
    filtered_products = []
    for product in products:
        if 'sizes' in product:
            filtered_sizes = [size for size in product['sizes'] if size['count'] > 0]
            product['sizes'] = filtered_sizes
            if filtered_sizes:
                filtered_products.append(product)
        elif 'colors' in product:
            filtered_colors = [color for color in product['colors'] if color['count'] > 0]
            product['colors'] = filtered_colors
            if filtered_colors:
                filtered_products.append(product)
        elif 'available' in product:
            if product['available']:
                filtered_products.append(product)
    return filtered_products


def update_save(products, product_id, size_id=None, color_id=None, save=True):
    # Find and change the count of the specific item
    for item in products:
        if item['id'] == product_id:
            if ("sizes" in item.keys()):
                for size in item['sizes']:
                    if size['size_id'] == size_id:
                        size['count'] -= 1
            if ("colors" in item.keys()):
                for size in item['colors']:
                    if size['color_id'] == color_id:
                        size['count'] -= 1
            elif ("available" in item.keys()):
                item['available'] -= 1
    
    # Save the updated dict
    if save:
        with open(config.products_path, 'w') as json_file:
            json.dump(products, json_file,  indent=4)


def record_sold_product(Product, db, product_id, name, size_id, color_id, price):
    row = Product(product_id=product_id, name=name, size_id=size_id, color_id=color_id, price=price)
    # Add the instances to the session
    db.session.add(row)
    # Commit the changes to the database
    db.session.commit()


def get_position(cell_positions, product_id, size_id=None, color_id=None):
    for item in cell_positions:
        if item['product_id'] == product_id:
            if size_id is None and color_id is None:
                return item['position']
                
            else:
                for position in item['positions']:
                    if size_id:
                        if (position['size_id'] == size_id):
                            return position['position']
                    if color_id:
                        if (position['color_id'] == color_id):
                            return position['position']
