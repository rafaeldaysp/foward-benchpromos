from db import Database
from utils.messageFormatter import MessageFormatter
from api import bench, telegram
import time

TABLE_NAME = "PRODUCTS"
DB_FILE_NAME = "lastPriceProducts.db"

def syncDatabaseProducts(products: list, db: Database):
  dbProducts = db.fetchTable(TABLE_NAME, "productId")
  dbProductsId = [dbProduct[0] for dbProduct in dbProducts]
  for product in products:
    if product["id"] not in dbProductsId:
      db.insertIntoTable(TABLE_NAME, productId=product['id'], lastPrice=product['price'])

def updateDatabaseProduct(product: dict, db: Database):
    db.updateTable(tableName=TABLE_NAME, columns={"lastPrice": product['price']}, productId=product['id'])
  

def main():
  db = Database(dbName=DB_FILE_NAME)
  db.createTable('PRODUCTS', productId="TEXT NOT NULL", lastPrice="INT NOT NULL")
  products = bench.getProducts()
  sales = bench.getSales()
  
  syncDatabaseProducts(products, db)

  for product in products:
    if product['reference_price'] and product['price'] < product['reference_price']:
      lastPriceArray = db.conditionalFetchTable(TABLE_NAME, "lastPrice", productId=product['id'])
      lastPrice = lastPriceArray[0][0]
      if product['price'] != lastPrice:
        print(f"{product['title']}\n{lastPrice} -> {product['price']} < {product['reference_price']}")
        telegram.sendPhoto(product['image_url'], MessageFormatter(product, sales))
        updateDatabaseProduct(product, db)
        time.sleep(1)

  db.closeConnection()

if __name__ == '__main__':
  main()
