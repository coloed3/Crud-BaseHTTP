from database_setup import Base, 
Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

# the below will query all of the datase by name
veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')


# print(veggieBurgers)

# this query will allow us to grab the information we want with 1 name
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=2).one()
# UrbanVeggieBurger.price = '2.99'
# session.add(UrbanVeggieBurger)
# session.commit()


# modifing prices to all veggie veggieBurgers
# for veggieBurger in veggieBurgers:
#     if veggieBurger.price != '2.99':
#         veggieBurger.price = '2.99'
#         session.add(veggieBurger)
#         session.commit()
#
#
# for veggieBurgers in veggieBurgers:
#     print(veggieBurgers.id)
#     print(veggieBurgers.price)
#     print(veggieBurgers.restaurant.name)
#     print("\n")


Base.metadata.bind = engine
