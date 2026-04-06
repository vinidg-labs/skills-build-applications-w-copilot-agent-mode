from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpa os dados existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Cria usuários
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)


        # Cria atividades
        Activity.objects.create(user_id=str(tony.id), user_name=tony.name, type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user_id=str(steve.id), user_name=steve.name, type='bike', duration=45, date='2024-01-02')
        Activity.objects.create(user_id=str(clark.id), user_name=clark.name, type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user_id=str(bruce.id), user_name=bruce.name, type='yoga', duration=20, date='2024-01-04')

        # Cria treinos
        Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 3 sets of 20 situps', suggested_for='dc')

        # Cria leaderboard
        Leaderboard.objects.create(user_id=str(tony.id), user_name=tony.name, points=120, rank=1)
        Leaderboard.objects.create(user_id=str(steve.id), user_name=steve.name, points=110, rank=2)
        Leaderboard.objects.create(user_id=str(clark.id), user_name=clark.name, points=100, rank=3)
        Leaderboard.objects.create(user_id=str(bruce.id), user_name=bruce.name, points=90, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populado com dados de teste!'))
