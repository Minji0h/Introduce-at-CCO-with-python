m = int(input("Digite a altura:"))
n = int(input("Digite a largura"))
i = 1
while(i <= n):
    j = 1
    while(j <= m):
        if(j == 1 or j == m):
            print(end="#")
        elif(i == 1 or i == n):
            print(end = "#")
        else:
            print(end = " ")
        j = j + 1
    print()
    i = i + 1
