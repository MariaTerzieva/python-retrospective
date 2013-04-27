class Person:
    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.parents = (mother, father)
        self.kids = []

        for parent in self.parents:
            if parent is not None:
                parent.__add_child(self)

    def __add_child(self, child):
        return self.kids.append(child)

    def __get_siblings(self, gender):
        siblings_plus_self = set([person for parent in self.parents
                                  for person in parent.children(gender)])
        return list(siblings_plus_self - {self})

    def get_brothers(self):
        return self.__get_siblings('M')

    def get_sisters(self):
        return self.__get_siblings('F')

    def children(self, gender=None):
        if gender is not None:
            return [kid for kid in self.kids if kid.gender == gender]
        else:
            return self.kids

    def is_direct_successor(self, person):
        return self in person.parents
