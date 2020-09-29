import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Collins = User(first_name = "Ruth",
                                last_name = "Jomo",
                                username = "ruthjomo",
                                password = "2603@ruth",
                                email = "ruthjomo@gmail.com")
        self.new_post = Post(post_title = "Test Title",
                            post_content = " I love blogging!",
                            user_id = self.user_George.id)
        self.new_comment = Comment(comment = "Nice one!",
                                    post_id = self.new_post.id,
                                    user_id = self.user_George.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Ruth, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))