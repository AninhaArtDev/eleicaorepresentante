
votos_ana = 0
votos_bruno = 0
votos_carlos = 0
votos_brancos = 0

opcao = 0

while opcao != 6:

    print("\n===== ELEIÇÃO DO REPRESENTANTE =====")
    print("1 - Votar em Ana")
    print("2 - Votar em Bruno")
    print("3 - Votar em Carlos")
    print("4 - Votar em branco")
    print("5 - Consultar resultado parcial")
    print("6 - Encerrar votação")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        votos_ana += 1
        print("Voto em Ana registrado!")

    elif opcao == 2:
        votos_bruno += 1
        print("Voto em Bruno registrado!")

    elif opcao == 3:
        votos_carlos += 1
        print("Voto em Carlos registrado!")

    elif opcao == 4:
        votos_brancos += 1
        print("Voto em branco registrado!")

    elif opcao == 5:
        total = votos_ana + votos_bruno + votos_carlos + votos_brancos

        print("\n===== RESULTADO PARCIAL =====")
        print("Ana:", votos_ana, "votos")
        print("Bruno:", votos_bruno, "votos")
        print("Carlos:", votos_carlos, "votos")
        print("Brancos:", votos_brancos, "votos")
        print("Total de votos:", total)

    elif opcao == 6:
        print("\nEncerrando votação...")

    else:
        print("Opção inválida! Escolha uma opção de 1 a 6.")


total = votos_ana + votos_bruno + votos_carlos + votos_brancos

print("\n===== RESULTADO FINAL =====")
print("Ana:", votos_ana, "votos")
print("Bruno:", votos_bruno, "votos")
print("Carlos:", votos_carlos, "votos")
print("Brancos:", votos_brancos, "votos")
print("Total de votos:", total)


if votos_ana > votos_bruno and votos_ana > votos_carlos:
    print("Candidato vencedor: Ana")

elif votos_bruno > votos_ana and votos_bruno > votos_carlos:
    print("Candidato vencedor: Bruno")

elif votos_carlos > votos_ana and votos_carlos > votos_bruno:
    print("Candidato vencedor: Carlos")

else:
    maior = votos_ana

    if votos_bruno > maior:
        maior = votos_bruno

    if votos_carlos > maior:
        maior = votos_carlos

    print("Houve empate entre os candidatos mais votados!")

print("Votação encerrada!")
