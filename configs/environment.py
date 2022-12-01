from dotenv import dotenv_values


class Environment:

    @staticmethod
    def get_db_url():
        return dotenv_values(".env").get("DB_URL")
