

# Parcc- An Automated Parking System

This system is designed to manage the entry and exit of vehicles in a parking lot.
![alt text](logo.png)

## Features

- Reads the number plates of incoming/outgoing vehicles and stores the entry/exit time in a database
- Calculates parking fees based on the duration of time the vehicle was parked
- Provides a user interface(UI) for the admin of the system to view the overall vehicle log file and camera footage
- Provides a user interface(UI) for the user that shows the calculated fee amount and a QR code for digital payment

## Installation

To install and run this system on your local machine, follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/yourusername/automated-parking-management-system.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run parcc.py

## Usage

### Admin Interface

The admin interface provides a dashboard to view the overall database and camera footage. The dashboard includes the following features:

- List of all vehicles parked in the lot, along with their entry/exit times and parking fees
- Real-time camera footage from the parking lot
- Ability to view vehicles in the vehicle log

### User Interface

The user interface allows the user to view the calculated fee amount and make a digital payment using a QR code. The user interface includes the following features:

- Display of the calculated parking fee based on the duration of time the vehicle was parked
- QR code for digital payment

## Technologies Used

- Python
- QtDesigner
- Tesseract 3.0

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b new-feature`)
3. Make changes to the code
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin new-feature`)
6. Create a pull request
