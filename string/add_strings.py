def add_digits(d1, d2, carry):
     d3 = d1 + d2 + carry
     carry = 0
     if d3 >= 10:
          carry = d3//10
          d3 %= 10
     return d3, carry

def find_sum(n1, n2): # 138, 164
     i = 1
     s = ""
     carry = 0
     while len(n1) >= i and len(n2) >= i:
          d1 = int(n1[len(n1) - i])
          d2 = int(n2[len(n2) - i])
          d3, carry = add_digits(d1, d2, carry)
          s = str(d3) + s
          # print("s is", s)
          i += 1
     while len(n1) >= i:
          d1 = int(n1[len(n1) - i])
          d2 = 0
          d3, carry = add_digits(d1, d2, carry)
          s = str(d3) + s
          i += 1
          print("s is ", s, "len[n1] is", len(n1))
     while len(n2) >= i:
          print("s is ", s, "len[n2] is", len(n2), "i is", i)
          d1 = 0
          d2 = int(n2[len(n2) - i])
          d3, carry = add_digits(d1, d2, carry)
          s = str(d3) + s
          i += 1
     if carry == 1:
          s = str(carry) + s
          
     return s

def main():
     # print(find_sum("37", '14'), "should be 51")
     # print(find_sum("87", '40'), "should be 127")
     # print(find_sum("46", '92'), "should be 138")
     print(find_sum("15", '5'), "should be 134")
     # print(find_sum("0", '0'), "should be 0")
     # print(find_sum("-1", '-1'), "should be -2")

if __name__== "__main__":
     main()