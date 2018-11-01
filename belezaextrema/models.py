from django.db import models

# Create your models here.


class usuario(models.Model):
	login = models.CharField(
			max_length = 25,
			null = False,
			blank = False
		)

	senha = models.CharField(
			max_length = 25,
			null = False,
			blank = False
		)

class cliente(models.Model):
	nome_completo = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)

	data_nascimento = models.CharField(
			max_length = 8,
			null = False,
			blank = False
		)

	contato = models.CharField(
			max_length = 15,
			null = False,
			blank = False
		)

	email = models.CharField(
			max_length = 50,
			null = False,
			blank = False
		)

	cpf = models.CharField(
			'CPF',
			max_length = 15,
			null = False,
			blank = False,
			unique = True
		)

	credito = models.CharField(
			max_length = 255,
			null = False,
			blank = False,
			default = 'DEFAULT VALUE'
		)
	def __str__(self):
   		return self.nome_completo

class vendedor(models.Model):
	nome_completo = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)

	data_nascimento = models.CharField(
			max_length = 8,
			null = False,
			blank = False
		)

	contato = models.CharField(
			max_length = 15,
			null = False,
			blank = False
		)

	endereco = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)

	email = models.CharField(
			max_length = 50,
			null = False,
			blank = False
		)

	cpf_cnpj = models.CharField(
			'CPF',
			max_length = 15,
			null = False,
			blank = False,
			unique = True
		)

	credito = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)
	def __str__(self):
   		return self.nome_completo

class fornecedor(models.Model):
	nome_fornecedor = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)


	contato = models.CharField(
			max_length = 15,
			null = False,
			blank = False
		)

	endereco = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)

	email = models.CharField(
			max_length = 50,
			null = False,
			blank = False
		)

	cpf_cnpj = models.CharField(
			max_length = 15,
			null = False,
			blank = False,
			unique = True
		)

	credito = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)
	def __str__(self):
   		return self.nome_fornecedor

class categoria(models.Model):
	nome_categoria = models.CharField(
			max_length = 255,
			blank = False,
			null = False
		)
	descricao_categoria = models.CharField(
			max_length = 255,
			blank = False,
			null = False
		)

	foto_categoria = models.ImageField(
			upload_to='categoria_foto',
	 		blank = False,
	 		null = False
	 	)
	def __str__(self):
   		return self.nome_categoria

class produto(models.Model):
	nome_produto = models.CharField(
			max_length = 255,
			null = False,
			blank = False
		)

	descricao_produto = models.CharField(
			max_length= 255,
			null = False,
			blank = False
		)

	categoria_produto = models.ForeignKey(
	 		categoria, on_delete=models.CASCADE
	 	)

	referencia_produto = models.CharField(
	 		max_length = 255,
	 		null = False,
	 		blank = False
	 	)

	peso_produto = models.CharField(
	 		max_length = 255,
	 		null = False,
	 		blank = False
	 	)

	foto_produto = models.ImageField(
	 		upload_to = 'produto_foto',
	 		blank = False,
	 		null = False
	 	)
	def __str__(self):
   		return self.nome_produto