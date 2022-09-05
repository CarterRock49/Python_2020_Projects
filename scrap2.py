def HalfList(listt, con):
  x = int()
  for x in range(0, len(listt)):
    if listt[x] == con:
      return "TRUE"
    elif listt[x] != con and len(listt) == x:
      return "FALSE"
    
    
    
def main():
  listt = ["P", "a", "s", "s", "&", "W", "o", "r", "d"]
  con = [""]
  HalfList(listt, con)



main()