def main():
	menu = input("#1 Novo Aluno||#2 Listar||#0 Sair \n")
	while True:
		opcao = menu()
		if menu ==1:
			novo_aluno()
		elif menu ==2:
			listar_alunos()
		elif menu ==0:
			break	
if __name__ == '__main__':
	main()
