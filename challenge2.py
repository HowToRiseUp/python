CURRENT_YEAR = 2023 #constant varialbe
print("Nhập con mẹ mày tên :")
first_name = input()
print("Nhập con mẹ mày họ :")
last_name = input()
print("Năm Sinh : ")
year_born = input()
year_born = int(year_born)
age = CURRENT_YEAR - year_born
print("Hello " + first_name +" "+ last_name +" nhé !")
print(str(age) + " Tuổi " + "|| vào năm" + str(CURRENT_YEAR))


