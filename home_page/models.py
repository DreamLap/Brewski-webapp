from django.db import models
from .DBManager import DBManager
# Create your models here.



def create_journal(item):
	DB = DBManager.getInstance()
	Item={
					'JournalID': item,
		}
	DB.saveItem(Item,'Journal')

	
def register_user(username, password):
	DB = DBManager.getInstance()
	Item={
					'Username': username,
					'Password': password
		}
	DB.saveItem(Item,'Users')


