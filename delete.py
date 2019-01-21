from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


"""
steps to delete using sqlalchemy
1. Find entry
    example: session.query(MenuItem).filter_by(xxx = 'xxx')
    add  above to a variable
2. session.delete(entry)
3. session.commit()

"""


spinach = session.query(MenuItem).filter_by(name="Spinach Ice Cream")

# for spinach in spinach:
#     print(spinach.restaurant.name)
#     print(spinach.id)
#     print(spinach.description)

session(spinach).delete(synchronize_session=False)
session.commit()
Base.metadata.bind = engine
