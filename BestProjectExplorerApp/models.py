#from django.db import models
from django.contrib.gis.db import models


INDICATORS_TYPES = ['OUTPUT', 'OUTCOME']
INDICATORS_CATEGORIES = ['DONORS', 'ORG']
INDICATORS_UNITS = ['Number', '%']

SSG = 'SSG'
SG = 'SG'
MG = 'MG'
GRANT_TYPE = (
  (SSG, 'Swift Small Grant'),
  (SG, 'Small Grant'),
  (MG, 'Medium Grant'),
)

CR = 'CR'
IAS = 'IAS'
HR = 'HR'
SC = 'SC'
MAIN_SUBJECT = (
  (CR,'Coral Restoration'),
  (IAS,'IAS Control'),
  (HR, 'Habitat Restoration'),
  (SC, 'Species Conservation'),
)


# Create your models here.
class Project(models.Model):
    best_code = models.CharField(max_length=4, default='0000')
    grant_type = models.CharField(max_length=255, choices=GRANT_TYPE)
    name = models.CharField(max_length=255)
    organisations = models.CharField(max_length=255, null=True, blank=True)
    territory = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_subject = models.CharField(max_length=255, choices=MAIN_SUBJECT)
    total_budget = models.IntegerField(null=True, blank=True)
    geom = models.PointField()

    def __str__(self):
        return self.name
#
#     def __unicode__(self):
#         return '%s %s %s' % (self.name, self.geom.x, self.geom.y)
#
#     def __getattr__(self, attrname):
#         if attrname == 'name' and self._name_dirty:
#             raise ('You should get a clean copy or save this object.')
#
#         return super(Project, self).__getattr__(attrname)
#
#     def __setattr__(self, attrname, val):
#         setter_func = 'setter_' + attrname
#         if attrname in self.__dict__ and callable(getattr(self, setter_func, None)):
#             super(Project, self).__setattr__(attrname, getattr(self, setter_func)(val))
#         else:
#             super(Project, self).__setattr__(attrname, val)
#
# #TODO se former à la notion de décorations pythons
#     @property
#     def setter_lon(val):
#         return val.upper()


class Site(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    created_on_date = models.DateField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    geom = models.PolygonField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geom.x, self.geom.y)


class Waypoint(models.Model):
    name = models.CharField(max_length=32)
    geom = models.PointField()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geom.x, self.geom.y)


class MainOutcome(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class SpecificOutcome(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Output(models.Model):

    name = models.CharField(max_length=32)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='outputs')

    def __str__(self):
        return '(' + self.project.best_code + ')' + '-' + self.name


class Indicator(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=10, default=INDICATORS_TYPES[0])
    category = models.CharField(max_length=10, default=INDICATORS_CATEGORIES[0])
    unit = models.CharField(max_length=10, default=INDICATORS_UNITS[0])
    target = models.IntegerField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    output = models.ForeignKey(Output, on_delete=models.CASCADE, related_name='activities')

    name = models.CharField(max_length=32)
    target = models.IntegerField(null=True, blank=True)
    unit = models.CharField(max_length=255,null=True, blank=True)
    monthly_report = models.CharField(max_length=255, null=True, blank=True, default='0,0,0,0,0,0,0,0,0,0,0,0')

    def __str__(self):
        return self.name


class ActivityPlanned(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    date_planned = models.DateField(blank=True)
    date_achieved = models.DateField(blank=True)
    nb_planned = models.IntegerField(blank=True)
    nb_achieved = models.IntegerField(blank=True)

    def __str__(self):
        return "%s %s" % (self.date_planned, self.activity.name)


class GanttTask(models.Model):
    name = models.CharField(max_length=32)
    start_date = models.DateField()
    duration = models.DurationField()
    progress = models.IntegerField()

    def __str__(self):
        return self.name


