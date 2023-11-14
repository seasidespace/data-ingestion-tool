import streamlit as st
from snowflake.connector import connect
from snowflake.connector.pandas_tools import write_pandas

class SnowflakeUploader:
    def __init__(self, connection_params, dataframe):
        self.connection_params = connection_params
        self.dataframe = dataframe
        self.connection = None
        self.options = ('create a new table and insert data', 'Insert the data into an existing table')

    def connect_to_snowflake(self):
        self.connection = connect(**self.connection_params)

    def table_exists(self, table_name):
        # This function checks if the table already exists in Snowflake
        query = f"SHOW TABLES LIKE '{table_name.upper()}'"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchone() is not None
        except ProgrammingError as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def upload_dataframe(self):
        # UI components
        option = st.selectbox('Choose your action:', self.options )

        table_name = st.text_input('Enter the name of the table:')

        if st.button('Upload Data'):
            if not table_name:
                st.warning('Please enter the name of the table.')
                return

            self.connect_to_snowflake()

            if option == self.options[0]:
                self.create_table_and_insert_data(table_name)
            elif option == self.options[1]:
                self.insert_data_into_existing_table(table_name)

    def create_table_and_insert_data(self, table_name):
        if self.table_exists(table_name):
            # If the table exists, issue a warning in Streamlit
            st.warning(f"The table `{table_name}` already exists.")
        else:
            # If the table does not exist, create it and insert the data
            try:
                write_pandas(self.connection, self.dataframe, table_name.upper(), auto_create_table=True)
                st.success(f"Table `{table_name}` created and data inserted successfully.")
            except Exception as e:
                st.error(f"An error occurred while creating the table: {e}")

    def insert_data_into_existing_table(self, table_name):
        # Here you would have logic to insert into an existing table
        # This includes checking if the table exists and if the columns match
        if not self.table_exists(table_name):
            # If the table exists, issue a warning in Streamlit
            st.warning(f"The table `{table_name}` does not exist.")
        else:
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"DESC TABLE {table_name.upper()}")
                table_description = cursor.fetchall()

                # Check if columns match
                table_columns = [desc[0] for desc in table_description]
                df_columns = self.dataframe.columns.tolist()

                if set(df_columns).issubset(set(table_columns)):
                    write_pandas(self.connection, self.dataframe, table_name.upper())
                    st.success(f"Successfully inserted data into Table: `{table_name}` ")

                else:
                    st.warning('The columns of the DataFrame do not match the columns of the existing table.')
            except Exception as e:
                st.error(f"An error occurred while creating the table: {e}")



