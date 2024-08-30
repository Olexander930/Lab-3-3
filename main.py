s=input(str("Введіть речення: "))
words=s.split()
min_word=min(map(len,words))
print("Довжина найкоротшого слова: ", min_word)