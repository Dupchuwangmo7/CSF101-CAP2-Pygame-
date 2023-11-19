# Memory Puzzle Game Unit Tests Documentation

## Overview

Unit tests for a Python memory puzzle game built with the Pygame library are available in this repository. The unit tests that are included test a variety of aspects of the functionality of the card matching game.


## Code Structure

The main application code is organized as follows:

     - **MemoryPuzzleGame.py**: The main game script that initializes the game, handles user interactions, and manages game state.

     - **objects.py**: A module that defines the classes used in the game, including `Board`, `Button`, and others.

     - **Assets**: Directory containing images used in the game (images, background, etc.).

     - **Sounds**: Directory containing sound files used in the game.

     - **Info**: Directory containing JSON files with information about the images used in the game.



# test cases
## Test Descriptions
 TestCard

    test_card_creation: Verifies that a Card object has been properly initialized with the desired properties.
    test_card_on_click: Examines whether specific properties are updated appropriately following a simulated click event by testing a Card object's on_click method.

TestInfoCard

    test_info_card_creation: Verifies that an InfoCard object has been properly initialized with the desired properties.


TestButton

    test_button_creation: Verifies the proper initialization of a Button object.
    test_button_draw: Verifies that a Button object's draw method appropriately updates the button state.


TestMessageBox

           test_message_box: Explanation of the particular examinations conducted on the message_box function.


## Resources

    Pygame: A collection of Python modules made specifically for creating video games, the Pygame library, is used to implement the game.

    JSON: JSON files found in the Info directory are used to load information about card images.

    Sounds and Images: The game employs a variety of sounds and images to create both auditory and visual effects.

