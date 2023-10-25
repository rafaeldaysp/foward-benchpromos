def priceCalculator(fullPrice: int, couponDiscountStr: str | None = None, cashbackPercent: int | None = None):
  couponDiscount = 0
  if(couponDiscountStr):
    couponDiscount = float(couponDiscountStr.split('%', 1)[0]) / 100 * fullPrice if '%' in couponDiscountStr else float(couponDiscountStr.replace('.', '').replace(',', '.'))/100
  
  cashbackDiscount = 0
  if (cashbackPercent):
    cashbackDiscount = (fullPrice - couponDiscount) * cashbackPercent / 100
    
  return round(fullPrice - couponDiscount - cashbackDiscount)