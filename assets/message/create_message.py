def create_mentor_card(db_data):
    card_mentor = '''
<strong>{} {}</strong> \n
Основной язык: <strong>{}</strong> 
Дополнительные языки: <strong>{}</strong> 
Ссылка на телеграм: <a href="{}">{}</a> 
    '''.format( \
        db_data[0], \
        db_data[1], \
        db_data[2], \
        db_data[3], \
        db_data[4], \
        db_data[4])
    return card_mentor
