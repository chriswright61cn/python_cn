# Write an if statement that checks the ages of
# cinema goers, and display the ticket prices:
# - Child (below age of 18): £8
# - Adult (18+): £10.95
# - Senior (60+): £7.50

age = 66

if age < 18:
    print('Child Ticket: £8')
elif age > 60:
    print('Senior Concession Ticket: £7.50')
else:
    print('Adult Ticket: £10.95')
