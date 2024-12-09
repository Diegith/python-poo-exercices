class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_cedula(self, cedula):
        self._cedula = cedula

    def get_cedula(self):
        return self._cedula

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono


class EmpleadoIndefinido(Empleado):
    def __init__(
        self, nombre, cedula, telefono, nPlaza, salarioBase, duracion_contrato
    ):
        # constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)

        # nuevos atributos
        self._nPlaza = nPlaza
        self._salarioBase = salarioBase
        self._duracion_contrato = duracion_contrato

    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza

    def get_nPlaza(self):
        return self._nPlaza

    def set_salario_base(self, salarioBase):
        self._salarioBase = salarioBase

    def get_salario_base(self):
        return self._salarioBase

    def set_duracion_contrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato

    def get_duracion_contrato(self):
        return self._duracion_contrato

    def calcularSalarioTotal(self):
        return self._salarioBase + (self._salarioBase * 0.02)


class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salarioBase, categoria):
        # constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)

        # nuevos atributos
        self._nPlaza = nPlaza
        self._salarioBase = salarioBase
        self._categoria = categoria

    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza

    def get_nPlaza(self):
        return self._nPlaza

    def set_salario_base(self, salarioBase):
        self._salarioBase = salarioBase

    def get_salario_base(self):
        return self._salarioBase

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria

    def calcularSalarioTotal(self):
        if self._categoria == 1:
            return self._salarioBasse + (self._salarioBase * 0.03)

        elif self._categoria == 2:
            return self._salarioBasse + (self._salarioBase * 0.05)

        elif self._categoria == 3:
            return self._salarioBasse + (self._salarioBase * 0.08)

        else:
            return self._salarioBase


class EmpleadoSubcontato(Empleado):
    def __init__(self, nombre, cedula, telefono, empresaResponsable):
        # constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)

        # nuevos atributos
        self._empresaResponsable = empresaResponsable

    def set_empresaResponsable(self, empresa):
        self._empresaResponsable = empresa

    def get_empresaResponsable(self):
        return self._empresaResponsable


# Empleado subcontratados

sub_contrato1 = EmpleadoSubcontato(
    "Roberto Flores Morales", 1234567, 8888888, "Coca-Cola"
)
sub_contrato2 = EmpleadoSubcontato("Ana Mora Cruz", 223344576, 7777777, "Pepsi")

sub_contratos = [sub_contrato1, sub_contrato2]

print("\n***  Empleados subcontratados  ***")
for i, sub_cont in enumerate(sub_contratos):
    print(f"\n**** Empleado {i+1} ****")
    print(
        f"Nombre: {sub_cont.get_nombre()} \nCédula: {sub_cont.get_cedula()} \nTeléfono: {sub_cont.get_telefono()} \nEmpresaResponsable: {sub_cont.get_empresaResponsable()}"
    )

# Empleado por tiempo definido

contrato_def1 = EmpleadoDefinido("Jeff Muñoz Castro", 67353224, 6666666, 3, 5000000, 2)
contrato_def2 = EmpleadoDefinido(
    "María Gonzalez Pérez", 7623566, 5555555, 2, 6000000, 3
)

contratos_def = [contrato_def1, contrato_def2]

print("\n***  Empleados por tiempo definido  ***")
for i, contr_def in enumerate(contratos_def):
    print(f"\n**** Empleado {i+1} ****")
    print(
        "Nombre: "
        + contr_def.get_nombre()
        + "\nCédula: "
        + str(contr_def.get_cedula())
        + "\nTeléfono: "
        + str(contr_def.get_telefono())
        + "\nPlaza: "
        + str(contr_def.get_nPlaza())
        + "\nSalario Base: "
        + str(contr_def.get_salario_base())
        + "\nCategoria: "
        + str(contr_def.get_categoria())
    )


# empleado por tiempo indefinido
contrato_indef1 = EmpleadoIndefinido("Roberto Rojas", 56436346, 2222222, 4, 3500000, 1)
contrato_indef2 = EmpleadoIndefinido("Rebeca Suaréz", 87589325, 33442266, 7, 5100000, 2)
contrato_indef3 = EmpleadoIndefinido("Sara Vega", 989427358, 667778833, 5, 4750000, 3)

contratos_indef = [contrato_indef1, contrato_indef2, contrato_indef3]
print("\n***  Empleados por tiempo indefinido  ***")
for i, contr_indef in enumerate(contratos_indef):
    print(f"\n**** Empleado {i+1}")
    print(
        f"Nombre: {contr_indef.get_nombre()} \nCédula: {contr_indef.get_cedula()} \nTeléfono: {contr_indef.get_telefono()} \nPlaza: {contr_indef.get_nPlaza()}  \nSalario Base: {contr_indef.get_salario_base()} \nSalario total: {contr_indef.calcularSalarioTotal()} \nDuración contrato: {contr_indef.get_duracion_contrato()}"
    )
