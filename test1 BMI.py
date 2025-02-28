def calculator_BMI_M():
    weight = float(input("Wprowadź swoją wagę( podaj ją w kilogramach ): "))
    height = float(input("Podaj swój wzrost( podaj go w metrach !!): "))
    BMI = weight / (height)**2
    if BMI < 18.5:
        print("Masz niedowagę!!! Udaj się do lekarza, lub sprawdź poprawność wprowadzonych danych.")
        return BMI
    elif BMI> 18.5 and BMI < 25:
        print("Twoja waga jest w normie:)")
        return BMI
    elif BMI > 25 and BMI < 30:
        print("Masz nadwagę. Sugeruję trochę ćwiczeń")
        return BMI
    elif BMI > 30:
        print("Masz otyłość!!! Udaj się do lekarza, lub sprawdź poprawność wprowadzonych danych.")
        return BMI

def calculator_BMI_K():
    weight = float(input("Wprowadź swoją wagę( podaj ją w kilogramach ): "))
    height = float(input("Podaj swój wzrost( podaj go w metrach !!): "))
    BMI = weight / (height)**2
    if BMI < 18.5:
        print("Masz niedowagę!!! Udaj się do lekarza, lub sprawdź poprawność wprowadzonych danych.")
        return BMI
    elif BMI> 18.5 and BMI < 25:
        print("Twoja waga jest w normie:)")
        return BMI
    elif BMI > 25 and BMI < 30:
        print("Masz nadwagę. Sugeruję trochę ćwiczeń")
        return BMI
    elif BMI > 30:
        print("Masz otyłość!!! Udaj się do lekarza, lub sprawdź poprawność wprowadzonych danych.")
        return BMI

def main():
    s = input("Podaj swoją płeć: ")
    match s.lower():
        case "mężczyzna" | "Mężczyzna":
            print(round(calculator_BMI_M(),2))
    match s.lower():
        case "kobieta"|"Kobieta":
            print(round(calculator_BMI_K()))







