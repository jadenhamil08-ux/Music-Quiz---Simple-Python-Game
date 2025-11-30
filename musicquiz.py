import random

print("Welcome to the music quiz:")
user = input("Enter your username to proceed: ")
password = int(input("Enter your password to proceed: "))
score = 0
def security():
  if password == 1990:
    print("Access granted. Lets play!")
    print(" ")
  else:
    print("Access denied.")

def rules():
  print("*****************************************")
  print(" ")
  print("The rules are simple. You will be given the first letter of a song and artist.")
  print("The objective is to guess the correct song.")
  print("For every correct answer you will be awarded 3 points.")
  print("For every correct song on the second attempt you will be awarded 1 point.")
  print("When answering each question, use a capital letter for each word of the song.")
  print("Good luck and have fun!")
  print(" ")
  print("*****************************************")
  print(" ")
  input("Press enter to Start: ")
  
def generate_song():
  song1 = "Levitating"
  song2 = "Dance Monkey"
  song3 = "Blinding Lights"
  song4 = "Savage"
  song5 = "Shape of You"
  artist1 = "Dua Lipa"
  artist2 = "Tones and I"
  artist3 = "The Weeknd"
  artist4 = "Megan Thee Stallion"
  artist5 = "Ed Sheeran"
  with open("songlist.txt", "w") as f:
    f.write(song1 + ":" + artist1 + "\n")
    f.write(song2 + ":" + artist2 + "\n")
    f.write(song3 + ":" + artist3 + "\n")
    f.write(song4 + ":" + artist4 + "\n")
    f.write(song5 + ":" + artist5 + "\n")

def question_song():
  print(" ")
  print("*****************************************")
  print(" ")
  with open("songlist.txt", "r") as f:
    global songs
    global random_song
    global song_title
    global song_info
    global artist
    global first_letters
    songs = f.read().splitlines()
    random_song = random.choice(songs)
    song_info = random_song.split(": ")
    song_title = song_info[0].split(":")[0]
    artist = song_info[0].split(":")[1]
    first_letters = song_title[0]

def songcount():
  songs = ["Levitating", "Dance Monkey", "Blinding Lights", "Savage", "Shape of You"]
  while songs:  
    song_title = random.choice(songs)
    songs.remove(song_title) 

security()

rules()

songcount()

generate_song()

question_song()

question1 = input("Question 1: " + first_letters + "___ by " + artist + "\n" + "Song: ")
if question1 == song_title:
  print("Correct! Next question!")
  score =+ 3
else:
  print("Incorrect. Try one more time")
  question1 = input("Question 1: " + first_letters + "_ by " + artist + "\n" + "Song: ")
  if question1 == song_title:
    print("Correct! Next question!")
    score =+ 1
  else:
    print("Incorrect. Unlucky.")


songcount()

question2 = input("Question 2: " + first_letters + "___ by " + artist + "\n" + "Song: ")
if question2 == song_title:
  print("Correct! Next question!")
  score =+ 3
else:
  print("Incorrect. Try one more time")
  question2 = input("Question 2: " + first_letters + "_ by " + artist + "\n" + "Song: ")
  if question2 == song_title:
    print("Correct! Next question!")
    score =+ 1
  else:
    print("Incorrect. Unlucky.")

songcount()
question_song()


question3 = input("Question 3: " + first_letters + "___ by " + artist + "\n" + "Song: ")
if question3 == song_title:
  print("Correct! Next question!")
  score =+ 3
else:
  print("Incorrect. Try one more time")
  question3 = input("Question 3: " + first_letters + "_ by " + artist + "\n" + "Song: ")
  if question3 == song_title:
    print("Correct! Next question!")
    score =+ 1
  else:
    print("Incorrect. Unlucky.")

songcount()
question_song()


question4 = input("Question 4: " + first_letters + "___ by " + artist + "\n" + "Song: ")
if question4 == song_title:
  print("Correct! Next question!")
  score =+ 3
else:
  print("Incorrect. Try one more time")
  question4 = input("Question 4: " + first_letters + "_ by " + artist + "\n" + "Song: ")
  if question4 == song_title:
    print("Correct! Next question!")
    score =+ 1
  else:
    print("Incorrect. Unlucky.")

songcount()
question_song()


question5 = input("Question 5: " + first_letters + "___ by " + artist + "\n" + "Song: ")
if question5 == song_title:
  print("Correct!")
  score =+ 3
else:
  print("Incorrect. Try one more time")
  question5 = input("Question 5: " + first_letters + "_ by " + artist + "\n" + "Song: ")
  if question5 == song_title:
    print("Correct!")
    score =+ 1
  else:
    print("Incorrect. Unlucky.")

with open("score.txt", "w") as f:
  f.write("Name: " + user + "\n" + "Score: " + str(score))

print(" ")
print("*****************************************")
print(" ")
print("Thanks for playing guess the song!")
print("View the score file to see your score!")
print(" ")
print("*****************************************")