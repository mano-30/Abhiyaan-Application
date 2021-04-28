def swap(numarr):
  
  n = len(numarr)  
  moves = 0  
  for i in range(n):
         
    for j in range(0,n-i-1):
  
      if numarr[j]>numarr[j+1]:
  
        temp = numarr[j]
        numarr[j] = numarr[j+1]
        numarr[j+1] = temp
        moves = moves + 1
      
      
  print(numarr)
  print("No of moves = %d"%moves)

if __name__ == "__main__":

   input_list = [int(num) for num in input("Enter Input : ").split()]
   swap(input_list)
