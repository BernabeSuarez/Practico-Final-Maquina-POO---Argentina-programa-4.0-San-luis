class Encargado:
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    @property
    def dni(self, new_dni):
        return self._dni

    @dni.setter
    def set_dni(self, new_dni):
        self._dni = new_dni
