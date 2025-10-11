from core.database import get_connection

class UsuarioModel:

    @staticmethod
    def autenticar(email: str, password: str):
        conexion = get_connection()
        if conexion is None:
            print("No se pudo establecer conexión con la base de datos.")
            return None

        cursor = conexion.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario