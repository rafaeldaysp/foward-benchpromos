import requests
from dotenv import load_dotenv
import os

from api.graphql import *

load_dotenv()

class Bench:
  API_URL, API_KEY = (os.getenv('API_URL'), os.getenv('API_KEY'))
  
  def __init__(self) -> None:
    
    self.headers = {'api-key': self.API_KEY}
    
    pass
  
  def run_query(self, query: str, variables = None):

    res = requests.post(self.API_URL, json={'query': query, 'variables': variables}, headers=self.headers)
    
    if res.status_code != 200 or 'errors' in res.json():
      raise Exception("Query failed to run by returning code of {}. {}. Variables?: {}. \n\nResponse: {}".format(res.status_code, query, variables, res.json()))
  
    return res.json()['data']
  
  def get_categories(self) -> list:

    res = self.run_query(GET_CATEGORIES)
    data = res['categories']
    
    return data
  
  def get_retailers(self) -> list:
    
    res = self.run_query(GET_RETAILERS)
    data = res['retailers']
    
    return data
  
  def get_products(self, variables = None):
    res = self.run_query(GET_PRODUCTS, variables)
    
    data = res['products']['products']
    
    return data
  
  def get_sales_by_product(self, productSlug: str):
    variables = {
      'productSlug': productSlug
    }
    res = self.run_query(GET_SALES_BY_PRODUCT, variables)
    
    data = res['sales']['list']
    
    return data
  
  def remove_product(self, product_id):
    variables = {
      'removeProductId': product_id
    }
    
    self.run_query(REMOVE_PRODUCT, variables)
  
  def create_product(self, name: str, image_url: str, category_id: str, reference_price: int = None, review_url: str = None, specs: dict = None) -> dict:
    
    variables = {
      "input": {
        "categoryId": category_id,
        "imageUrl": image_url,
        "name": name,
        "referencePrice": reference_price,
        "reviewUrl": review_url,
        "specs": specs
      } 
    }
    print(variables)
    res = self.run_query(CREATE_PRODUCT, variables)
    data = res['createProduct']
    
    return data

  def create_deal(self, availability, price, product_id, retailer_id, url, sku = None):

    variables = {
        "createDealInput": {
          "availability": availability,
          "price": price,
          "productId": product_id,
          "retailerId": retailer_id,
          "url": url,
          "sku": sku
        }
    }
    
    res = self.run_query(CREATE_DEAL, variables)
    data = res['createDeal']
    
    return data 
  
  def create_history(self, array):
    self.run_query(CREATE_PRODUCT_HISTORY, variables={'createDailyStatusInput': array})
  
  
  def remove_all_product_history(self, product):
    variables = {
      'productId': product['id']
    }
    res = self.run_query(REMOVE_ALL_PRODUCT_HISTORY, variables)
    return
  
  def create_sale(self, category_id, image_url, price, title, url, caption = None, cashback_id = None, coupon = None, created_at = None, highlight = None, installments = None, label = None, product_slug = None, review = None, total_installment_price = None):
    variables = {
      "createSaleInput": {
        "categoryId": category_id,
        "price": price,
        "imageUrl": image_url,
        "title": title,
        "url": url,
        "caption": caption,
        "cashbackId": cashback_id,
        "coupon": coupon,
        "createdAt": created_at,
        "highlight": highlight,
        "installments": installments,
        "label": label,
        "productSlug": product_slug,
        "review": review,
        "totalInstallmentPrice": total_installment_price
      }
    }
    
    
    res = self.run_query(CREATE_SALE, variables)
    print(res)
    return
  
  def remove_sale(self, sale):
    variables = {
      "removeSaleId": sale['id']
    }
    self.run_query(REMOVE_SALE, variables)
    
    return
  
  def get_sales(self):
    res = self.run_query(GET_SALES)
    data = res['sales']['list']
    
    return data

  def get_deals(self, variables = {}):
    variables = {
      "getDealsInput": variables
    }
    
    res = self.run_query(GET_DEALS, variables)
    data = res['deals']
    
    return data
  
  def get_retailers(self):
    res = self.run_query(GET_RETAILERS)
    data = res['retailers']
    
    return data
  
  def get_coupons(self, retailer_id):
    variables = {
      'retailerId': retailer_id
    }
    
    res = self.run_query(GET_COUPONS, variables)
    data = res['coupons']

    return data
  
  def create_coupon(self, code, discount, retailer_id):
    variables = {
      "createCouponInput": {
        "code": code,
        "discount": discount,
        "retailerId": retailer_id,
        "availability": True
      }
    }
    
    res = self.run_query(CREATE_COUPON, variables)
    data = res['createCoupon']
    
    return data

  def update_deal(self, update_deal_input):
    variables = {
      'updateDealInput': update_deal_input
    }
    
    self.run_query(UPDATE_DEAL, variables)
    
    return

  def get_cashbacks(self):
    res = self.run_query(GET_CASHBACKS)
    data = res['cashbacks']
    
    return data

  def update_cashback(self, update_cashback_input):
    variables = {
      'updateCashbackInput': update_cashback_input
    }
    
    self.run_query(UPDATE_CASHBACK, variables)
    
    return 
  
  def update_coupon(self, update_coupon_input):
    variables = {
      'updateCouponInput': update_coupon_input
    }
    
    self.run_query(UPDATE_COUPON, variables)
    
    return 
  
  def get_benchmarks_with_results(self):
    
    res = self.run_query(GET_BENCHMARKS_WITH_RESULTS)
    data = res['benchmarks']
    
    return data

  def remove_benchmark_result(self, remove_benchmark_result_id):
    
    variables = {
      'removeBenchmarkResultId': remove_benchmark_result_id
    }
    
    self.run_query(REMOVE_BENCHMARK_RESULT, variables)
    
    return
  
if __name__ == '__main__':
  bench = Bench()

  # print(bench.get_categories())
  # print(bench.get_deals({"retailerId": "clnaedifz000bo80nmuc6tu6p"}))
  print(bench.get_retailers())
  # bench.create_product('produto teste', 'https://cdn.myanimelist.net/r/200x268/images/characters/6/473767.jpg?s=9a8f58b1cad9e51dbcb4d8b0cd9f8186', 'cln96knjv0000my0nk1xnwizj')
    
