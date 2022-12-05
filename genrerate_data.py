import random
import string

import pandas as pd

feature = ['CurrentAge', 'Weight', 'Height', 'Gender', 'MonthOfBirth',
           'HairColor', 'Food', 'FeedingMethod', 'Temper',
           'ExerciseFrequency', 'FirstAlphabetOfName', 'Label']

print(len(feature))
option = 2
data_csv = 'inputs/data.csv' if option == 1 else 'inputs/data-2.csv'
# data distribution
data_count = 5000

# choice
gender_choice = ['F', 'M']
hair_color = ['yellow', 'black', 'white', 'black_and_tan']
food = ['feed', 'can', 'fresh']
feeding_method_choice = ['stocking', 'indoor', 'indoor_and_yard']
temper = ['good', 'bad']

# initialize data of lists.
rows = []
for index in range(data_count):
    current_age = random.randint(0, 9)
    gender = random.randint(0, len(gender_choice) - 1)
    weight = random.randint(5, 15)
    height = random.randint(30, 45)
    m_of_birth = random.randint(1, 12)
    feeding_method = random.randint(0, len(feeding_method_choice) - 1)
    exercise_freq = random.randint(1, 7)

    row = [current_age, weight, height,
           gender, m_of_birth,
           random.randint(0, len(hair_color)),
           random.randint(0, len(food)),
           feeding_method,
           random.randint(0, len(temper) - 1),
           exercise_freq,
           random.randint(0,
                          len(list(
                              string.ascii_uppercase)) - 1)]
    # calculate rules
    """
    [Option1]
    1. If current age >= 1:
        - Female: weight :point_right: 6 ~ 9
        - Male: weight :point_right: 8 ~ 11
    2. If current age >= 1:
        - Height: 35 ~ 41
    3. Month of birth (If is Fibonacci): 1,2,3,5,8
    4. Feeding Method: `indoor` or `indoor and yard`
    5. Exercise frequency per week: 3~7
    """
    label = 0
    if option == 1:
        if current_age >= 1:
            if gender == 0 and weight >= 6 and weight <= 9:
                label = 1
            elif gender == 1 and weight >= 8 and weight <= 11:
                label = 1
            elif height >= 35 and height <= 41:
                label = 1
        elif m_of_birth in [1, 2, 3, 5, 8]:
            label = 1
        elif feeding_method in [1, 2]:
            label = 1
        elif exercise_freq >= 3:
            label = 1
    else:
        # 修改第一個條件 （改為 0.8)
        if current_age >= 0.8:
            if gender == 0 and weight >= 6 and weight <= 9:
                label = 1
            elif gender == 1 and weight >= 8 and weight <= 11:
                label = 1
            elif height >= 35 and height <= 41:
                label = 1
        elif m_of_birth in [1, 2, 3, 5, 8]:
            label = 1
        elif feeding_method in [1, 2]:
            label = 1
        elif exercise_freq >= 3:
            label = 1
    row.append(label)
    rows.append(row)
df = pd.DataFrame(rows, columns=feature)
df.to_csv(data_csv, index=False)
