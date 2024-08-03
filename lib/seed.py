#!/usr/bin/env python3
from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Sample data
google = Company(name='Google', founding_year=1998)
microsoft = Company(name='Microsoft', founding_year=1975)
alice = Dev(name='Alice')
bob = Dev(name='Bob')

session.add_all([google, microsoft, alice, bob])
session.commit()

freebie1 = Freebie(item_name='T-shirt', value=20, dev=alice, company=google)
freebie2 = Freebie(item_name='Sticker', value=5, dev=alice, company=microsoft)
freebie3 = Freebie(item_name='Mug', value=10, dev=bob, company=google)

session.add_all([freebie1, freebie2, freebie3])
session.commit()
