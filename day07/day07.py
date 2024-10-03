# # def display(secret_word, hp, user_input, user_word):
# #     new_user_word = ""
# #     for i in range(len(secret_word)):
# #         if secret_word[i] == user_input:
# #             new_user_word += user_input
# #         else:
# #             new_user_word += user_word[i]
# #     print(f"{new_user_word}   " + f"You have {hp} penalities")
# #     return new_user_word, hp


# # def create_word(secret_word):
# #     new_word = ""
# #     for i in secret_word:
# #         new_word += "_"
# #     return new_word

# # def game_loop(secret_word):
# #     end = False
# #     user_word = create_word(secret_word)
# #     hp = 0
# #     while not end:
# #         if user_word == secret_word:
# #             print("You won!")
# #             end = True
# #             return
# #         if hp >= 15:
# #             end = True
# #             print("You lost ^^\n")
# #             return
# #         user_input = input("Enter a letter: ")
# #         if user_input in secret_word:
# #             hp += 1
# #             user_word, hp = display(secret_word, hp, user_input, user_word)
# #         else:
# #             hp += 3
# #             display(secret_word, hp, user_input, user_word)
# #             print(f"not found, you have {hp} penalties")
# #     return

# # def hangman():
# #     secret_word = input("Give the word to guess : ")
# #     game_loop(secret_word)

# # hangman()


# # ____________________


# class Player:
#     def __init__(self,secret_word, user_input, hp, has_won=False):
#         self.hp = hp
#         self.tmp = ""
#         self.has_won = has_won
#         self.user_input = user_input
#         self.secret_word = secret_word
#         self.new_word = "-" * (len(secret_word))
#     def has_letter(self):
#         self.hp += 1
#     def has_not_letter(self):
#         self.hp += 3

# def display(player):
#     player.user_input = input("Enter a letter : ")
#     player.tmp = ""
#     found_letter = False

#     for i in range (len(player.secret_word)):
#         if player.secret_word[i] == player.user_input:
#             player.tmp += player.user_input
#             found_letter = True
#         else:
#             player.tmp += player.new_word[i]
#     if not found_letter:
#         player.has_not_letter()
#     else:
#         player.has_letter()
#     player.new_word = player.tmp
#     print(f"{player.new_word} {player.hp} penalties")

# def game_loop(player):
#     while not player.has_won:
#         display(player)

# def hangman():
#     secret_word = input("Give the word to guess : ")
#     player = Player(secret_word = secret_word ,user_input= "", hp = 0)

#     game_loop(player)

# hangman()

def cisco_type_7_decrypt(password):
    xlat = [0x64, 0x73, 0x66, 0x64, 0x3b, 0x6b, 0x66, 0x6f, 0x41, 0x2c, 0x2e, 0x69, 0x79, 0x77, 0x6b, 0x6c,
            0x75, 0x6e, 0x65, 0x6d, 0x69, 0x63, 0x73, 0x6d, 0x61, 0x77, 0x67, 0x3b, 0x7c, 0x69, 0x6f, 0x78,
            0x67, 0x63, 0x6b, 0x39, 0x74, 0x79, 0x6b, 0x64, 0x6e, 0x75, 0x6f, 0x7b, 0x66, 0x67, 0x3e, 0x4b,
            0x2c, 0x7f, 0x3e, 0x79, 0x63, 0x70, 0x64, 0x32, 0x3d, 0x63, 0x66, 0x35, 0x66, 0x6d, 0x67, 0x32,
            0x39, 0x34, 0x78, 0x67, 0x39, 0x32, 0x31, 0x35, 0x34, 0x36, 0x39, 0x34, 0x38, 0x66, 0x6f, 0x37]
    result = ""
    if password[:2].isdigit():
        s = int(password[:2])
        password = password[2:]
        for i in range(0, len(password), 2):
            result += chr(int(password[i:i+2], 16) ^ xlat[s % 53])
            s += 1
    return result

print(cisco_type_7_decrypt("144101205C3B29242A3B3C3927"))
