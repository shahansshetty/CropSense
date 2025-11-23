import sqlite3

conn = sqlite3.connect("crop.db")
c = conn.cursor()

# Creating crop table using .execute() function 
c.execute(
    """ CREATE TABLE crop(
          crop_name text,
          picture blob,
          info text,
          link text
          )
          """
)

#
crop_data = [
    (
        "maize",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/ZeaMays.jpg/330px-ZeaMays.jpg",
        "Maize, also known as corn, is a cereal grain first domesticated by indigenous peoples in southern Mexico about 9,000 years ago. Today, it is one of the most widely grown crops in the world, used for human consumption, livestock feed, and industrial products such as biofuels. Maize thrives in warm climates and is highly productive under good agronomic conditions.",
        "https://en.wikipedia.org/wiki/Maize",
    ),
    (
        "chickpea",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Chickpeas_Plant.jpg/500px-Chickpeas_Plant.jpg",
        "Chickpea, also known as gram or Bengal gram, is a protein-rich legume widely consumed across South Asia, the Middle East, and the Mediterranean. It is valued for its nutritional content, drought tolerance, and soil-enriching ability through nitrogen fixation. Chickpeas are used in various forms, including whole grains, flour, and culinary dishes like hummus.",
        "https://en.wikipedia.org/wiki/Chickpea",
    ),
    (
        "kidneybeans",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Red_Rajma_BNC.jpg/500px-Red_Rajma_BNC.jpg",
        "Kidney beans are a popular variety of the common bean known for their distinct kidney shape and rich protein content. They are widely cultivated in tropical and subtropical regions and are used in dishes like chili, curries, and salads. Proper cooking is essential, as raw or undercooked kidney beans contain naturally occurring toxins.",
        "https://en.wikipedia.org/wiki/Kidney_bean",
    ),
    (
        "pigeonpeas",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Cajanus_cajan_Blanco1.167-cropped.jpg/330px-Cajanus_cajan_Blanco1.167-cropped.jpg",
        "Pigeon pea is a hardy legume widely grown in tropical and subtropical regions. Known for its ability to tolerate drought and improve soil fertility through nitrogen fixation, it forms an important protein source in South Asian and African diets. It is commonly used in dal, curries, and soups.",
        "https://en.wikipedia.org/wiki/Pigeon_pea",
    ),
    (
        "mothbeans",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Matki.JPG/375px-Matki.JPG",
        "Moth bean is a drought-resistant legume cultivated primarily in arid and semi-arid regions of India. The plant thrives in sandy soils and extremely dry climates. Its seeds and sprouts are rich in protein and minerals, making it a valuable food source in dryland agriculture.",
        "https://en.wikipedia.org/wiki/Moth_bean",
    ),
    (
        "mungbean",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Mung_bean_%28Vigna_radiata%29_Dired_open_Pod_in_Hong_Kong.JPG/500px-Mung_bean_%28Vigna_radiata%29_Dired_open_Pod_in_Hong_Kong.JPG",
        "Mung bean is a fast-growing legume widely consumed in Asia. Known for its versatility, it is eaten whole, sprouted, or as flour. Mung beans are highly nutritious, rich in protein, vitamins, and fiber, and they grow well in warm climates with moderate rainfall.",
        "https://en.wikipedia.org/wiki/Mung_bean",
    ),
    (
        "blackgram",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Black_gram.jpg/500px-Black_gram.jpg",
        "Black gram, also known as urad dal, is an important pulse crop extensively grown in South Asia. It has high protein content and is a key ingredient in Indian dishes like idli, dosa, and dal makhani. The plant enhances soil fertility through nitrogen fixation and grows well in warm climates.",
        "https://en.wikipedia.org/wiki/Black_gram",
    ),
    (
        "lentil",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/3_types_of_lentil.png/500px-3_types_of_lentil.png",
        "Lentil is a nutrient-dense legume cultivated for its edible seeds. It is one of the oldest domesticated crops and plays a major role in vegetarian diets due to its high protein, fiber, and mineral content. Lentils grow well in cool, dry climates and are relatively easy to cultivate.",
        "https://en.wikipedia.org/wiki/Lentil",
    ),
    (
        "pomegranate",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Pomegranate_Juice_%282019%29.jpg/500px-Pomegranate_Juice_%282019%29.jpg",
        "Pomegranate is a fruit-bearing shrub known for its juicy, antioxidant-rich arils. Originally native to the Middle East and South Asia, it is now grown in many dry, warm regions worldwide. The fruit is valued for its health benefits and used in juices, salads, desserts, and traditional medicine.",
        "https://en.wikipedia.org/wiki/Pomegranate",
    ),
    (
        "banana",
        "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
        "Banana is a tropical fruit crop grown across humid regions of the world. It is one of the most widely consumed fruits due to its soft texture, high energy value, and year-round availability. Bananas grow on large herbaceous plants and are a major export commodity for many tropical countries.",
        "https://en.wikipedia.org/wiki/Banana",
    ),
    (
        "mango",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Mangos_-_single_and_halved.jpg/960px-Mangos_-_single_and_halved.jpg",
        "Mango, often called the 'king of fruits', is a tropical stone fruit native to South Asia. It is known for its sweet flavor, vibrant color, and rich aroma. Mangoes are packed with vitamins A and C and are widely cultivated in tropical and subtropical regions.",
        "https://en.wikipedia.org/wiki/Mango",
    ),
    (
        "grapes",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Grapes%2C_Rostov-on-Don%2C_Russia.jpg/500px-Grapes%2C_Rostov-on-Don%2C_Russia.jpg",
        "Grapes are small, juicy berries grown in clusters on woody vines. They are widely cultivated for fresh consumption, wine production, raisins, and juices. Grapes thrive in temperate climates and are valued for their antioxidants and natural sugars.",
        "https://en.wikipedia.org/wiki/Grape",
    ),
    (
        "watermelon",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg/500px-Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg",
        "Watermelon is a refreshing fruit composed mostly of water and natural sugars. Native to Africa, it is now cultivated in warm climates worldwide. Its sweet red flesh is rich in vitamins A and C, and the plant thrives in sandy, well-drained soils with abundant sunlight.",
        "https://en.wikipedia.org/wiki/Watermelon",
    ),
    (
        "muskmelon",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Muskmelon.jpg/500px-Muskmelon.jpg",
        "Muskmelon, which includes varieties such as cantaloupe, is a sweet, aromatic fruit grown in warm, dry regions. It is rich in vitamins A and C and has high water content. Muskmelons grow best in sandy soils with good drainage and long warm seasons.",
        "https://en.wikipedia.org/wiki/Cucumis_melo",
    ),
    (
        "apple",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/95apple.jpeg/500px-95apple.jpeg",
        "Apple is a temperate fruit cultivated across cool and mid-latitude regions. It is one of the most widely consumed fruits globally and comes in numerous varieties with different flavors and textures. Apples are rich in fiber and antioxidants and form a major global fruit market.",
        "https://en.wikipedia.org/wiki/Apple",
    ),
    (
        "orange",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Oranges_-_whole-halved-segment.jpg/960px-Oranges_-_whole-halved-segment.jpg",
        "Orange is a citrus fruit valued for its sweet-tart flavor and high vitamin C content. It is grown extensively in tropical and subtropical climates. Oranges are consumed fresh, as juice, and used in various culinary and cosmetic products.",
        "https://en.wikipedia.org/wiki/Orange_(fruit)",
    ),
    (
        "papaya",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Papaya_-_longitudinal_section.jpg/960px-Papaya_-_longitudinal_section.jpg",
        "Papaya is a tropical fruit crop known for its sweet orange flesh and digestive enzyme papain. It grows rapidly in warm climates and bears fruit year-round. Papaya is rich in vitamins A and C and widely consumed fresh or in salads and beverages.",
        "https://en.wikipedia.org/wiki/Papaya",
    ),
    (
        "coconut",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Coconut_4.jpg/500px-Coconut_4.jpg",
        "Coconut is a versatile tropical crop grown primarily along coastal regions. It provides food, water, oil, fiber, and timber. Every part of the tree has economic value, making it known as the 'tree of life' in many cultures. Coconut palms require warm climates and sandy soils.",
        "https://en.wikipedia.org/wiki/Coconut",
    ),
    (
        "cotton",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/CottonPlant.JPG/330px-CottonPlant.JPG",
        "Cotton is a major fiber crop used worldwide for textile production. It grows well in warm climates with moderate rainfall. The crop has high economic significance and is used not only for fabric but also for cottonseed oil, animal feed, and industrial products.",
        "https://en.wikipedia.org/wiki/Cotton",
    ),
    (
        "jute",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jute_Field_Bangladesh_%287749587518%29.jpg/500px-Jute_Field_Bangladesh_%287749587518%29.jpg",
        "Jute is a long, soft, and shiny bast fiber extracted from plants of the genus Corchorus. It is the second most important natural fiber after cotton and is used for making sacks, ropes, carpets, and eco-friendly textiles. Jute grows well in warm, humid climates with fertile alluvial soil.",
        "https://en.wikipedia.org/wiki/Jute",
    ),
    (
        "coffee",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Coffee_beans_unroasted.jpg/500px-Coffee_beans_unroasted.jpg",
        "Coffee is a tropical plantation crop known for its seeds, which are processed to produce one of the world’s most consumed beverages. It is primarily grown in high-altitude regions of Africa, Asia, and Latin America. Coffee beans vary in flavor depending on the variety, climate, and processing methods.",
        "https://en.wikipedia.org/wiki/Coffee",
    ),
]

# Inserting list of tuples into the database "crop.db"

c.executemany(
    """ 
            INSERT INTO crop VALUES(?,?,?,?)
""",
    crop_data,
)

print("pushed to db")

conn.commit()
conn.close()
