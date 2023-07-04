# Abstract class
import abc
from abc import ABC, abstractmethod


class HTTP():
    @abc.abstractmethod
    def put(self):
        return

    @staticmethod
    @abstractmethod
    def my_abstract_static_method():
        pass

    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls):
        return

    @property
    @abstractmethod
    def my_property(self):
        return

    @my_property.setter
    @abstractmethod
    def my_property(self, value):
        return

    @my_property.getter
    @abstractmethod
    def my_property(self):
        return

    @abstractmethod
    def _get_x(self):
        return self.x

    @abstractmethod
    def _set_x(self, value):
        self.x = value

    x = property(_get_x, _set_x)


class NewHTTP(HTTP):
    def __init__(self):
        self.property = "my property"

    def put(self):
        return "I`m a put method"

    @property

    def my_property(self):
        return self.property

    @my_property.setter
    def my_property(self, value):
        if not isinstance(value, str):
            raise "The value is not a string"
        self.property = value

    def _get_x(self):
        return x

    def _set_x(self, value):
        return

    def my_abstract_classmethod(self):
        return

    def my_abstract_static_method(self):
        return

    def x(self):
        return self.x


# http = HTTP()
# print(http.put())

new_http = NewHTTP()
print(new_http.put())
# print(new_http.get())

new_http = NewHTTP()
print(new_http.put())
print(new_http.my_property)
new_http.my_property = 'new property value'
#new_http.my_property = 10 # Exception
print(new_http.my_property)
print(new_http.x())
print(new_http)

new_http.x()

print(new_http.my_abstract_classmethod())

print(new_http.my_abstract_static_method())