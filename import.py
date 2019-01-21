from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

session = DBSession()

myFirstRestaurant = Restaurant(
    name="Pizza Place"
)

cheesepizza = MenuItem(
    name="Cheese Pizza",
    description="Made with all natural ingredient  and fresh mozzarella",
    course="Entree",
    price='$8.99',
    restaurant=myFirstRestaurant
)

session = DBSession()
session.add(myFirstRestaurant)
session.add(cheesepizza)
session.commit()


session.query(Restaurant).all()
session.query(MenuItem).all()

DBSession = sessionmaker(bind=engine)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
