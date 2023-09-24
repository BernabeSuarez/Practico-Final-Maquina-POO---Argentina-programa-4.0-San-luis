# la fecha, nombre del estudiante, nombre de la materia, nombre del profesor, curso, división y la nota obtenida
# (este valor inicialmente es -1)


class Inscripciones:
    def __init__(self, fecha, nombre, materia, profesor, curso, division, nota=-1):
        """Inicializa una inscripcion con los datos dados."""
        self._fecha = fecha
        self._nombre = nombre
        self._materia = materia
        self._profesor = profesor
        self._curso = curso
        self._division = division
        self._nota = nota

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def set_fecha(self, new_fecha):
        self._fecha = new_fecha

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
    def profesor(self):
        return self._profesor

    @profesor.setter
    def set_profesor(self, new_profesor):
        self._profesor = new_profesor

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def set_curso(self, new_curso):
        self._curso = new_curso

    @property
    def division(self):
        return self._division

    @division.setter
    def set_division(self, new_division):
        self._division = new_division

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def set_nota(self, new_nota):
        self._nota = new_nota
