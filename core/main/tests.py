from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Artist
import os


class TestArtistModel(TestCase):
    """Test Artist Model"""


    def test_creating_instance(self):
        """Test creating valid and invalid instance"""
        artist1 = Artist.objects.create(
            id=1,
            name = 'Chilli Crew',
            desription = """Integer vehicula porttitor quam. Vestibulum venenatis sem sit amet odio consectetur lacinia.
            Vestibulum et scelerisque mauris. Nam ultrices sagittis eros, sed suscipit massa tristique eget.""",
            year = 2018,
            thumbnail = SimpleUploadedFile(name='test_image.jpg', content=open('/app/core/main/test.jpg', 'rb').read(), content_type='image/jpeg'),
            logo = SimpleUploadedFile(name='test_image2.jpg', content=open('/app/core/main/test.jpg', 'rb').read(), content_type='image/jpeg'),
            facebook = 'www.facebook.com/chillicrew',
            spotify = 'www.spofity.com/chillicrew',
            youtube = 'www.yt.com/chillcrew',
            instagram = 'www.instagram.com/chillicrew',
            mail = 'office@chillicrew.com',
            phone = '+48777888999'
        )

        artist2 = Artist.objects.create(
            id=2,
            name = 'Pikes',
            desription = """Integer vehicula porttitor quam. Vestibulum venenatis sem sit amet odio consectetur lacinia.
            Vestibulum et scelerisque mauris. Nam ultrices sagittis eros, sed suscipit massa tristique eget.""",
            year = 2017,
            thumbnail = SimpleUploadedFile(name='test_image.jpg', content=open('/app/core/main/test.jpg', 'rb').read(), content_type='image/jpeg'),
            logo = SimpleUploadedFile(name='test_image2.jpg', content=open('/app/core/main/test.jpg', 'rb').read(), content_type='image/jpeg'),
            facebook = 'www.facebook.com/pikes',
            spotify = 'www.spofity.com/pikes',
            youtube = 'www.yt.com/pikes',
            instagram = 'www.instagram.com/pikes',
            mail = 'office@pikes.com',
            phone = '+48777888999'
        )
        artist3 = {}
        artists = Artist.objects.all()

        self.assertIn(artist1, artists) # test created artist1
        self.assertIn(artist2, artists) # test created artist2
        self.assertNotIn(artist3, artists) # test that artist3 is not Artist instance
        self.assertEqual(len(artists), 2) # test created 2 instance
        self.assertEqual(artist1.name, 'Chilli Crew') # test valid data
        self.assertEqual(artist1.year, 2018) # test valid type
        self.assertEqual(str(artist1), 'Chilli Crew') #string representacion
        self.assertEqual(str(type(artist1.thumbnail)), "<class 'django.db.models.fields.files.ImageFieldFile'>") # test image type
        self.assertEqual(artist1.thumbnail.path, f'/app/core/artist_thumbnail/Chilli_Crew_thumbnail.jpg') # test valid new file name

        artist1.delete()
        artist2.delete()
        artists = Artist.objects.all()
        self.assertEqual(len(artists), 0) # test delete instance
        self.assertFalse(os.path.isfile('/app/core/artist_thumbnail/Chilli_Crew_thumbnail.jpg')) # test deleting instance images when will deleting instance
