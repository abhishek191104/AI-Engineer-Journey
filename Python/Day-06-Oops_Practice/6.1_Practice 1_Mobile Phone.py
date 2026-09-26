class mobile:

  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def display(self):
    print("\nBrand: ", self.brand)
    print("Model: ", self.model)
    print("Price: ", self.price)

mobile1 = mobile("Poco", "M4 pro", 15000)
mobile2 = mobile("Vivo", "V20", 14000)

mobile1.display()
mobile2.display()