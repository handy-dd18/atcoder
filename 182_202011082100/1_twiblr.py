import sys

arg=input()
arg_split=arg.split()
a_follower=int(arg_split[0])
b_follow=int(arg_split[1])

if (0 > a_follower or b_follow > 10000):
  print('error')
  sys.exit()

follow_max=a_follower*2+100

if (b_follow > follow_max):
  print("follow over")
  sys.exit()

add_follow=follow_max-b_follow

if (add_follow >= 0):
  print(add_follow)
else:
  print("not follow")
  sys.exit()
