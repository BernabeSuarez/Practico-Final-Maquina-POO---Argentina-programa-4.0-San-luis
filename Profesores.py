class Profesores:
    def __init__(self, nombre, materia, curso, division):
        self._nombre = nombre
        self._materia = materia
        self._curso = curso
        self._division = division

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def set_materia(self, new_materia):
        self._materia = new_materia

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def set_curso(self, new_curso):
        self._curso = new_curso

    @property
    def materia(self):
        return self._materia

    @materia.setter
    def set_materia(self, new_materia):
        self._materia = new_materia
