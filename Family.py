class Family:
    """ Abstracts the concept of a family who has kids at the kindergarten. The family that may or may not have any
    restriction regarding the days it prefers and/or needs to stay home """

    def __init__(self, name, kids, restrictions):
        self.name = name
        self.kids = kids
        self.restrictions = restrictions

    def compare(self, other) -> int:
        """ Compares the current instance of Family with the other Family received as argument.
        1. Families with hard restrictions are greater than
        2. Families with any restriction, which, by their turn, are greater than
          2.1 Pupils with more restrictions , which, by their turn, are greater than
          2.2 Pupils with less restrictions
        3. Families with no restriction at all.
        Finally, whenever two families are equal, the family with more kids is greater."""

        my_num_restrictions = len(self.restrictions)
        their_num_restrictions = len(other.restrictions)

        # Any has no restrictions at all?
        if my_num_restrictions == 0:
            return -1  # less restrictions, less priority
        else:
            if their_num_restrictions == 0:
                return 1

        # Is any of the restrictions a hard one? Who has more?
        my_hard_restr = [m for m in self.restrictions if m.hard is True]
        their_hard_restr = [t for t in other.restrictions if t.hard is True]
        if len(my_hard_restr) > 0 or len(their_hard_restr) > 0:
            if len(my_hard_restr) > len(their_hard_restr):
                return 1  # more hard restrictions, more priority
            else:
                if len(their_hard_restr) > len(my_hard_restr):
                    return -1

        # Who has more restrictions?
        if my_num_restrictions > their_num_restrictions:
            return 1  # more restrictions, more priority
        else:
            if my_num_restrictions < their_num_restrictions:
                return -1

        # With the same number of restrictions, families with more kids are greater
        if len(self.kids) > len(other.kids):
            return 1
        else:
            if len(other.kids) > len(self.kids):
                return -1

        # Both families have the same number of restrictions and the same number of kids
        return 0
