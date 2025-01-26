from django.test import TestCase
from django.urls import reverse
from games.models import Game, Character, Genre, Job
from datetime import date

class GameModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name="RPG")
        self.game = Game.objects.create(
            title="Final Fantasy VII",
            release_date=date(1997, 1, 31),
            genre=self.genre,
            description="A classic RPG game."
        )

    def test_game_creation(self):
        self.assertEqual(self.game.title, "Final Fantasy VII")
        self.assertEqual(self.game.genre.genre_name, "RPG")
        self.assertEqual(str(self.game), "Final Fantasy VII")

class CharacterModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name="RPG")
        self.game = Game.objects.create(
            title="Final Fantasy VII",
            release_date=date(1997, 1, 31),
            genre=self.genre,
            description="A classic RPG game."
        )
        self.job = Job.objects.create(
            job_name="Warrior",
            job_description="Fights on the front lines."
        )
        self.character = Character.objects.create(
            name="Cloud Strife",
            game=self.game,
            jobs=self.job,
            character_description="Main protagonist."
        )

    def test_character_creation(self):
        self.assertEqual(self.character.name, "Cloud Strife")
        self.assertEqual(self.character.game, self.game)
        self.assertEqual(self.character.jobs, self.job)
        self.assertEqual(str(self.character), "Cloud Strife")

class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name="RPG")

    def test_genre_creation(self):
        self.assertEqual(self.genre.genre_name, "RPG")
        self.assertEqual(str(self.genre), "RPG")

class JobModelTest(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            job_name="Mage",
            job_description="Uses magic attacks."
        )

    def test_job_creation(self):
        self.assertEqual(self.job.job_name, "Mage")
        self.assertEqual(str(self.job), "Mage")

class ViewsTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name="RPG")
        self.job = Job.objects.create(
            job_name="Warrior",
            job_description="Fights on the front lines."
        )
        self.game = Game.objects.create(
            title="Final Fantasy VII",
            release_date=date(1997, 1, 31),
            genre=self.genre,
            description="A classic RPG game."
        )
        self.character = Character.objects.create(
            name="Cloud Strife",
            game=self.game,
            jobs=self.job,
            character_description="Main protagonist."
        )

    def test_index_view(self):
        response = self.client.get(reverse("games:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Final Fantasy VII")

    def test_game_details_view(self):
        response = self.client.get(reverse("games:game_details", args=[self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Final Fantasy VII")
        self.assertContains(response, "A classic RPG game.")

    def test_character_list_view(self):
        response = self.client.get(reverse("games:character_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cloud Strife")

    def test_character_details_view(self):
        response = self.client.get(reverse("games:character_details", args=[self.character.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cloud Strife")
        self.assertContains(response, "Main protagonist.")

    def test_genre_list_view(self):
        response = self.client.get(reverse("games:genre_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RPG")

