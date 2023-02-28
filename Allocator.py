from functools import cmp_to_key

from Family import Family
from WeekDay import WeekDay


class Allocator:
    """ Encapsulates the intelligence of allocating a list of Families in a working week taking into considerations
    the size of each family: Larger families (more restrictions and/or more kids) are allocated first """

    @classmethod
    def allocate(cls, families, available_places, weekly_spots) -> dict:
        """ Implements the harmonic series sum up to the limit (number of terms) given as input and prints the terms of
        the sum.
            Args:
                families: a list of families.
                available_places: number of available places each day
                weekly_spots: number of days in the week each family has a place offered
            Returns:
                A dictionary associating each WeekDay to a list of Pupil """

        allocation = {
            WeekDay.Mon: [],
            WeekDay.Tue: [],
            WeekDay.Wed: [],
            WeekDay.Thu: [],
            WeekDay.Fri: [],
        }

        allocation_days = allocation.keys()

        # sorted originally from smaller to larger, reversed for convenience
        sorted_families = sorted(families, key=cmp_to_key(Family.compare)).reverse()

        # tries the best-fit approach
        for family in sorted_families:
            family_restriction_days = list()
            for restriction in family.restrictions:
                family_restriction_days.append(restriction.weekday)
            for i in range(weekly_spots):
                day_to_occupy = allocation_days[i]
                if (day_to_occupy not in family_restriction_days) \
                        and (len(allocation.get(day_to_occupy)) < available_places) \
                        and (family.kids not in allocation.get(day_to_occupy)):
                    allocation.get(day_to_occupy).append(family.kids)
                    # sorts the weekdays from the less occupied to the more occupied
                    allocation = sorted(allocation.keys(), key=lambda x: len(allocation.get(x)))

        return allocation
