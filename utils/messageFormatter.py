def MessageFormatter(product: dict, sales: list):
  specsFromSale = None
  priceWithoutCashback = None
  if product['cashback']: priceWithoutCashback = 'R$ {:,.2f}'.format(product['price']/(100-product['cashback']['value'])).replace('.', '-').replace(',', '.').replace('-', ',')
  for sale in sales:
    if sale["product_id"] and sale["product_id"] == product['id']: 
      specsFromSale = '🔴' + sale["specs"].replace('🔴', '') + '🔴\n\n'
      break
  price = 'R$ {:,.2f}'.format(product['price']/100).replace('.', '-').replace(',', '.').replace('-', ',')
  finalPrice = price
  if priceWithoutCashback: finalPrice =  priceWithoutCashback + ' (Sem Cashback)\n💰 ' + price + ' (Com Cashback)'
  coupon = f'\n🎟 Cupom: {product["coupon"]["code"]}\n' if product['coupon'] else ''
  link = f'https://benchpromos.com/produto/{product["id"]}'
  cashback = f'🟢 Tem {product["cashback"]["value"]}% de Cashback usando o {product["cashback"]["name"]}, se você não utiliza, entra aqui >\
  {product["cashback"]["affiliatedLink"]} 🟢' if product['cashback'] else ''
  telegramMessage = f"🔥 {product['title']} - {price} 🔥\n\n {specsFromSale if specsFromSale else ''} {coupon}💸 {finalPrice}\n\n🔗 {link}\n\n{cashback}"

  return telegramMessage