from django.db import models

charFieldLength = 20


class Room(models.Model):
    building: str = models.CharField(max_length=charFieldLength, default='ABC')
    number: str = models.CharField(max_length=charFieldLength, default='1000')

    def __str__(self): return self.building + ' ' + str(self.number)


class Block(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self): return str(self.start_time)[:-3] + '-' + str(self.end_time)[:-3]


class Session(models.Model):
    day: int = models.CharField(max_length=3, default='M', choices=(
        ('Mon', 'Monday'),('Tue', 'Tuesday'),('Wed', 'Wednesday'),('Thu', 'Thursday'),('Fri', 'Friday'),('Sat', 'Saturday'),('Sun', 'Sunday'),))
    block = models.ForeignKey(Block, on_delete=models.DO_NOTHING, null=True)

    def __str__(self): return str(self.day) + '@' + str(self.block)


class Class(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING, null=True)
    class Meta:
        verbose_name_plural = "classes"

    def __str__(self): return str(self.room) + '-' + str(self.session)


class Course(models.Model):
    name: str = models.CharField(max_length=40, default='Introduction to Django')
    idName: str = models.CharField(max_length=charFieldLength, default='HELP-123')
    description: str = models.TextField(blank=True)
    serial: int = models.CharField(max_length=charFieldLength, blank=True)
    credits: int = models.IntegerField(default=3)
    coreqs = models.ManyToManyField('self', blank=True)
    prereqs = models.ManyToManyField('self', blank=True)
    sameAs = models.ManyToManyField('self', blank=True)
    countsAs = models.ManyToManyField('self', blank=True)

    def __str__(self): return self.idName


class Section(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)
    classes = models.ManyToManyField(Class)
    serial: str = models.IntegerField(default=1, blank=True, null=True)
    year: int = models.IntegerField(default=2018)
    semester: int = models.IntegerField(default=1)
    status: int = models.IntegerField(default=1) #0=Open, 1=Closed
    currentlyEnrolled: int = models.IntegerField(default=0)
    maxStudents: int = models.IntegerField(default=20, blank=True)
    cost: float = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        concl = str(self.course) + ' ['
        for I in self.classes.all():
            concl += str(I) + '; '
        return concl[:-2] + ']'