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


def choose_var_2(a):
    """
    this use is for var the small quantity
    :param a: this case and practically only case is date frame of the titanic
    :return: var chosen
    """
    a = a.drop_duplicates(subset=['PassengerId'])
    v = input("""put the var 1 among the following'
              1 Survived 
              2 Pclass 
              3 Sex 
              4 Parch
              5 Embarked
              option: """)

    if v == '1':
        a = a.loc[:, ['Survived']]
        return a
    if v == '2':
        a = a.loc[:, ['Pclass']]
        return a
    if v == '3':
        a = a.loc[:, ['Sex']]
        return a
    if v == '4':
        a = a.loc[:, ['Parch']]
        return a
    if v == '5':
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
            graphics.graphics_use_for_var_one_var(choose_var_2(df))
            plt.show()

        if amount_var == '2':
            graphics.graphics_use_for_vars(choose_var_2(df), choose_var_1(df))

    if var_option == '2':
        pre_graphic = input("""select the option what do you want to see
            1)comparison between the living and the dead depending on sex, and class
            2)graphics dispers the age and survived
            3)histogram of age
            4)histogram of fare
            5)Distribution the Fare for Survivor
            6)histogram survived in for the class
            7)histogram price for class
            Option: """)
        if pre_graphic == '1':
            sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True)
            plt.title('Distribution the Age for Survivor and Gender')

            plt.show()

        if pre_graphic == '2':
            df['Age'] = df.apply(lambda row: row['Age'] + 0.2 if row['Survived'] == 0 else row['Age'], axis=1)
            plt.figure(figsize=(10, 6))

            # Scatter plot
            sns.scatterplot(x='PassengerId', y='Age', hue='Survived', data=df, palette={0: 'red', 1: 'blue'}, alpha=0.7)

            plt.title('Scatter Plot: Age vs. Survivors')
            plt.xlabel('PassengerId')
            plt.ylabel('Age')
            plt.legend(title='Survived', labels=['Not Survived', 'Survived'])
            plt.show()
        if pre_graphic == '3':
            """
            more improvement
            """
            a = df.loc[:, ['Age']]
            sns.histplot(a)
            plt.title('age')
            plt.tight_layout()
            plt.show()
        if pre_graphic == '4':
            df = df.loc[:, ['Fare']]
            df['Fare'] = df['Fare'].astype('float64')
            sns.histplot(df)
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
        if pre_graphic == '6':
            sns.histplot(x='Pclass', hue='Survived', data=df)
            plt.show()
        if pre_graphic == '7':
            sns.histplot(x='Fare', hue='Pclass', data=df)
            plt.show()
        if pre_graphic == '8':
            """
            test
            """
            df = df.sort_values(by='Fare', ascending=False)
            df = df.iloc[:5, ]
            sns.histplot(x='Fare', hue='Sex', data=df)
            plt.show()

# print(df)
# 'PassengerId','n','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'
