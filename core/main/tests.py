from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Artist
import os


TEXT_SAMPLE_LONG_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ornare malesuada
eros. Mauris nec lacus vulputate, maximus sapien et, lacinia turpis.
In hendrerit nibh ac eros consequat, at cursus ipsum tincidunt.
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
Pellentesque porta faucibus venenatis. Fusce urna massa, lacinia nec ex id, placerat condimentum lacus.
Nullam hendrerit ipsum ac nisi volutpat, nec tincidunt turpis scelerisque.
Nulla sit amet volutpat eros.
Integer at est sagittis, iaculis nulla eget, convallis tellus.
Phasellus facilisis, nulla et tempus interdum, lacus quam lobortis purus, eu congue leo mauris vitae urna.
Duis porttitor efficitur metus et suscipit. Suspendisse mattis elit id hendrerit imperdiet.

Integer vehicula porttitor quam. Vestibulum venenatis sem sit amet odio consectetur lacinia.
Vestibulum et scelerisque mauris. Nam ultrices sagittis eros, sed suscipit massa tristique eget.
Phasellus non commodo dui. Nam enim libero, placerat euismod metus ut, scelerisque vehicula sem.
Donec consectetur erat id metus rhoncus blandit. Maecenas ultrices libero a pharetra ullamcorper.
Pellentesque blandit libero luctus, faucibus turpis non, tempor enim. Aenean mauris magna, efficitur vitae egestas eget, auctor congue lacus.
Nulla nec justo eu lacus faucibus semper. Suspendisse sollicitudin, lectus eget faucibus rhoncus, nulla libero mollis tellus, in finibus mauris ipsum consequat nibh.
Quisque fermentum velit sapien, ut congue metus laoreet facilisis. Aliquam mattis diam quis eros porta, a rutrum quam imperdiet. Etiam ornare ipsum eu erat semper mollis.

Sed at nibh fringilla, porttitor tortor nec, mattis urna.
Vestibulum enim nibh, tempor ut tortor vel, lacinia ultricies leo.
In at lectus sollicitudin, eleifend massa id, aliquet augue.
Curabitur ipsum nunc, bibendum ut hendrerit quis, vehicula dignissim nibh.
Suspendisse hendrerit sed purus a imperdiet.
Donec vel convallis nisl. Morbi magna augue, volutpat nec vehicula vel, auctor a risus.
"""

class TestArtistModel(TestCase):
    """Test Artist Model"""


    def test_creating_instance(self):
        """Test creating valid and invalid instance"""
        artist1 = Artist.objects.create(
            id=1,
            name = 'Chilli Crew',
            desription = TEXT_SAMPLE_LONG_TEXT,
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
            desription = TEXT_SAMPLE_LONG_TEXT,
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
        self.assertEqual(artist2.name, 'Pikes') # test valid data
        self.assertEqual(artist1.year, 2018) # test valid type
        self.assertEqual(artist2.year, 2017) # test valid type
        self.assertEqual(str(artist1), 'Chilli Crew') #string representacion
        self.assertEqual(str(artist2), 'Pikes') #string representacion
        self.assertEqual(str(type(artist1.thumbnail)), "<class 'django.db.models.fields.files.ImageFieldFile'>") # test image type
        self.assertEqual(str(type(artist2.thumbnail)), "<class 'django.db.models.fields.files.ImageFieldFile'>") # test image type
        self.assertEqual(artist1.thumbnail.path, f'/app/core/artist_thumbnail/Chilli_Crew_thumbnail.jpg') # test valid new file name

        artist1.delete()
        artist2.delete()
        artists = Artist.objects.all()
        self.assertEqual(len(artists), 0) # test delete instance
        self.assertFalse(os.path.isfile('/app/core/artist_thumbnail/Chilli_Crew_thumbnail.jpg'))
