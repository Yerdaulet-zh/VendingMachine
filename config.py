# https://russian.alibaba.com/p-detail/Custom-1600946237279.html?spm=a2700.galleryofferlist.normal_offer.2.617b4f97ZOblGx
# https://russian.alibaba.com/p-detail/Custom-1600126973163.html?spm=a2700.galleryofferlist.normal_offer.d_title.458433e1guqS65
# https://russian.alibaba.com/p-detail/STARLII-1600946210398.html?spm=a2700.galleryofferlist.p_offer.2.296128b76lijDS&s=p
# https://russian.alibaba.com/p-detail/wholesale-60410982716.html?spm=a2700.galleryofferlist.normal_offer.d_title.72d93cf4PNyVw8
# https://russian.alibaba.com/p-detail/Wholesale-1600848337398.html?spm=a2700.galleryofferlist.normal_offer.d_title.129517e27WluQU
# https://russian.alibaba.com/p-detail/GITRA-1600186376243.html?spm=a2700.galleryofferlist.normal_offer.d_title.1682718dtu7xI2


from turtle import position


products = [
    {'id':1, 'name': 'T-shirt', 'image': 't-shirtuni.png', 'price': 4000, 'sizes': [
        {"size_id":1, "name": "S", "count": 2}, {"size_id":2, "name": "M", "count": 2}, {"size_id":3, "name": "L", "count": 2}, {"size_id":4, "name": "XL", "count": 2}, {"size_id":5, "name": "XXL", "count": 1}, 
    ],
    'info': [
        {"Peculiarity":	"Anti-flaking, Anti-shrink, Anti-wrinkle, Breathable, Resistant, Large size"},
        {"Fabric weight":	"100g-200g"},
        {"Material":	"100% cotton"},
        {"Style":	"Casual"},
    ]},
    {'id':2, 'name': 'Sweatshirt ', 'image': 'sweatshirt3.png', 'price': 8000, 'sizes': [
        {"size_id":1, "name": "S", "count": 2}, {"size_id":2, "name": "M", "count": 2}, {"size_id":3, "name": "L", "count": 2}, {"size_id":4, "name": "XL", "count": 2}, {"size_id":5, "name": "XXL", "count": 1}, 
    ],
    'info': [
        {"Peculiarity":	"Breathable, Resistant, Quick-drying, Antibacterial, Anti-static, Lightweight"},
        {"Material":	"Spandex/Polyester"},
        {"Style":	"Casual"},
        {"Quality":	"First Grade"},
    ]},
    {'id':3, 'name': 'Tote Bag', 'image': 'ToteBag.png', 'price': 5000, 'available': 7, 
     'info': [
        {"Material": "Polyester"},
        {"Size":	"30 cm < Maximum length < 50 cm"},
        {"Style":	"Minimalist, Vintage, Modern"},
        {"Type":	"Handle, foldable"}
    ]},
    {'id':4, 'name': 'Termo Bottle', 'image': 'termoBottle.png', 'price': 5000, 'available': 7,
     'info': [
        {"Peculiarity":	"Standard, Business, Portable, Temperature Display, With Cover"},
        {"Material": "Stainless steel, Metallic corpus"},
        {"Design style":	"Classical"},
        {"Thermal insulation ability":	"12-24 hours"},
        {"Capacity":	"501-600ml"},
    ]},
    {'id':5, 'name': 'Umbrella', 'image': 'samurai.png', 'price': 7000, 'available': 7, 
     'info': [
        {"Item name":"Traditional compact golf samurai sword shaped handle katana umbrella"},	
        {"Design style": "Modern"},
        {"Control":	"Semi-automatic"},
        {"Open diameter":	"<90 cm"},
        {"Material": "Polyester"},
    ]},

    {'id':6, 'name': 'Powerbank', 'image': 'PB_white.png', 'price': 6000, 'colors': [
        {"color_id":1, "name": "white", "count": 5}, {"color_id":2, "name": "black", "count": 4}
    ],
    'info': [
        {"Battery Type": "Lithium battery"},
        {"Output interface": "Micro USB, Type C, Apple interface"},
        {"Battery capacity": "2000/2200/2600mAh"},
        {"Weight": "222G"},
    ]},
]


cell_positions = [
    {'product_id': 1, 'positions': [
        {'size_id': 1, 'position': 20},
        {'size_id': 2, 'position': 25},
        {'size_id': 3, 'position': 30},
        {'size_id': 4, 'position': 30},
        {'size_id': 5, 'position': 30},
    ]},
    {'product_id': 2, 'positions': [
        {'size_id': 1, 'position': 20},
        {'size_id': 2, 'position': 25},
        {'size_id': 3, 'position': 30},
        {'size_id': 4, 'position': 30},
        {'size_id': 5, 'position': 30},
    ]},
    {
        'product_id': 3, 'positon': 45
    },
    {
        'product_id': 4, 'positon': 50
    },
    {
        'product_id': 5, 'positon': 55
    },
    {'product_id': 6, 'positions':[
        {'color_id': 1, 'position': 10},
        {'color_id': 2, 'position': 15},
    ]}
    
]