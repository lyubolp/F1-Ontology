from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")


class Person(Thing):
    namespace = onto

if __name__ == '__main__':
    print("Hello world")