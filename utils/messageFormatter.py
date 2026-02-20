from utils.priceCalculattor import priceCalculator

def MessageFormatter(product: dict, sales: list):
  deal = product['deals'][0]
  dealPrice = priceCalculator(deal['price'], deal['coupon']['discount'] if deal['coupon'] and deal['coupon']['availability'] else None, deal['cashback']['value'] if deal['cashback'] else None)
  dealInstallmentPrice = priceCalculator(deal['totalInstallmentPrice'], deal['coupon']['discount'] if deal['coupon'] and deal['coupon']['availability'] else None, deal['cashback']['value'] if deal['cashback'] else None) if deal['totalInstallmentPrice'] else None
  dealInstallments = deal['installments']
  specsFromSale = None
  for sale in sales:
    if sale["productSlug"] and sale["productSlug"] == product['slug'] and sale['caption']: 
      specsFromSale = '🔴 ' + sale["caption"].replace('🔴', '').strip() + ' 🔴\n\n'
      break
  price = 'R$ {:,.2f}'.format(dealPrice/100).replace('.', '-').replace(',', '.').replace('-', ',')
  dealInstallmentPrice = 'R$ {:,.2f}'.format(dealInstallmentPrice/100).replace('.', '-').replace(',', '.').replace('-', ',') if dealInstallmentPrice else None
  coupon = f'🎟 Cupom: `{deal["coupon"]["code"]}`\n' if deal['coupon'] and deal['coupon']['availability'] else ''
  priceField = price
  if dealInstallments and dealInstallments > 1: priceField =  price + f' (À Vista{" Com Cupom" if coupon else ""})\n💰 ' + dealInstallmentPrice + f' (Parcelado em até {dealInstallments}x)'
  link = f'https://benchpromos.com/{product["category"]["slug"]}/{product["slug"]}'
  cashback = f'🟢 Tem {deal["cashback"]["value"]}% de Cashback usando {deal["cashback"]["provider"]}, se você não utiliza, entra aqui >\
  {deal["cashback"]["affiliatedUrl"]} 🟢' if deal['cashback'] else ''
  telegramMessage = f"🔥 {product['name']} - {price} #anúncio🔥\n\n{specsFromSale if specsFromSale else ''} {coupon}💸 {priceField}\n\n🔗 {link}\n\n{cashback}"

  return telegramMessage