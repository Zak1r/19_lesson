# работа с файлами

#open('data.txt', 'w')           # to create file
# file = open('data.txt', 'r+')

# file.write('Zakir')
# file.write('\n')
# file.write('Ikramzhanov')
# file.write('\n')
# file.writelines(['1', '2', '3'])
# file.write('\n')
# file.writelines(['1', '2', '3'])

# file.write('\n')

# file.write('\n')



# file.close()



# file = open('data.txt', 'r+')

# file.write('Zakir')
# file.write('\n')
# file.write('Ikramzhanov')
# file.write('\n')

# file = open('data.txt', 'a')
# file.write('\n')
# file.writelines(['1', '2', '3'])

# file = open('data.txt', 'a+')
# file.write('\n')
# file.writelines(['4', '5', '6'])

# file.close()


    # читаем файл с помощью метода read

# file = open('./data.txt', 'r')
# print(file.read())
# print(file.read(16))
# print(file.readline(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline() == '')

# file = open('./data.txt', 'r')
# lineCounter = 1
# while True:
#     line = file.readline()
#     if lineCounter % 2 == 0:    print(line, end = '')
#     else:   pass

#     if not line: break
#     lineCounter += 1


# file.close()



        # считать lines 
# lines = [1, 3, 6, 8]

# file = open('./data.txt', 'r')

# lineCounter = 1
# while True:
#     line = file.readline()
#     if lineCounter in lines:    print(file.readline())
#     else:   pass
#     lineCounter += 1
#     if line == '': break


# file.close()