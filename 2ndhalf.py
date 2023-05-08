    def leaveGarage(self, ticket_number):
        if ticket_number is not None and ticket_number in self.currentTicket and self.currentTicket[ticket_number]['paid']:
            print("Thank you, have a nice day!")
            parking_space = self.currentTicket[ticket_number]['parking_space']
            self.parkingSpaces.append(parking_space)
            self.tickets.append(ticket_number)
            del self.currentTicket[ticket_number]
        else:
            print("Ticket not paid.")
            payment = input("Please make a payment to exit the parking lot: ")
            if payment == "payment":
                self.currentTicket[ticket_number]['paid'] = True
                print("Payment successful. You may now leave the garage. Thank you, have a nice day!")
                parking_space = self.currentTicket[ticket_number]['parking_space']
                self.parkingSpaces.append(parking_space)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                print("Payment not received. YOU ARE TRAPPED HERE MUAHAHAH!")


# Create an instance of ParkingGarage
garage = ParkingGarage()

# Take a ticket
garage.takeTicket()

# Pay for the ticket and get the ticket number
ticket_number = garage.payForParking()

# Leave the garage using the ticket number
garage.leaveGarage(ticket_number)