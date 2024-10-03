
import pygame
import sys
import random
pygame.init()

# Words list
word_list = ['PYTHON', 'PROGRAMMING', 'HANGMAN', 'DEVELOPER', 'GAMES']
word = random.choice(word_list)
guessed_letters = []
all_letters = []
wrong_attempts = ''
max_attempts = 6

font = pygame.font.Font(None, 74)
mid_font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# Hangman drawing positions
head = [400, 150, 50, 50]
body = [400, 200, 400, 300]
left_arm = [400, 250, 350, 220]
right_arm = [400, 250, 450, 220]
left_leg = [400, 300, 350, 370]
right_leg = [400, 300, 450, 370]

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

window_width = 800
window_height = 600
window_size = (window_width, window_height)

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Stickman in Pygame Window')

background_color = (255, 255, 255)  # White
stickman_color = (0, 0, 0)  # Black

def display_hangman(wrong_attempts):
    if wrong_attempts > 0:
        pygame.draw.circle(screen, stickman_color,(head[0], head[1]),head[2] // 1 , 2)  # (surface, color, center, radius, width)
    if wrong_attempts > 1:
        pygame.draw.line(screen, stickman_color, (body[0], body[1]), (body[2], body[3]), 2)  # (surface, color, start_pos, end_pos, width)
    if wrong_attempts > 2:
        pygame.draw.line(screen, stickman_color, (left_arm[0], left_arm[1]), (left_arm[2], left_arm[3]), 2)  # Left arm
    if wrong_attempts > 3:
        pygame.draw.line(screen, stickman_color, (right_arm[0], right_arm[1]), (right_arm[2], right_arm[3]), 2)  # Right arm
    if wrong_attempts > 4:
        pygame.draw.line(screen, stickman_color, (left_leg[0], left_leg[1]), (left_leg[2], left_leg[3]), 2)  # Left leg
    if wrong_attempts > 5:
        pygame.draw.line(screen, stickman_color, (right_leg[0], right_leg[1]), (right_leg[2], right_leg[3]), 2)  # Right leg

def loose_display(wrong_attempts):
    display_loose = 'Haha you loose in ' + str(wrong_attempts) + ' attempts !'
    loose_text = small_font.render(display_loose, True, black)
    screen.blit(loose_text, (50, 50))

def win_display():
    display_win = 'Congratulations! You won!'
    win_text = small_font.render(display_win, True, black)
    screen.blit(win_text, (50, 50))

def display_txt(wrong_attempts):
    display_word = ''
    display_score = 'current score is : ' + str(wrong_attempts)

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
        text = font.render(display_word, True, black)
        screen.blit(text, (150, 400))

    score_text = mid_font.render(display_score, True, black)
    screen.blit(score_text, (150, 500))

def display_window(wrong_attempts):
    screen.fill(white)
    display_txt(wrong_attempts)
    display_hangman(wrong_attempts)

def is_letter_in_word(letter):
    if word.count(letter) == 0:
        return 1
    return 0

def letter_analysis(wrong_attempts,event):
    if event.unicode.isalpha():
        letter = event.unicode.upper()
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            wrong_attempts += is_letter_in_word(letter)
    return wrong_attempts

def event_manager(wrong_attempts,event,running):
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        wrong_attempts = letter_analysis(wrong_attempts,event)
    return wrong_attempts, running

def event_handler(wrong_attempts, running):
    for event in pygame.event.get():
        wrong_attempts, running = event_manager(wrong_attempts,event, running)
    return wrong_attempts, running

def end_manager(wrong_attempts):
    if wrong_attempts >= max_attempts:
        loose_display(wrong_attempts)
        pygame.display.flip()
        pygame.time.wait(2000)
        return False
    if all(letter in guessed_letters for letter in word):
        win_display()
        pygame.display.flip()
        pygame.time.wait(2000)
        return False
    return True

def game_loop():
    running = True
    wrong_attempts = 0

    while running:
            running = end_manager(wrong_attempts)
            wrong_attempts, running = event_handler(wrong_attempts,running)
            display_window(wrong_attempts)
            pygame.display.flip()
    pygame.quit()
    sys.exit()
game_loop()