import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from CreateDB import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# myFirstRestaurant = Restaurant(name="Pizza Palace")
# session.add(myFirstRestaurant)
# session.commit()
# restaurants = session.query(Restaurant).all()
# for restaurant in restaurants:
#     print(restaurant.name)