with open("article.txt", "r") as f:
   lines = f.read()
   words = lines.split()
   print(len(words))
   print(words)