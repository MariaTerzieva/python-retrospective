class Person:
    instances = list()

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.father = father
        self.mother = mother
        self.instances.append(self)

    def get_siblings(self, gender):
        def we_have_common_parent(my, your):
            return (my.father is your.father and my.father is not None or
                    my.mother is your.mother and my.mother is not None)

        siblings_list = list()

        for instance in self.instances:
            if (we_have_common_parent(self, instance) and
                    instance.gender == gender and instance is not self):
                siblings_list.append(instance)

        return siblings_list

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def children(self, gender=None):
        def gender_filter(my_list, gender):
            return filter(lambda instance: instance.gender == gender,
                          my_list)

        children_list = list()

        for instance in self.instances:
            if instance.father is self or instance.mother is self:
                children_list.append(instance)

        if gender is not None:
            return list(gender_filter(children_list, gender))
        else:
            return children_list

    def is_direct_successor(self, person):
        return (person.mother is self or person.father is self)
