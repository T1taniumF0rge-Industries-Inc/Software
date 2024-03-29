import random, time
print('Guess a number from 1-100!')
num = random.randint(1,100)
guess = ''
i = 0
while guess != num:
  i += 1
  guess = int(input('Please input a number between 1-100: '))
  if guess == num:
    print('Congrats! You guessed correct!')
  elif guess < num:
    print('Your number was too small...')
  else:
    print('Your number was too big...')
print('You guessed in total%d' %i + 'times', end = '')
print("Quick! Go compare your score with your friends'!")
time.sleep(3)
