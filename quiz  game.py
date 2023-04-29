print('Are you ready to play!')
start=input('Yes(or)No :').lower()
score=0
if start !='yes':
  quit()
print("let's play :)")
ans=input("which is the smallest ocean in the world? ").lower()
if ans=='arctic':
  print('correct!')
  score +=1
else:
  print('incorrect!')

ans=input("which is the oldest language in the world? ").lower()
if ans=='tamil':
  print('correct!')
  score +=1
else:
  print('incorrect!')

ans=input("brain of computer is? ").lower()
if ans=='cpu':
  print('correct!')
  score +=1
else:
  print('incorrect!')

ans=input("1024 kilobytes is equal to? ").lower()
if ans=='1 mb':
  print('correct!')
  score +=1
else:
  print('incorrect!')
print('your score: '+str(score))
print('your percentage :'+str((score/4)*100)+'%')