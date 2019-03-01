"""
    abstract database access

"""

import psycopg2


class DBUtils:
    """Class for Database Access"""

    __host = None
    __port = None
    __user = None
    __pword = None
    __database = None
    __connection = None
    __cursor = None

    def __init__(self, conf):
        config = conf
        self.__host = config.get("host", None)
        self.__port = config.get("port", None)
        self.__user = config.get("user", None)
        self.__pword = config.get("password", None)
        self.__database = config.get("database", None)

    def open(self):
        self.__connection = psycopg2.connect(host=self.__host,
                                             port=self.__port,
                                             user=self.__user,
                                             password=self.__pword,
                                             dbname=self.__database)
        self.__connection.autocommit = True
        self.__cursor = self.__connection.cursor()

    def close(self):
        if self.__cursor.closed is False:
            self.__cursor.close()
        self.__connection.close()

    def execute_nonquery(self, query, data=None):
        """
            Run a DML statement.
        """
        self.__cursor.execute(query, data)
    
    def execute_query(self, query, data=None):
        """
        Run a SELECT statement and return result as list of dict

        """
        self.__cursor.execute(query, data)
        columns = self.__cursor.description
        result = \
            [{columns[index][0]:column for
              index, column in enumerate(value)}
             for value in self.__cursor.fetchall()]
        return result
