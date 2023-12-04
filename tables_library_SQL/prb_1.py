from sqlalchemy import create_engine
import pandas as pd

# import mysql.connector
df = pd.read_csv("C:/Users/alejo/Downloads/prestamos_libros_biblioteca.csv")
# engine = ce('C:/Users/alejo/Documents/dumps/Dump20230920')
db_conn = create_engine(url=f'mysql://root:123456@localhost/librarys')


class library():
    def book_load(self):
        """
        Esta clase carga los datos relevnates con la tabla libro
        :return:
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

    def filter_published_year(self, pos_year_search):
        """
        Esta clase permite mostrar los libros desde cierto año en adelante
        :param pos_year_search: int
        :return:
        """
        self.loc[self['published_year'].isna(), 'published_year'] = 0

        self['published_year'] = self['published_year'].astype('int16', errors="ignore")
        self = self.drop_duplicates(subset=['book_title', 'author_name'])
        var1 = self[self['published_year'] < pos_year_search]
        return var1



test1 = library.filter_published_year(df, 1800)
print(test1)
def pruebas ():
    file_path = 'ml-100k/u.item'
    separator = '|'

    # Nombres de columnas (ajusta esto según tus necesidades)
    m_cols = ['id', 'name_book']

    # Codificación
    encoding = 'latin-1'

    # Lectura del archivo
    df_books = pd.read_csv(df_rooute_1, sep=separator, names=m_cols, encoding=encoding)
    # engine = ce('C:/Users/alejo/Documents/dumps/Dump20230920')
    # Ruta al archivo y separador
    # df = pd.read_csv('C:/Users/alejo/Desktop/pythonProject4/books.csv', delimiter=',')
    # column_names = ['id', 'name_book']
    # df = pd.read_csv(df_rooute_1, delimiter=',', names=column_names)
    # Nombres de columnas (ajusta esto según tus necesidades)
    m_cols = ['id', 'name_book']
    file_path = 'ml-100k/u.item'
    separator = '|'


