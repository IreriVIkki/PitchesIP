import unittest
from app import models
from app import db

User = models.User
Comment = models.Comment
Pitch = models.Pitch


class Test(unittest.TestCase):

    def setUp(self):
        self.new_user = User(name='Victor', email='mimi@gmail.com',
                             bio='Who cares about this', photo='sdfasd.jpg', password='smimi')
        self.new_pitch = Pitch(title='Pitch Test', content='this is the pitch content', rating=8,
                               likes=23, dislikes=0, time='10:22', category_id='News', author=self.new_user)
        self.new_comment = Comment(content='this is a comment for the project', time='10:25',
                                   rating=5, likes=234, dislikes=2, author=self.new_user, pitch=self.new_pitch)

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()

    def test_instance_pitch(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_instance_user(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_instance_comment(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'Pitch Test')
        self.assertEquals(self.new_pitch.content, 'this is the pitch content')
        self.assertEquals(self.new_pitch.likes, 23)

    def test_save_pitch(self):
        self.new_pitch.save_pitch(self.new_pitch)
        self.assertTrue(len(Pitch.query.all()) > 0)


if __name__ == '__main__':
    unittest.main()
