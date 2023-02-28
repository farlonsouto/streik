import WeekDay


class Restriction:
    """ A restriction is a workday where the pupil prefers to stay home. If it's hard, the pupil needs to stay home
        at the given day """

    def __int__(self, weekday, hard):
        self.weekday = weekday
        self.hard = hard
