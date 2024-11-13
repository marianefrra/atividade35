#lendo 10 números reais e armazenando na lista

nums = []
for i in range (10):
    num = float(input(f"digite o número { i + 1}: "))
    nums.append(num)

#exibindo os números na ordem inversa
 
print("números na ordem inversa: ")
for num in reversed(nums):
    print(num)
    