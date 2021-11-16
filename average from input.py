def main():

    try:
        total = 0.0
        count = 0

        infile = open('numbers.txt', 'r')
        numbers = infile.readline()
        
        while numbers != '':
            number = float(numbers)
            print(number)
            count += 1
            total += number
            average = total/count
            numbers = infile.readline()
        print('The average number is:', format(average))
        infile.close()

    except ValueError:
        print('File must only have numbers. Please try again.')

    except IOError:
        print('File could not open. Please try again')


if __name__ == '__main__':
    main()
