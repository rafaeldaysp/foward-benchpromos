def priceCalculator(fullPrice: int = None, couponDiscountStr = None, cashbackPercent = None, discountValues = None):
  if not fullPrice:
    return 0
    
  price = fullPrice
  couponDiscount = 0
  if couponDiscountStr:
    couponDiscount = float(couponDiscountStr.split('%', 1)[0]) / 100 * fullPrice if '%' in couponDiscountStr else float(couponDiscountStr) * 100

  price = fullPrice - couponDiscount

  if discountValues:
    for discount in discountValues:
      if '%' in discount:
        price -= (float(discount.split('%', 1)[0]) / 100) * price
      else:
        price -= float(discount) * 100

  if cashbackPercent:
    price -= (price * cashbackPercent) / 100
    
  return round(price)