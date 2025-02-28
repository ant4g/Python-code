a = float(input("Ile opakowań o pojemnści jednego lub mniej litra oddałeś?"))
k_a = a * 0.1
b = float(input("Ile opakowań o pojemności większej niż jeden litr oddałeś?"))
k_b = b * 0.25
k_c = k_a + k_b
print("Cała kwota, którą otrzymasz za wszystkie butelki wynosi: %.2f."% k_c, "$")
