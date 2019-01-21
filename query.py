from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


myFirstRestaurant = Restaurant(name="pizza Palace")


cheesepizza = MenuItem(
    name="Cheese Pizza",
    description="Made with all natural ingredient  and fresh mozzarella",
    course="Entree",
    price='$8.99',
    restaurant=myFirstRestaurant
)

# session.add(cheesepizza)
# session.add(myFirstRestaurant)
# session.commit()
firstResult = session.query(Restaurant).first()
Menuquery = session.query(MenuItem)

items = session.query(MenuItem).all()

for item in items:
    print(item.name)
    print(item.name + " " + item.description + " " + item.price)

Base.metadata.bind = engine
