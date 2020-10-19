restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(restaurant.name)