import os
import json


def load_candidates_from_json(name_file):
    """
    Функция загрузки данных в список и файла json
    :param name_file: имя файла
    :return: весь список кандидатов
    """
    # Загрузка json если файл найден
    if os.path.isfile(name_file):
        with open(name_file, 'r', encoding='utf8') as json_file:
            all_candidates = json.load(json_file)
            return all_candidates
    else:
        return None


def get_candidate_id(person_id, all_candidates):
    """
    Функция возвращает кандидата  по его id
    :param person_id: искомый id
    :param all_candidates: список всех кандидатов
    :return: найденный кандидат
    """
    person = list(filter(lambda item: item['id'] == person_id, all_candidates))
    return person


def get_candidates_by_skill(all_candidates, skill_name):
    """
    Функция  возвращает отфильтрованный список  кандидатов по скилу
    :param all_candidates: список кандидатов
    :param skill_name: скил
    :return: отфильтрованный список
    """
    candidates_filter = []
    for candidate_ in all_candidates:
        list_skill = create_list_skill(candidate_['skills'])
        if skill_name in list_skill:
            candidates_filter.append(candidate_)
    return candidates_filter


def get_candidates_by_name(find_str, all_candidates):
    """
    Функция поиска вхождения подстроки в имя кандидата
    :param find_str: искомая подстрока
    :param all_candidates: список кандидатов
    :return: список кандидатов в которой найдена подстрока
    """
    find_list = []
    for person in all_candidates:
        if find_str.lower() in person["name"].lower():
            find_list.append(person)
    return find_list


def get_sort_skill(all_candidates):
    """
    Функция формирует список уникальных скилов в нижнем регистре
    отсортированных по алфавиту для списка фильтра.
    :param all_candidates: список всех кандидатов
    :return: список уникальных скилов
    """
    # Формируем список скилов
    list_skill = []
    for _ in all_candidates:
        list_skill += create_list_skill(_['skills'])
    # Делаем список скилов уникальным
    list_skill = list(set(list_skill))
    # Сортируем скилы  при передаче
    return sorted(list_skill)


def create_list_skill(skill_str):
    """
    Функция получаюет строку элементов  разделенных запятыми и возвращаеи список в нижнем регистре и
    очищенные от пробелов элементы списка
    :param skill_str:
    :return: список list_skill
    """
    list_skill = skill_str.lower().split(',')
    list_skill = [x.strip() for x in list_skill]
    return list_skill
