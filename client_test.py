import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
      #test 'getDataPoint' function with normal quotes
      quotes = [
          {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
              'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
            'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], 
                                                quote['top_bid']['price'], 
                                                quote['top_ask']['price'], 
                                                (quote['top_ask']['price'] + quote['top_bid']['price']) / 2)
                        )
          

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
       #test 'getDataPoint' function when the bid price is greater than the ask price
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
          self.assertEqual(getDataPoint(quote), (quote['stock'], 
                                                  quote['top_bid']['price'], 
                                                  quote['top_ask']['price'], 
                                                  (quote['top_ask']['price'] + quote['top_bid']['price']) / 2)
                          )

    def test_getRatio_calculate(self):
      #test 'getRatio' function with dummy data
      self.assertEqual(getRatio(1, 2), 0.5)
    
    
    def test_getRatio_handleInvalidInput(self):
      #test 'getRatio' function when division by zero would occur
      self.assertIsNone(getRatio(1, 0))
      

if __name__ == '__main__':
    unittest.main()
