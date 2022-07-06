import numpy as np
import sys

def gen4mers():
  bases=['a','c','g','t']
  i=j=k=m=0
  kmers=[]
  for m in range(0,4):
    for k in range(0,4):
      for j in range(0,4):
        for i in range(0,4):
          b=bases[m]+bases[k]+bases[j]+bases[i]
          kmers.append(b)
  return kmers

def readFile(file_path):
  file1 = open(file_path, 'r') 
  Lines = file1.readlines() 
  seqs=[]
  names=[]
  i=0
  first=True;
  fasta=""
  for line in Lines: 
    line=line.split('\n')[0]
    if (line.startswith(">")):
      line=line.split('>')[1]
      names.append(line)
      if first:
        first=False
      else:
        seqs.append(fasta)
        fasta=''
    else:
      fasta+=line.lower()
      #seqs.append(line.lower())
      #if i>10:
        #break
      #i+=1
  seqs.append(fasta) #to take the last sequence
  return names,seqs

def readMapping(file_path):
  file1 = open(file_path, 'r') 
  Lines = file1.readlines() 
  seq_class={}
  i=0
  for line in Lines: 
    line=line.split('\n')[0]
    if (line.startswith("RH")):
      name=line.split()[0]
      tax_id=line.split()[2]
      seq_class[name]=tax_id
      #if i>10:
        #break
      #i+=1
  return seq_class

if __name__ == "__main__":
  #seqs=['aaaaaaatttt','actgtaaggactg','aaatttctgtgt','ttttacttttccttttc']
  names,seqs=readFile(sys.argv[1])
  seq_class=readMapping(sys.argv[2])
  kmers=gen4mers()
  n=0
  for items in seqs:
    if(names[n] in seq_class):
      print(names[n],end=',')
      ct=np.zeros(256)
      i=0
      for km in kmers:
        for j in range (len(items)-(3)):
          k=j+4
          if km in items[j:k]:
            ct[i]+=1
        print(int(ct[i]),end=',')
        i+=1
      print(seq_class[names[n]])
    #else:
      #print(names[n],'ERROR')
    n+=1
