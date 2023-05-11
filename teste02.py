#Definindo reservas
#"M01": ["U001"]
reservas = {
    "M01": [],
    "M02": [],
    "M03": [],
    "M04": []
}

aux_reserva3 = "M01"
aux_emprestimo_reserva1 = 0
aux_emprestimo_reserva2 = reservas[aux_reserva3]
for f in aux_emprestimo_reserva2:
    if (len(aux_emprestimo_reserva2)) < 2:
        aux_emprestimo_reserva1 = 1
print(aux_emprestimo_reserva1)