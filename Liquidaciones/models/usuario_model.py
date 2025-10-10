class UsuarioModel:
    """Modelo simple en memoria para usuarios (MVP).
    Para producción sustituir por base de datos.
    """
    usuarios_db = {}

    @classmethod
    def registrar(cls, usuario):
        if usuario.username in cls.usuarios_db:
            raise ValueError("El usuario ya existe")
        cls.usuarios_db[usuario.username] = usuario.password

    @classmethod
    def verificar(cls, username, password):
        return cls.usuarios_db.get(username) == password