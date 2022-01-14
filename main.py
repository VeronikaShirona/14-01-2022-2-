teksts = input("ievadit ciparu: ")
def deleteE(teksts):
  if teksts.count("e")>0:
    teksts = teksts.replace("e"," ")
    teksts = teksts.upper()
    print(teksts)
  else:
    teksts = "TEKSTS NESATUR VAJADZĪGO BURTU."
    print(teksts)
  return teksts
deleteE(teksts)