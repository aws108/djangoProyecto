from django.db import models



class Categoria(models.Model):
	nombre = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.nombre


class Producto(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=200)
	precio = models.CharField(max_length=200)
	cantidad = models.CharField(max_length=200)
	detalles = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.nombre


"""class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) """