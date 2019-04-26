from django.db import models

pk_dict = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5
}


class Day(models.Model):

    name = models.CharField(max_length=9, blank=False)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        print(pk_dict[self.name.capitalize()])
        self.pk = pk_dict[self.name.capitalize()]
        super(Day, self).save(*args, **kwargs)

    @classmethod
    def load(cls, **kwargs):
        obj, created = cls.objects.get_or_create(kwargs['name'].capitalize())
        return obj
        pass

    def clean(self):
        if self.name.capitalize() not in pk_dict:
            raise ValidationError(
                "Invalid day name, should assume Monday...Friday")

    def __str__(self):
        return "{}".format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=6)
    day = models.ManyToManyField(Day, related_name='courses', through='Class')

    def __str__(self):
        return "{}".format(self.name)


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, related_name='classes',
                            on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    venue = models.CharField(blank=True, max_length=64)

    def __str__(self):
        return "Course: {} Day: {} Time: {} Venue: {}".format(
            self.course,
            self.day,
            self.time,
            self.venue
        )
