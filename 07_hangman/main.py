from collections import namedtuple
import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.
# TODO-6: - Update the code below to tell the user how many lives they have left.
# TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

# ################################################################

def update_guess_field(chosen_word, past_guess):
    result = ''
    for letter in chosen_word:
        if letter in past_guess:
            result += letter
        else:
            result += '_'
        result += ' '
    return result

def restart_game():
    result = None
    while result not in (True, False):
        restart_input = input('\nStart a new game?\nType Y (yes) or N (No)\n').strip().upper()
        if restart_input in ('Y', 'YES'): result = True
        elif restart_input in ('N', 'NO'): result = False
        else: result = None
    return result

def create_new_game(words):
    # Create game data
    Game = namedtuple('Game', ['over', 'max_lives', 'word', 'info'])
    game_over = False
    max_lives = 6
    chosen_word = random.choice(words).upper()
    game_info = None
    game = Game(game_over, max_lives, chosen_word, game_info)

    # Create player data
    Player = namedtuple('Player', ['lives', 'guess_field', 'history'])
    current_lives = max_lives
    past_guess = []
    guess_field = update_guess_field(chosen_word, past_guess)
    player = Player(current_lives, guess_field, past_guess)

    Data = namedtuple('Data', ['Game', 'Player'])
    data = Data(game, player)

    return data

def game_logic(data):
    game, player = data.Game, data.Player

    # Branch 0: lives = 0 (game over)
    if not player.lives:
        game = game._replace(over = True)
        game = game._replace(info = '\n*******    You Lose!    *******\n')

    # Branch 1: lives > 0 (game continues)
    else:
        player_input = input(f'Guess a letter: ').strip().upper()
        # Input validation
        if len(player_input) != 1:
            game = game._replace(info = '\n****    Invalid input !    ****\n')
        elif player_input in player.history:
            game = game._replace(info = f'\n**   [ {player_input} ] Already guessed, pick different letter!   **\n')
        else:
            player = player._replace(history=player.history + [player_input])
            # Branch 1-0: Wrong Guess
            if player_input not in game.word:
                game = game._replace(info = f'\n** [ {player_input} ] Your guess is wrong! **\n')
                player = player._replace(lives = player.lives - 1)
            # Branch 2-0: Correct Guess
            else:
                game = game._replace(info = '\n*** Your guess is correct ! ***\n')
                player = player._replace(guess_field = update_guess_field(game.word, player.history))
                if '_' not in player.guess_field:
                    game = game._replace(over = True)
                    game = game._replace(info = '\n*******    You Win !    *******\n')

    data = data._replace(Game = game)
    data = data._replace(Player = player)

    return data

def display(data):
    game, player = data.Game, data.Player

    if not game.info: text_header = '\n*******    HANGMAN    *******\n'
    else: text_header = game.info

    # Display updated current_lives
    display_lives = ''
    for _ in range(game.max_lives - player.lives): display_lives += '🖤'
    for _ in range(player.lives): display_lives += '❤️'

    # Display footer
    wrong_guess = []
    for letter in player.history:
        if letter not in game.word: wrong_guess.append(letter)
    wrong_guess.sort()
    wrong_guess = ','.join(wrong_guess)
    if not wrong_guess: wrong_guess = None
    if not game.over:
        text_footer = f'Wrong guess: {wrong_guess}'
    else: text_footer = f'Word was [ {game.word} ], wrong guess: {wrong_guess}'

    display_game = [rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |  
     /|\  |     {player.guess_field}
     / \  |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |
     /|\  |     {player.guess_field}
     /    |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |
     /|\  |     {player.guess_field}
          |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |
     /|   |     {player.guess_field}
          |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |
      |   |     {player.guess_field}
          |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
      O   |
          |     {player.guess_field}
          |
          |
    =========   {text_footer}
    ''', rf'''{text_header}
      +---+     {display_lives}
      |   |
          |
          |     {player.guess_field}
          |
          |
    =========   {text_footer}
    ''']

    print(display_game[player.lives])

    return data

# ################################################################

def hangman():
    # Start Message
    print(hangman_art.logo)

    # Game Loop
    start_game = restart_game()
    while start_game:
        current_game = create_new_game(hangman_words.word_list)
        display(current_game)
        while not current_game.Game.over:
            current_game = display(game_logic(current_game))
        start_game = restart_game()

    # End Message
    print('\n\nThank you for playing!\n\n')

# ################################################################

hangman()
