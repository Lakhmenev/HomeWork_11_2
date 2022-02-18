from flask import Flask, render_template, request, redirect
from utils import load_candidates_from_json, get_candidate_id, get_sort_skill, get_candidates_by_skill, \
    get_candidates_by_name


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def page_index():
    # Обработаем фильтр на сайте
    if request.method == 'POST':
        select_skull = request.form.get('select_skull')
        select_find = request.form.get('str_find')
        if select_skull is not None:
            return redirect(f"/skill/{select_skull}")
        elif select_find is not None:
            return redirect(f"/search/{select_find}")

    # Получим уникальный список скилов  для формирования выпадающего списка фильтра
    list_skills = get_sort_skill(all_candidates)

    return render_template('list.html', candidates=all_candidates, list_skills=list_skills)


@app.route("/person/<person_id>/", methods=['GET'])
def candidate(person_id):
    person = get_candidate_id(person_id, all_candidates)
    return render_template('person.html', candidates=person)


@app.route("/skill/<x>/", methods=['GET', 'POST'])
def skill(x):
    limit = 8
    if request.method == 'POST':
        limit_count = request.form.get('limit_count')
        if limit_count is not None and limit_count.isdigit():
            limit = int(limit_count)

    candidates_filter = get_candidates_by_skill(all_candidates, x)
    find_candidates = str(len(candidates_filter))

    start_position = 0
    if limit < len(candidates_filter):
        finish_position = limit
    else:
        finish_position = len(candidates_filter)

    return render_template('skill.html', candidates=candidates_filter[start_position: finish_position],
                           find_candidates=find_candidates, limit=str(limit),
                           start_position=str(start_position+1), finish_position=str(finish_position), skill=x)


@app.route("/search/<find_str>/", methods=['GET'])
def candidates_name(find_str):
    find_list = get_candidates_by_name(find_str, all_candidates)
    count = str(len(find_list))
    return render_template('search.html', count=count, find_str=find_str, find_list=find_list)


if __name__ == '__main__':
    all_candidates = load_candidates_from_json('candidates.json')
    if all_candidates is not None:
        # Активация  режима отладки  для  автоперезапуска сервера  при  изменении кода
        app.debug = True
        app.run(host="127.0.0.1", port=5000)
    else:
        print('Увы, но файл с данными не найден!!!')
        quit()
