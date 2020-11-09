import sys

n=int(input())
an=(int(a) for a in input().split())

if (0 > n or n > 100):
  print("error")
  sys.exit()

gcd_no=0
gcd_max=0

for k in range(max(an)):
  gcd_count=0

  if (k == 1):
    continue

  for a in an:
    print("a={}".format(a))
    if (2 > a or a > 1000):
      continue
    a_mod=a%k
    print(a_mod)
    if (a_mod == 0):
      gcd_count=gcd_count+1
      print("mod ok")
    else:
      print("mod ng")

  if (gcd_max <= gcd_count):
    gcd_max = gcd_count
    gcd_no = k

  print("gcd_max={}".format(gcd_max))
  print("gcd_no={}".format(gcd_no))

print(gcd_no)
