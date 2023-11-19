import unittest
import pygame
from objects import Board, Card, InfoCard, Button, message_box 

class TestCard(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_card_creation(self):
        image = pygame.Surface((45, 45))
        card = Card(1, (0, 0), image, (0, 0))

        # the part Checks if the card is initialized correctly
        self.assertEqual(card.value, 1)
        self.assertEqual(card.index, (0, 0))
        self.assertEqual(card.image, image)
        self.assertEqual(card.pos, (0, 0))
        self.assertTrue(card.is_alive)
        self.assertFalse(card.visible)
        self.assertFalse(card.animate)
        self.assertTrue(card.slide_left)
        self.assertFalse(card.animation_complete)
        self.assertEqual(card.rect.x, 0)
        self.assertEqual(card.rect.y, 0)
        self.assertEqual(card.cover_x, 45)

    def test_card_on_click(self):
        image = pygame.Surface((45, 45))
        card = Card(1, (0, 0), image, (0, 0))

        # Simulate an on_click event
        card.on_click(pygame.Surface((100, 100)), speed=5)

        # Checking if the card state is updated correctly
        self.assertFalse(card.animation_complete)
        self.assertFalse(card.visible)
        self.assertTrue(card.slide_left)

class TestInfoCard(unittest.TestCase):
    def test_info_card_creation(self):
        image = pygame.Surface((45, 45))
        info_card = InfoCard(1, (0, 0), image, (0, 0))

        # Checking if the info card is initialized correctly
        self.assertEqual(info_card.value, 1)
        self.assertEqual(info_card.index, (0, 0))
        self.assertEqual(info_card.image, image)
        self.assertEqual(info_card.pos, (0, 0))
        self.assertEqual(info_card.rect.x, 0)
        self.assertEqual(info_card.rect.y, 0)

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_button_creation(self):
        image = pygame.Surface((50, 50))
        button = Button(image, (50, 50), 0, 0)

        # Checking if the button is initialized correctly
        self.assertEqual(button.rect.x, 0)
        self.assertEqual(button.rect.y, 0)
        self.assertFalse(button.clicked)

    def test_button_draw(self):
        image = pygame.Surface((50, 50))
        button = Button(image, (50, 50), 0, 0)

        # Simulate a draw event
        action = button.draw(pygame.Surface((100, 100)))

        # Checking if the button state is updated correctly
        self.assertFalse(button.clicked)
        self.assertFalse(action)

class TestMessageBox(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_message_box(self):
        font = pygame.font.Font(None, 36)
        window = pygame.Surface((640, 520))

        # Simulate a message box event
        message_box(window, font, "Test", "This is a test message.")

        # Checking if the message box is drawn correctly
        

if __name__ == '__main__':
    unittest.main()
