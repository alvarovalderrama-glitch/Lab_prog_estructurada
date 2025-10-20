primer_digito = int(input("ingrese primer dígito de su rut: "))
segundo_digito = int(input("ingrese segundo dígito de su rut: "))
tercer_digito = int(input("ingrese tercer dígito de su rut: "))
cuarto_digito = int(input("ingrese cuarto dígito de su rut: "))
quinto_digito = int(input("ingrese quinto dígito de su rut: "))
sexto_digito = int(input("ingrese sexto dígito de su rut: "))
septimo_digito = int(input("ingrese séptimo dígito de su rut: "))
octavo_digito = int(input("ingrese octavo dígito de su rut: "))
rut = [primer_digito,segundo_digito,tercer_digito,cuarto_digito,quinto_digito,sexto_digito,septimo_digito,octavo_digito]
print(rut)
nuevo_rut = ((octavo_digito * 2),(septimo_digito * 3),(sexto_digito * 4),(quinto_digito * 5),(cuarto_digito * 6),(tercer_digito * 7),(segundo_digito * 2),(primer_digito * 3))
resultado = sum(nuevo_rut)
resto = resultado % 11
if resto == 0:
    print('el digito verificador es 0')
elif resto == 1:
    print('el digito verificador es k')
elif resto > 1 or resto < 11:
    aux = 11 - resto
    print('el digito verificador es', aux)