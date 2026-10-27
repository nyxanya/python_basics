

def reverse_list(s):
    l = []
    for c in s:l.append(c)
    i = len(l) - 1
    j = 0
    vowels = "aeiouAEIOU"
    
    while j < i:
          # print("".join(l))
          # print(i, j)
          # input()
          if l[j] in vowels and l[i] in vowels:
               t = l[j]
               # print("swapping", l[i], l[j])
               l[j] = l[i] 
               l[i] = t
               i -= 1
               j += 1
          elif l[j] in vowels:
             i -= 1
          elif l[i] in vowels:
              j += 1
          else:
             j += 1 
             i -= 1    
    return "".join(l)


def main():
     print(reverse_list("Marge, let's \"went.\" I await news telegram."), "is Marge, let's \"went.\" i awaIt news telegram.")
     print(reverse_list("IceCreAm"), "is AceCreIm")

if __name__== "__main__":
     main()