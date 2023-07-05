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
      db.insertIntoTable(TABLE_NAME, productId=product['id'], lastPrice=product['price'], lastAvailable=1 if product['available'] else 0)

def updateDatabaseProduct(product: dict, db: Database):
    db.updateTable(tableName=TABLE_NAME, columns={"lastPrice": product['price'], "lastAvailable": 1}, productId=product['id'])
  

def main():
  db = Database(dbName=DB_FILE_NAME)
  db.createTable(TABLE_NAME, productId="TEXT NOT NULL", lastPrice="INT NOT NULL", lastAvailable="BOOLEAN")
  products = bench.getProducts()
  sales = bench.getSales()
  
  syncDatabaseProducts(products, db)

  for product in products:
    if product['reference_price'] and product['price'] < product['reference_price'] and product['available']:
      lastState = db.conditionalFetchTable(TABLE_NAME, "lastPrice", "lastAvailable", productId=product['id'])
      lastPrice = lastState[0][0]
      lastAvailable = lastState[0][1]
      if abs(product['price'] - lastPrice) > 1000 or lastAvailable == False:
        print(f"{product['title']}\n{lastPrice} -> {product['price']} < {product['reference_price']}")
        
        telegram.sendPhoto(product['image_url'], MessageFormatter(product, sales), product['id'])
        updateDatabaseProduct(product, db)
        time.sleep(1)

  db.closeConnection()

if __name__ == '__main__':
  main()
