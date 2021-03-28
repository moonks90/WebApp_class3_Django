from django.db import models
from datetime import datetime,timezone

class Author(models.Model):
    name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def _repr_(self):
        return self.name + ' - ' + self.nationality

    def _str_(self):
        return self.name + ' - ' + self.nationality


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publisher = models.CharField(max_length=30)
    date = models.DateField()

    def _repr_(self):
        return self.title + ' - ' + self.author.name + ' - ' + self.publisher

    def _str_(self):
        return self.title + ' - ' + self.author.name + ' - ' + self.publisher


'''
a1 = Author(name="Tolstoy", nationality="Russian", date_of_birth=date(1828, 9, 9))
a2 = Author(name="Anthony Doerr", nationality="American", date_of_birth=date(1973, 10, 27))
a3 = Author(name="Aalkdkl", nationality="English", date_of_birth=date(1945, 6, 5))
a4 = Author(name="Sslfjfa", nationality="Irish", date_of_birth=date(1987, 1, 3))
a5 = Author(name="Pafkjfank", nationality="Russian", date_of_birth=date(1647, 2, 19))
a1.save()
a2.save()
a3.save()
a4.save()
a5.save()
b1 = Book(title="Anna Karenina", author=a1, publisher="Little Brown & Company", date=date(1858, 9, 19))
b2 = Book(title="War and Peace", author=a1, publisher="", date=date(1868, 1, 9))
b3 = Book(title="All the light you cannot see", author=a2, publisher="Scribner", date=date(2014, 5, 6))
b4 = Book(title="Asjfkaskjnf", author=a3, publisher="Little Brown & Company", date=date(1967, 1, 1))
b5 = Book(title="Asjfkjs vaks", author=a4, publisher="Publisher X", date=date(1997, 1, 1))
b6 = Book(title="Asjfkdkjsfn fsdkf", author=a5, publisher="Little Brown & Company", date=date(1687, 1, 19))
b7 = Book(title="182jkslf sc saf", author=a4, publisher="Publisher Y", date=date(2001, 1, 19))
b1.save()
b2.save()
b3.save()
b4.save()
b5.save()
b6.save()
b7.save()
'''