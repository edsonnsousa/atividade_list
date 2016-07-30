def main():
    print"_________________________________"
    
    todos_alunos=[]
    while True:
        opcao = int(input("#1 Novo Aluno||#2 Listar||#0 Sair \n"))
        print"_________________________________"
        if opcao == 1:
            aluno =novo_aluno()
            todos_alunos.append(aluno)
        elif opcao ==2:
            lista_aluno(todos_alunos)
        elif opcao ==0:
            break
    print"Fim da operacao"
def novo_aluno():
	nome = raw_input('Nome: ')
	sexo = raw_input('Sexo |M-F|: ')
	idade = input('Idade: ')
	aluno = {'nome': nome, 'idade': idade, 'sexo':sexo} 
	return aluno    
def lista_aluno(todos_alunos):
    for i in range(len(todos_alunos)):
        print  todos_alunos[i]['nome']," || ", todos_alunos[i]['idade'],"anos || Sexo: ", todos_alunos[i]['sexo']," || "
    
if __name__ == '__main__':
	main()
