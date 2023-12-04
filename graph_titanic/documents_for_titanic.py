import pandas as pd
import matplotlib.pyplot as plt
import graphics
import seaborn as sns

df = pd.read_csv("C:/Users/alejo/Desktop/pythonProject5/tested.csv")


def choose_var_1(a):
    """
    :param a: this case and practically only case is date frame of the titanic
    :return: var chosen
    """
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


def use_mode():
    """
    mode to choose the graphics to use

    :return:graphs
    """
    df = pd.read_csv("C:/Users/alejo/Desktop/pythonProject5/tested.csv")
    df = df.drop_duplicates()

    var_option = input("""experimentent, or use pre-made variables
    1)experiment
    2)pre-made
    option: """)
    if var_option == '1':
        amount_var = input("""amount var for use: 1 or 2: """)
        if amount_var == '1':
            graphics.graphics_use_for_var_one_var(choose_var_1(df))

        if amount_var == '2':
            graphics.graphics_use_for_vars(choose_var_1(df), choose_var_1(df))

    if var_option == '2':
        pre_graphic = input("""select the option what do you want to see
            1) comparison between the living and the dead depending on sex, and age
            2) graphics dispers
            3)histogram of age
            4)histogram of fare
            5)Distribution the Fare for Survivor
            Option: """)
        if pre_graphic == '1':
            sns.violinplot(x='Survived', y='Age', hue='Sex', data=df, split=True)
            plt.title('Distribution the Age for Survivor and Gender')
            plt.show()

        if pre_graphic == '2':
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='Age', y='Survived', data=df, alpha=0.7)
            plt.title('scatter: Age vs. Survivors')
            plt.xlabel('Age')
            plt.ylabel('Survivors (0: Not, 1: yes)')
            plt.show('survivor for fare')

        if pre_graphic == '3':
            a = df.loc[:, ['Age']]
            graphics.graphics_use_for_var_one_var(a)
            plt.title('age')
            plt.tight_layout()
            plt.show()
        if pre_graphic == '4':
            df = df.loc[:, ['Fare']]
            df['Fare'] = df['Fare'].astype('float64')
            graphics.graphics_use_for_var_one_var(df)
            plt.title(' ticket price')
            plt.tight_layout()
            plt.show()
        if pre_graphic == '5':
            plt.figure(figsize=(10, 6))
            sns.violinplot(x='Survived', y='Fare', data=df, split=True)
            plt.title('Distribution the Fare for Survivor')
            plt.xlabel('Survivors (0: Not, 1: yes)')
            plt.ylabel('Fare')
            plt.show()

# 'PassengerId','n','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'
