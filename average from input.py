def main():

    try:
        total = 0.0
        count = 0

        infile = open('numbers.txt', 'r')
        numbers = infile.read()
        infile.close()
        
        for line in infile:
            number = float(line)
            count += 1
            total += number
            average = total/count
            print('The average number is:', format(average))
            infile.close()

    except ValueError:
        print('File must only have numbers. Please try again.')

    except IOError:
        print('File could not open. Please try again')

if __name__ == '__main__':
    main()
