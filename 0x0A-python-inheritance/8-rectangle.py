#!/usr/bin/python3
'''Module that creates a new class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    '''Subclass of BaseGeometry'''
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
        super().area(width, height)
        self.__height = height
        
