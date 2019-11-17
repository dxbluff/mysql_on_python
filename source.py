import mysql.connector

my_db = mysql.connector.connect(
        user='root',
        password='********',
        host='127.0.0.1',
        db='veterinary'
    )

my_cursor = my_db.cursor()


def create_database(cursor, db_name):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name)
        )
    except mysql.connector.Error as err:
        return err


def get_table_code(table_name):
    tables = {
        'Clients':
            """
            CREATE TABLE IF NOT EXISTS Clients (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(60) NOT NULL,
                birth_date DATE NOT NULL,
                mail VARCHAR(60) NOT NULL,
                phone_number VARCHAR(15) NOT NULL,
                gender CHAR(1) NOT NULL,
                UNIQUE KEY(full_name, birth_date)
            );
            """,
        'Pets':
            """
            CREATE TABLE IF NOT EXISTS Pets (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(30) NOT NULL,
                birth_date DATE NOT NULL, 
                animal_type VARCHAR(60) NOT NULL,
                gender CHAR(1) NOT NULL,
                Clients_ID INT NOT NULL,
                FOREIGN KEY(Clients_ID)
                    REFERENCES Clients(id) 
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                UNIQUE KEY(name, birth_date, animal_type)
            );
            """,
        'Doctors':
            """
            CREATE TABLE IF NOT EXISTS Doctors(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(60) NOT NULL,
                birth_date DATE NOT NULL,
                specialization VARCHAR(30) NOT NULL,
                work_expirience INT NOT NULL,
                gender CHAR(1) NOT NULL,
                UNIQUE KEY(full_name, birth_date)
            );
            """,
        'Medical_testings':
            """
            CREATE TABLE IF NOT EXISTS Medical_testings(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                testing_type VARCHAR(30) NOT NULL,
                testing_date DATETIME NOT NULL,
                room_number INT NOT NULL
            );
            """,
        'Labaratory_staff':
            """
            CREATE TABLE IF NOT EXISTS Labaratory_staff(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(60) NOT NULL,
                birth_date DATE NOT NULL,
                work_expirience INT NOT NULL,
                gender CHAR(1) NOT NULL,
                UNIQUE KEY(full_name, birth_date)
            );            
            """,
        'Visits':
            """
            CREATE TABLE IF NOT EXISTS Visits(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                room_number VARCHAR(30) NOT NULL,
                visit_date DATETIME NOT NULL,
                Clients_ID INT NOT NULL,
                FOREIGN KEY (Clients_ID)
                    REFERENCES Clients(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Doctors_ID INT NOT NULL,
                FOREIGN KEY (Doctors_ID)
                    REFERENCES Doctors(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Pets_ID INT NOT NULL,
                FOREIGN KEY (Pets_ID)
                    REFERENCES Pets(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT		
            );
            """,
        'Referals_to_testing':
            """
            CREATE TABLE IF NOT EXISTS Referals_to_testing(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Medical_testings_ID INT NOT NULL,
                FOREIGN KEY (Medical_testings_ID)
                    REFERENCES Medical_testings(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Doctors_ID INT NOT NULL,
                FOREIGN KEY (Doctors_ID)
                    REFERENCES Doctors(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Pets_ID INT NOT NULL,
                FOREIGN KEY (Pets_ID)
                    REFERENCES Pets(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
            );
            """,
        'Take_testing':
            """
            CREATE TABLE IF NOT EXISTS Take_testing(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                Labaratory_staff_ID INT NOT NULL,
                FOREIGN KEY (Labaratory_staff_ID)
                    REFERENCES Labaratory_staff(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Pets_ID INT NOT NULL,
                FOREIGN KEY (Pets_ID)
                    REFERENCES Pets(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT,
                Medical_testings_ID INT NOT NULL,
                FOREIGN KEY (Medical_testings_ID)
                    REFERENCES Medical_testings(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
            );
            """
    }
    return tables[table_name]


def create_table(table_name):
    my_cursor.execute(get_table_code(table_name))


def main():
    create_table('Pets')
    my_cursor.execute('SHOW TABLES')
    for i in my_cursor:
        print(i)
    my_db.close()


if __name__ == "__main__":
    main()