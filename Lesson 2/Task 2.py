#обычный принт
print ('Hello, Beetroot Academy!')
#конкатенация двух строк
print ('Hello, ' + 'Beetroot Academy!')
#использование разделителя запятая с пробелом
print ('Hello', 'Beetroot Academy!', sep=', ')
#использование  параметра end для игнорирования знака переноса строки
print ('Hello,', 'Beetroot Academy!', end=' ')
print ('Hello,', 'Little Beetroots!')
#использование  параметра end для 3 переносов строки
print ('Hello,', 'Beetroot Academy!', end='\n\n\n')
print ('Hello,', 'Little Beetroots!')
#использование  параметра end для окончания строки нужным знаком
print ('Hello,', 'Beetroot Academy', end='!')
#предыдущий пример не переносит строку, поэтому тут костыль для читаемости вывода
print ('\n')
#использование  параметра sep и end вместе
print ('Hello', 'Beetroot Academy', sep=', ', end='!')


