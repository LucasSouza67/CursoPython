# exibe uma mensagem de feliz ano novo caso seja primeiro de Janeiro
from datetime import datetime

dia = datetime.today().strftime('%d/%m/%Y')

if dia == '01/01/2024':
  print('Feliz ano novo 🎉🎆')
else:
  print('Ainda não é ano novo 🎉🎆')
