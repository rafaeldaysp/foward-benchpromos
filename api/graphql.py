GET_CATEGORIES = """
    {
      categories {
        id
        name
      }
    }
  """

CREATE_PRODUCT = """
    mutation($input: CreateProductInput!) {
      createProduct(createProductInput: $input) {
        id
      }
    }
  """
  
CREATE_DEAL = """
    mutation($createDealInput: CreateDealInput!) {
      createDeal(createDealInput: $createDealInput) {
        id
      }
    }
  """

GET_RETAILERS = """
    {
      retailers {
        id
        name
      }
    }
  """
  
CREATE_PRODUCT_HISTORY = """
    mutation($createDailyStatusInput: [CreateDailyStatusInput]){
      createProductHistory(createDailyStatusInput: $createDailyStatusInput)
    }
  """
GET_PRODUCTS = """
    query ($getProductsInput: GetProductsInput) {
      products(getProductsInput: $getProductsInput) {
        products {
          id
          name
          categoryId
          slug
          imageUrl
          referencePrice
          category {
            slug
          }
          deals {
            price
            url
            availability
            totalInstallmentPrice
            installments
            retailer {
              name
            }
            coupon {
              discount
              code
              availability
            }
            cashback {
              value
              provider
              affiliatedUrl
            }
            discounts {
              id
              discount
              label
              description
            }
          }
        }
      }
    }
  """
  
REMOVE_PRODUCT = """
    mutation($removeProductId: ID!) {
      removeProduct(id: $removeProductId) {
        id
      }
    }
  """

REMOVE_ALL_PRODUCT_HISTORY = """
    mutation($productId: String!) {
      removeAllProductHistory(productId: $productId)
    }
  """
   
GET_SALES = """
    {
      sales {
        list {
          id
          productSlug
          caption
        }
      }
    }
  """
  
CREATE_SALE = """
    mutation($createSaleInput: CreateSaleInput!) {
      createSale(createSaleInput: $createSaleInput) {
        id
      }
    }
  """

REMOVE_SALE = """
    mutation($removeSaleId: ID!) {
      removeSale(id: $removeSaleId) {
        id
      }
    }
  """
GET_DEALS = """
  query ($getDealsInput: GetDealsInput) {
    deals(getDealsInput: $getDealsInput) {
      id
      url
      sku
      retailer {
        id
        name
      }
      product {
        id
        name
      }
      coupon {
        id
        code
        discount
        availability
      }
      discounts {
        id
        discount
        label
        description
      }
    }
  }
"""

GET_RETAILERS = """
  {
    retailers {
      id
      name
    }
  }
"""

GET_COUPONS = """
  query ($retailerId: ID) {
    coupons(retailerId: $retailerId) {
      code
      discount
      availability
    }
  }
"""

CREATE_COUPON = """
  mutation($createCouponInput: CreateCouponInput!) {
    createCoupon(createCouponInput: $createCouponInput) {
      id
    }
  }
"""

UPDATE_DEAL = """
  mutation($updateDealInput: UpdateDealInput!) {
    updateDeal(updateDealInput: $updateDealInput) {
      id
    }
  }
"""

GET_CASHBACKS = """
  {
    cashbacks {
      id
      url
      provider
    }
  }
"""

UPDATE_CASHBACK = """
  mutation($updateCashbackInput: UpdateCashbackInput!) {
    updateCashback(updateCashbackInput: $updateCashbackInput) {
      id
    }
  }
"""

UPDATE_COUPON = """
  mutation($updateCouponInput: UpdateCouponInput!){
    updateCoupon(updateCouponInput: $updateCouponInput) {
      id
    }
  }
"""

GET_BENCHMARKS_WITH_RESULTS = """
  query {
    benchmarks(hasResults: true) {
      id
      results {
        id
      }
    }
  }
"""

REMOVE_BENCHMARK_RESULT = """
  mutation($removeBenchmarkResultId: ID!) {
    removeBenchmarkResult(id: $removeBenchmarkResultId) {
      id
    }
  }
"""

GET_SALES_BY_PRODUCT = """
  query ($productSlug: ID) {
    sales(productSlug: $productSlug) {
      list {
        caption
      }
    }
  }
"""