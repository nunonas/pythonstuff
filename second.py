def loadFile():
	while True:
		try:
			nome = raw_input("Nome do ficheiro: ")
			open(nome)
		except IOError as erro1:
			print "Ficheiro", nome, "inexistente"
			resp = raw_input("Voltar a tentar? ")
			if resp.upper() in ["SIM", "S"]:
				continue
			else:
				print "Um bem-haja!"
		break


loadFile()
