from sqlalchemy import create_engine
import pandas as pd

# import mysql.connector
df = pd.read_csv("C:/Users/alejo/Downloads/prestamos_libros_biblioteca.csv")

db_conn = create_engine(url=f'mysql://root:123456@localhost/librarys')
df_authors = pd.read_csv('C:/Users/alejo/Desktop/pythonProject4/authors.csv')
df_rooute_1_books = ('C:/Users/alejo/Desktop/pythonProject4/books.csv')
df_rooute_2_students = ('C:/Users/alejo/Desktop/pythonProject4/students.csv')
df_rooute_3_loans = ('C:/Users/alejo/Desktop/pythonProject4/loans.csv')


def book_load():
    """
    this function returns the authors with the clean data to a sql table
    """
    book_df = df.loc[:, ['published_year', 'book_title', 'author_name']]

    book_df.loc[
        book_df['published_year'].isna(), 'published_year'] = 0  # rellenar valores nullos con un numero por defecto
    # book_df['published_year'] = pd.to_numeric(book_df['published_year'], errors="ignore", downcast='integer')
    book_df['published_year'] = book_df['published_year'].astype('int16', errors="ignore")

    book_df = book_df.drop_duplicates(subset=['book_title', 'author_name'])
    print(book_df)

    book_df = book_df.rename(columns={'book_title': 'name_book'})
    print(book_df)
    book_df = book_df.loc[:, ['published_year', 'name_book']]

    # Export a la tabla libros (Load)
    book_df.to_sql(name='books', con=db_conn, index=False, if_exists='append')


def authors_load():
    """
    this function returns the authors_loads with the clean data to a sql table
    """
    author_df = df.loc[:, ['author_name']]

    author_df = author_df.drop_duplicates(subset=['author_name'])
    author_df = author_df.rename(columns={'author_name': 'name_author'})
    print(author_df)
    author_df.to_sql(name='authors', con=db_conn, index=False, if_exists='append')


def students_load():
    """
    this function returns the students_load with the clean data to a sql table
    """
    student_df = df.loc[:, ['student_name', 'student_email']]
    student_df = student_df.drop_duplicates(subset=['student_email'])
    student_df = student_df.rename(columns={'student_name': 'name_student', 'student_email': 'email'})
    print(student_df)
    student_df.to_sql(name='students', con=db_conn, index=False, if_exists='append')


def book_filter_for_authors():
    """
    clean the data of the books to be able to join them later in the intermediate table
    """
    book_df = df.loc[:, ['book_title', 'author_name']]
    book_df = book_df.drop_duplicates(subset=['book_title', 'author_name'])
    book_df = book_df.rename(columns={'book_title': 'name_book'})

    return book_df


date_book_inner = book_filter_for_authors()
# Codificación
encoding = 'latin-1'

# Lectura del archivo
df_books = pd.read_csv(df_rooute_1_books, delimiter=',', encoding=encoding)

df_books = df_books.rename(columns={'id': 'book_id'})

date_book_inner = date_book_inner.rename(columns={'author_name': 'name_author'})
df_authors = df_authors.rename(columns={'id': 'author_id'})


def inner_books_author_id():
    """
    inner the tables
    """
    inner_var_book = pd.merge(date_book_inner, df_books, on='name_book', how='inner')
    inner_var_book_authors = pd.merge(inner_var_book, df_authors, on='name_author', how='inner')

    return inner_var_book_authors


value_return = inner_books_author_id()


def value_insert():
    final = value_return.loc[:, ['book_id', 'author_id']]
    final.to_sql(name='books_authors', con=db_conn, index=False, if_exists='append')


df_student = pd.read_csv(df_rooute_2_students, delimiter=';', encoding=encoding)


def inner_student_loans():
    """
    clean the data of the books to be able to join them later in the intermediate table
    """
    loans_df = df.loc[:, ['student_email', 'loan_date', 'return_date']]
    loans_df = loans_df.drop_duplicates(subset=['student_email'])
    loans_df = loans_df.rename(columns={'student_email': 'email'})
    inner_loans = pd.merge(loans_df, df_student, on='email', how='inner')
    final_date = inner_loans.loc[:, ['id', 'loan_date', 'return_date']]
    final_date = final_date.rename(columns={'id': 'student_id'})
    final_date.to_sql(name='loans', con=db_conn, index=False, if_exists='append')
    print(final_date)


df_loans = pd.read_csv(df_rooute_3_loans, delimiter=',', encoding=encoding)


def loans_books():
    df2 = df.drop_duplicates(subset=['book_title', 'author_name'])
    loans = df2.loc[:, ['book_title', 'loan_date']]
    loans = loans.rename(columns={'book_title': 'name_book'})
    loans_2 = pd.merge(df_loans, loans, on='loan_date', how='inner')
    loans_3 = pd.merge(loans_2, df_books, on='name_book', how='inner')
    loans_3 = loans_3.rename(columns={'id': 'loans_id', 'book_id': 'books_id'})
    final = loans_3.loc[:, ['books_id', 'loans_id']]
    final.to_sql(name='books_in_loans', con=db_conn, index=False, if_exists='append')
    print(final)
