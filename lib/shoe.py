#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size 
    
    def set_brand(self, brand):
        self._brand = brand

    def get_brand(self):
        return self._brand
    
    brand = property(get_brand, set_brand)

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size 
        else: 
            print("size must be an integer")
    def get_size(self):
        return self._size
    
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")