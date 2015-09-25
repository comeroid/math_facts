import random
#if name=="__main__":

def main():
  print "welcome to math facts!"
  print "do you want to do:"
  print "a)ddition or s)ubtraction"
  print "m)ultiplication or d)ivision"
  choice = raw_input()   
  num_questions = 2
  counter_answers = 0
  for i in range(num_questions): 
    multiplicand = random.randint(1,12)
    multiplier = random.randint(1,12)
    product = multiplicand * multiplier
    print "{} * {} = ?".format(multiplicand,multiplier)
    answer = input()
    if answer== product:
      print "correct!" 
      counter_answers = counter_answers + 1
    else:
        print "incorrect!"
  print "congratulations you got %d/%d  correct" % (counter_answers,num_questions)

main()










































