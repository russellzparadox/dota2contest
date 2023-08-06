from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Competitions(models.Model):
    name = models.CharField(unique=True, max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Teams(models.Model):
    Name = models.CharField(unique=True, max_length=30)
    members = models.ManyToManyField(CustomUser, related_name='teams_joined')
    creator = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name='team_created')
    competition = models.ForeignKey(Competitions, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    def clean(self):
        if self.members.count() > 5:
            raise ValidationError('A team can have a maximum of 5 members.')

    def remove_member(self, member):
        if member in self.members.all():
            self.members.remove(member)
            count = self.members.count()
            if self.members.count() == 0:
                self.delete()
            elif member == self.creator:
                self.creator = self.members.first()

    # def get_members(self):
    #     memberList = []
    #     for i in self.members.all()
    def save(self, *args, **kwargs):
        user = CustomUser.objects.filter(teams_joined__competition=self.competition)
        teams = Teams.objects.filter(competition=self.competition)
        if self.creator in user:
            raise ValidationError('you cannot enter one competition wit two different teams')

        # for i in teams:
        #     if self.creator in i.members:

        super().save(*args, **kwargs)

        # Access the members field and perform validation
        if self.members.count() > 4:
            raise ValidationError('A team can have a maximum of 5 members.')
