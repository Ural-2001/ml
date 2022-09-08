import pandas as pd
import matplotlib.pyplot as plt


def get_unique(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique


def read_csv(file):
    data = pd.read_csv(file)
    return data


def ages(dataset):
    p_ages = list(dataset.Age)
    p_ages_without_nan = []
    colors = []
    numb = []

    for i in range(0, len(p_ages)):
        p_ages[i] = str(p_ages[i])
        if p_ages[i] != 'nan':
            p_ages_without_nan.append(float(p_ages[i]))

    uniq_p_ages = []
    i = 0
    for age in p_ages_without_nan:
        numb.append(i + 1)
        if age not in uniq_p_ages:
            uniq_p_ages.append(age)
            colors.append('r')
        i += 1
    uniq_p_ages.sort()

    people_by_ages = []
    for i in range(0, len(uniq_p_ages)):
        people_by_ages.append(0)

    for i in range(0, len(p_ages_without_nan)):
        people_by_ages[uniq_p_ages.index(p_ages_without_nan[i])] += 1

    print('уникальные возраста:', uniq_p_ages)

    p_ages_without_nan.sort()
    plt.bar(uniq_p_ages, people_by_ages, color=colors)
    plt.show()


def get_survived(dataset):
    uniq_p_classes = list(get_unique(dataset.Pclass))
    uniq_p_classes.sort()
    p_classes = list(dataset.Pclass)
    genders = list(dataset.Sex)
    survived = list(dataset.Survived)

    total_male_by_pclass = []
    survived_male_by_pclass = []
    total_female_by_pclass = []
    survived_female_by_pclass = []

    for i in range(0, len(uniq_p_classes)):
        total_male_by_pclass.append(0)
        survived_male_by_pclass.append(0)
        total_female_by_pclass.append(0)
        survived_female_by_pclass.append(0)

    for i in range(0, len(p_classes)):
        if genders[i] == 'male':
            total_male_by_pclass[p_classes[i] - 1] += 1
            if survived[i] == 0:
                survived_male_by_pclass[p_classes[i] - 1] += 1
        else:
            total_female_by_pclass[p_classes[i] - 1] += 1
            if survived[i] == 0:
                survived_female_by_pclass[p_classes[i] - 1] += 1

    print('всего мужчин по классам:', total_male_by_pclass)
    print('выжившие мужчины по классам:', survived_male_by_pclass)
    print('всего женщин по классам:', total_female_by_pclass)
    print('выжившие женщины по классам:', survived_female_by_pclass)

    survived_male_by_pclass_percent = []
    survived_female_by_pclass_percent = []

    for i in range(0, len(total_male_by_pclass)):
        survived_male_by_pclass_percent.append(survived_male_by_pclass[i] * 100 / total_male_by_pclass[i])

    for i in range(0, len(total_female_by_pclass)):
        survived_female_by_pclass_percent.append(survived_female_by_pclass[i] * 100 / total_female_by_pclass[i])

    print('% выживших мужчин по классам', survived_male_by_pclass_percent)
    print('% выживших женщин по классам', survived_female_by_pclass_percent)


def draw(dataset):
    uniq_p_classes = list(get_unique(dataset.Pclass))
    uniq_p_classes.sort()
    p_classes = list(dataset.Pclass)

    total_people_by_p_class = []

    for i in range(0, len(uniq_p_classes)):
        total_people_by_p_class.append(0)

    for i in range(0, len(p_classes)):
        total_people_by_p_class[p_classes[i] - 1] += 1

    print('всего людей по классам:', total_people_by_p_class)

    vals = total_people_by_p_class
    labels = uniq_p_classes
    fig, ax = plt.subplots()
    ax.pie(vals, labels=labels)
    ax.axis("equal")
    plt.show()


data = read_csv("datasets/titanic.csv")
get_survived(data)
draw(data)
ages(data)
