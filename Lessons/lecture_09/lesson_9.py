# class
# class Page:   # class
#     def __init__(self, name):
#                  # , url, xpath, driver):
#         self.name = name
#         # self.url = url
#         # self.xpath = xpath
#         # self.driver = driver
#         print('ID of object {}:'.format(id(self)))
#     def print_name(self):
#         return f'My name is {self.name}'
#
#    #
#
#     # def click(self):
#     #     self.driver.click(self.xpath)
#
# a =  Page('Rymma')    # class object
# b = Page('Alex')
#
# # print(a)
# print(a.__str__())
# print(a.print_name())
# print('ID of object a {}:'.format(id(a)))
# print(b)
# print(b.print_name())
# print('ID of object b {}:'.format(id(b)))

print('\n' * 2)

class Page:
    """
    This is a doc string of a class
    """
    counter = 0
    def __init__(self, name):
        self.name = name
        Page.counter += 1
        # print('ID of object {}' .format(id(self)))

    def get_name(self):
        """
        Function returns name of the object
        :return: name of the object"""
        return f'My name is {self.name}'

    def __del__(self):
        del self
        Page.counter -= 1


   def get_counter():
        print(Page.counter)



    # get_counter = staticmethod(get_counter)
Page.get_counter()
a = Page('main')
Page.get_counter()



# print('Page class objects counter {}' .format(Page.counter.__str__()))
# a = Page('Rymma')
# print(Page.get_name(self=a))
# print('Page class objects counter {}' .format(Page.counter.__str__()))
# b = Page('Alex')
# print('Page class objects counter {}' .format(Page.counter.__str__()))
# print(a)
# print(a.get_name())
# print('ID of object a {}' .format(id(a)))
# print(b)
# print(b.get_name())
# print("ID of object b {} " .format(id(b)))
#
# print(Page.__doc__)
# print(a.__doc__)
# print(a.get_name().__doc__)
# del b
# print('Page class objects counter {}' .format(Page.counter.__str__()))


print('\n' * 2)

# inheritance

class Page:
    """
    This is a doc string of a class
    """
    counter = 0

    def __init__(self, name):
        self.name = name
        Page.counter += 1
        # print('ID of object {}' .format(id(self)))

    def get_name(self):
        """
        Function returns name of the object
        :return: name of the object"""
        return f'My name is {self.name}'

    def __del__(self):
        del self
        Page.counter -= 1


def get_counter():
    print(Page.counter)


# get_counter = staticmethod(get_counter)
Page.get_counter()
a = Page('main')
Page.get_counter()


class MainPage(Page):
    def __int__(self, name, url):
        Page.__init__(self, name)
        self.url = url

    def get_url(self):
        return f'The page url is {self.url}'

a = MainPage('MainPage', 'https://')
print(a.get_name())
print(a.get_url())
