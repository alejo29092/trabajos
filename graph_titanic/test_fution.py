"""
here I did tests to know what to use
"""

import pandas as pd
import matplotlib.pyplot as plt
import graphics

df = pd.read_csv("C:/Users/alejo/Desktop/pythonProject5/tested.csv")
# print(f'rows: {df.shape}')
# print(df)
df = df.drop_duplicates()


# print(df)
# print(f'rows: {df.shape}')


# print(df)


# self = df.loc[
#          df['published_year'].isna(), 'published_year'] = 0

def fare_passager(a):
    fare_date = a.loc[:, ['Fare']]
    fare_date = fare_date.drop_duplicates(subset=['Fare'])
    print(fare_date)


def passenger_survivor(self):
    pass


def surviving_passagers_chart_sex(a):
    date_survivor = a.loc[:, ['Survived', 'Sex']]
    womens = date_survivor.drop(subset=['sex' 'male'])
    print(womens)


def choose_var_1(a):
    a = a.drop_duplicates(subset=['PassengerId'])
    v = input("""put the var 1 among the following'
              1 PassengerId
              2 Survived 
              3 Pclass 
              4 Name 
              5 Sex 
              6 Age 
              7 SibSp
              8 Parch
              9 Ticket
              10 Fare
              11 Cabin
              12 Embarked
              option: """)
    if v == '1':
        a = a.loc[:, ['PassengerId']]

        return a
    if v == '2':
        a = a.loc[:, ['Survived']]
        return a
    if v == '3':
        a = a.loc[:, ['Pclass']]
        return a
    if v == '4':
        a = a.loc[:, ['Name']]
        return a
    if v == '5':
        a = a.loc[:, ['Sex']]
        return a
    if v == '6':
        a = a.loc[:, ['Age']]
        return a
    if v == '7':
        a = a.loc[:, ['SibSp']]
        return a
    if v == '8':
        a = a.loc[:, ['Parch']]
        return a
    if v == '9':
        a = a.loc[:, ['Ticket']]
        return a
    if v == '10':
        a = a.loc[:, ['Fare']]
        return a
    if v == '11':
        a = a.loc[:, ['Cabin']]
        return a
    if v == '12':
        a = a.loc[:, ['Embarked']]
        return a


def choose_var_2(a):
    a = a.drop_duplicates(subset=['PassengerId'])
    v = input("""put the var 2 among the following'
              1 PassengerId
              2 Survived 
              3 Pclass 
              4 Name 
              5 Sex 
              6 Age 
              7 SibSp
              8 Parch
              9 Ticket
              10 Fare
              11 Cabin
              12 Embarked
              option: """)
    if v == '1':
        a = a.loc[:, ['PassengerId']]
        return a
    if v == '2':
        a = a.loc[:, ['Survived']]
        return a
    if v == '3':
        a = a.loc[:, ['Pclass']]
        return a
    if v == '4':
        a = a.loc[:, ['Name']]
        return a
    if v == '5':
        a = a.loc[:, ['Sex']]
        return a
    if v == '6':
        a = a.loc[:, ['Age']]
        return a
    if v == '7':
        a = a.loc[:, ['SibSp']]
        return a
    if v == '8':
        a = a.loc[:, ['Parch']]
        return a
    if v == '9':
        a = a.loc[:, ['Ticket']]
        return a
    if v == '10':
        a = a.loc[:, ['Fare']]
        return a
    if v == '11':
        a = a.loc[:, ['Cabin']]
        return a
    if v == '12':
        a = a.loc[:, ['Embarked']]
        return a


def use_mode(df):
    df = df
    var_option = input("""experimentent, or use pre-made variables
    1) experiment
    2)pre-made
    option: """)
    if var_option == '1':
        graphics.graphics_use_for_2_vars(choose_var_1(df), choose_var_2(df))
    if var_option == '2':
        pre_graphic = input("""select the option what do you want to see
            1) comparison between the living and the dead depending on sex
            2)
            Option: """)
        if pre_graphic == '1':
            df = df.drop_duplicates(subset=['PassengerId'])
            var_df_surviver = df.loc[:, ['Survived']]
            var_df_sex = df.loc[:, ['Sex']]
            # graphics.graphics_use_for_2_vars(var_df_surviver, var_df_sex)
            graphics.graphics_use_for_2_vars(var_df_surviver)
            # plt.hist(var_df_surviver, bins=15)
            plt.tight_layout()
            plt.show()

        if pre_graphic == '2':
            graphics.graphics_use_for_2_vars()


# 'PassengerId','Survived','Pclass','Age','SibSp','Parch','Ticket','Fare'
# 'PassengerId','n','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'
df.info()
cols_cat = ['Name', 'Sex', 'Embarked', 'Cabin', 'Fare']

for col in cols_cat:
    print(f'column: {col}: {df[col].nunique()}, sublevel')


def not_funtional():
    a = df.loc[:, ['Age']]
    plt.hist(a)
    # graphics.graphics_use_for_vars(var_df_surviver)
    # plt.hist(var_df_surviver, bins=15)
    plt.tight_layout()
    plt.show()


not_funtional()


def data_boxplot():
    cols_num = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare']
    fig, ax = plt.subplot(nrow=7, ncpls=1, figsize=(8, 30))

