def send_email(message,recipient, *, sender= "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not sender.endswith((".com",".ru",".net",)) or not recipient.endswith((".com",".ru",".net",)):
        print("Невозможно отправить письмо с адреса {} на адрес {}".format(sender, recipient))

    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        print("Письмо отправлено успешно: \nОтправитель: {}\nПолучатель: {}\nСообщение: {}".format(sender, recipient, message))



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

