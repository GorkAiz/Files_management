num_array = []
with open('num.txt', 'r') as rfile:
  with open('numend.txt','w') as wfile:
    # f_content = f.readlines()
    #print(f_content)
    #pass
    for line in rfile:
      num_array.append(int(line))
    
    print(num_array)  

    for x in num_array:
      num_array[x] = num_array[x] + 1      
    print(num_array)
    
    for wline in num_array:  
      wfile.write(str(wline) + '\n')
