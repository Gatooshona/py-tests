courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]


def uniq_names():
    all_list = []

    for m in mentors:
        all_list = all_list + m

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)
    all_names_sorted = ", ".join(all_names_sorted)

    return f'Уникальные имена преподавателей: {all_names_sorted}'


def top_names():
    all_list = []

    for m in mentors:
        all_list = all_list + m

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)
    all_names_sorted = ", ".join(all_names_sorted)

    popular = []

    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    return f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]} раз(а)'


def duration():
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    durations_dict = {}

    for id, course in enumerate(courses_list):
        key = course.get("duration")

        if key in durations_dict:
            durations_dict[key].append(id)
        else:
            durations_dict[key] = [id]

    durations_dict = dict(sorted(durations_dict.items()))

    counter = 0
    result_list = []

    for duration, titles in durations_dict.items():
        if len(titles) == 1:
            counter += 1
            result_list.append(f'{courses[titles[0]]} - {duration} месяцев')

        else:
            for idx, title in enumerate(titles):
                counter += 1
                result_list.append(f'{courses[title]} - {duration} месяцев')

    result = ', '.join(result_list)
    return result
