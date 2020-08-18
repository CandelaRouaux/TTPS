info = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
code, amount = map(int, input().split())
print("Total: R$","{:.2f}".format(info[code]*amount))