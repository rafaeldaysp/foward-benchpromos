from db import Database
from utils.messageFormatter import MessageFormatter
from api import benchpromos, telegram
import time

from utils.priceCalculattor import priceCalculator

TABLE_NAME = "PRODUCTS"
DB_FILE_NAME = "lastPriceProducts.db"

def syncDatabaseProducts(products: list, db: Database):
  dbProducts = db.fetchTable(TABLE_NAME, "productId")
  dbProductsId = [dbProduct[0] for dbProduct in dbProducts]
  for product in products:
    if not product['deals']:
      continue
    deal = product['deals'][0]
    if product["id"] not in dbProductsId:
      db.insertIntoTable(TABLE_NAME, productId=product['id'], lastPrice=priceCalculator(deal['price'], deal['coupon']['discount'] if deal['coupon'] and deal['coupon']['availability'] else None, deal['cashback']['value'] if deal['cashback'] else None), lastAvailable=1 if deal['availability'] else 0)

def updateDatabaseProduct(product: dict, db: Database):
  deal = product['deals'][0]
  db.updateTable(tableName=TABLE_NAME, columns={"lastPrice": priceCalculator(deal['price'], deal['coupon']['discount'] if deal['coupon'] and deal['coupon']['availability'] else None, deal['cashback']['value'] if deal['cashback'] else None), "lastAvailable": 1}, productId=product['id'])
  

def main():
  db = Database(dbName=DB_FILE_NAME)
  db.createTable(TABLE_NAME, productId="TEXT NOT NULL", lastPrice="INT NOT NULL", lastAvailable="BOOLEAN")
  products = benchpromos.Bench().get_products({
    'getProductsInput': {
      'hasDeals': True
    }
  })
  sales = benchpromos.Bench().get_sales()
  
  syncDatabaseProducts(products, db)

  for product in products:
    deal = product['deals'][0]
    dealPrice = priceCalculator(deal['price'], deal['coupon']['discount'] if deal['coupon'] and deal['coupon']['availability'] else None, deal['cashback']['value'] if deal['cashback'] else None)
    if product['referencePrice'] and dealPrice < product['referencePrice'] and deal['availability']:
      lastState = db.conditionalFetchTable(TABLE_NAME, "lastPrice", "lastAvailable", productId=product['id'])
      lastPrice = lastState[0][0]
      lastAvailable = lastState[0][1]
      if abs(dealPrice - lastPrice) > 1000 or lastAvailable == False:
        print(f"{product['name']}\n{lastPrice} -> {dealPrice} < {product['referencePrice']}")
        
        telegram.sendPhoto(product['imageUrl'], MessageFormatter(product, sales), product['id'])
        updateDatabaseProduct(product, db)
        time.sleep(2)

  db.closeConnection()

if __name__ == '__main__':
  main()
