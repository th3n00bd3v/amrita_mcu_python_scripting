# make the most simple class possible


class SimpleClass:
    pass


# create an instance of your SimpleClass and print it out

simple_instance = SimpleClass()
print(simple_instance)


# now add some functionality to your simple class

class LessSimpleClass:
    # add one class attribute
    
    class_attribute = "I am a class attribute"

    # add a class method

    @classmethod
    def class_method(cls):
        return f"This is a class method. Accessing: {cls.class_attribute}"
    
less_simple_instance = LessSimpleClass()

# print out your class attribute both from an instance of the class and through the class directly
print("Access via class:", LessSimpleClass.class_attribute)
print("Access via instance:", less_simple_instance.class_attribute)

# run the method - both directly from the class and through an instance.
print("Class method via class:", LessSimpleClass.class_method())
print("Class method via instance:", less_simple_instance.class_method())