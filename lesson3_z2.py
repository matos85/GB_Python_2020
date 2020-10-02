def data_user(names, surnames, ages, sitys, emails, tel_numbers):
    print(
        f'Имя: {name}. Фамииля: {surname}.Год рождения:{age}. Город: {sity}. Email: {email}. Номер телефона: {tel_number} ')


info_user = input('Введите Имя, Фамилию, Год рождения, Город, Email, Номер телефона. Введено: ').split()
for i in info_user:
    name = info_user[0]
    surname = info_user[1]
    age = info_user[2]
    sity = info_user[3]
    email = info_user[4]
    tel_number = info_user[5]
data_user(names=name, surnames=surname, ages=age, sitys=sity, emails=email, tel_numbers=tel_number)
