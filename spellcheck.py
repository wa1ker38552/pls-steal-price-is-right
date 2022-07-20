words = open('items.txt','r').read().split('\n')

def check(init):
  odd = []
  word_amount = {}
  score = {}

  if init in words:
    return init
  else:
    for a in words:
      odd.clear()
      word_amount.clear()
      points, c = 0, 0
      
      if len(a) == len(init): points += 25
      if a[0] == init[0]: points += 25
      else: points -= 50
      for i in range(len(init)):
        try:
          if a[i] == init[i]: points += (1/len(init))*100
          else: odd.append(init[i])
        except: c += 1
      try:
        if c == 1:
          if init.replace(odd[0],'') == a: points += 100
      except: pass
      points -= c*((1/len(init))*50)
      for i in a:
        if i in word_amount: word_amount[i] += 1
        else: word_amount[i] = 1
      c = 0
      for i in init:
        if i in word_amount: c += 1
      if c == len(init) and len(init) == len(a) and init != a: points += 50
      for i in init:
        try:
          if i in a: points += (1/len(init))*75
        except: pass
      score[a] = points
      
    value = max(score.values())
    return list(score)[list(score.values()).index(value)]
