import sqlalchemy
from src import database as db
import itertools


def gen_potion_types(x: int):
  """
  Generates all combinations of potion types with increments of x.
  Only works for factors of 100.
  """
  each_ml = []
  each_ml = [i for i in range(0, 101, x)]
  combinations = list(itertools.product(each_ml, repeat=4))
  potion_types = [list(i) for i in combinations if sum(i) == 100]
  return potion_types


#TODO based on # ml in each
def calc_price(potion_type: tuple):
  return 50


#TODO update prices on table without resetting other values
def update_prices():
  return


def create_potion_inventory():
  """"""
  with db.engine.begin() as connection:
    connection.execute(sqlalchemy.text("""
        CREATE SEQUENCE id START 1;
        CREATE TABLE potion_inventory (
          sku text DEFAULT 'potion_' || nextval('id')::text PRIMARY KEY,
          potion_type int[],
          num_potion int,
          price int)
        """))
    potion_types = gen_potion_types(25)
    for potion_type in potion_types:
      price = calc_price(potion_type)
      connection.execute(sqlalchemy.text("""
          INSERT INTO potion_inventory (potion_type, num_potion, price)
          VALUES (:potion_type, 0, :price)
          """), {"potion_type": potion_type, "price": price})


def delete_table(table: str):
  with db.engine.begin() as connection:
    connection.execute(sqlalchemy.text(f"DROP TABLE {table}"))


def create_carts():
  """"""
  with db.engine.begin() as connection:
    connection.execute(sqlalchemy.text("""
        CREATE TABLE carts (
          cart_id SERIAL PRIMARY KEY,
          customer text,
          items_id int REFERENCES cart_items(items_id),
          payment text
        )"""))


def create_cart_items():
  """"""
  with db.engine.begin() as connection:
    connection.execute(sqlalchemy.text("""
        CREATE TABLE cart_items (
          items_id SERIAL PRIMARY KEY,
          sku text REFERENCES ,
          quantity int
        )"""))