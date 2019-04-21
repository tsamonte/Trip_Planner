#requestplan.py

"""
Uses tkinter to request information from user before displaying it onto
their primary web browser along with a map of their travel plan.
"""

from geopy.geocoders import Nominatim

import tkinter
import mapwriter
import generatePlan




### CLASSES ###

class DontTripUI:
    '''
    Launcher for DontTrip Application
    '''
    
    def __init__(self):
        print('Requesting travel information')

        # main menu window
        self._main_menu = tkinter.Tk()
        self._main_menu.title("Don't Trip!")

        menu = tkinter.Canvas(
            master = self._main_menu,
            width = 500, height = 500, background = '#7779BD')

        menu.grid(
            row = 0, column = 0, columnspan = 5,
            padx = 2, pady = 1,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._main_menu.rowconfigure(0, weight=1)
        self._main_menu.columnconfigure(0, weight=1)

        # options
        #self._destination_entry = self._generate_option(1,
         #       self._main_menu, 'Destination (address)')

        self._city_entry = self._generate_option(1,
                self._main_menu, 'City')
        self._state_entry = self._generate_option(2,
                self._main_menu, 'State')
        self._zipcode_entry = self._generate_option(3,
                self._main_menu, 'Zipcode*')

        # launch the webpage
        title = tkinter.Label(
                master = self._main_menu,
                text = 'Don\'t Trip!\n\nWe got your travel plan.',
                font = ('Impact', 25), background = '#7779BD')

        title.grid(
                row = 0, column = 0, columnspan = 5,
                padx = 15, pady = 15,
                sticky = tkinter.W + tkinter.E)
        
        plan_button = tkinter.Button(
            master = self._main_menu, text = 'Let\'s Go!',
            font = ('Impact', 15),
            command = self._press_plan,
            height = 0, width = 10)

        plan_button.grid(
            row = 1, column = 0, columnspan = 2,
            padx = 0, pady = 0
            )

    def _generate_option(self, option_order_num,
                         master_window, option_text) -> None:
        '''
        Function template for generating option display
        '''
        option_label = tkinter.Label(
            master = master_window, text = option_text,
            font = ('Impact', 15))

        option_label.grid(
            row = option_order_num+1, column = 0, padx = 5, pady = 5,
            sticky = tkinter.W + tkinter.E)

        option_entry = tkinter.Entry(
            master = master_window, width = 20, font = ('Impact', 15))

        option_entry.grid(
            row = option_order_num+1, column = 1, padx = 5, pady = 5,
            sticky = tkinter.W)
            
        return option_entry

    def _press_plan(self) -> None:
        '''
        Launches the plan query into the web browser
        '''
        city = self._city_entry.get()
        state = self._state_entry.get()
        zipcode = self._zipcode_entry.get()
       
        destination = str(city+', '+state+', '+zipcode)
        generatePlan.generatePlan(destination)
        # print(destination)
        #destination = self._destination_entry.get()
        
        try:
            geolocator = Nominatim(user_agent="Dont Trip!")
            location = geolocator.geocode(destination)
            #print("Type: " + str(type(location)))
            if (location == None):
                raise InvalidDestinationError
        except:
            self._error_window = tkinter.Toplevel()
            self._error_window.title('Error')

            error_message = tkinter.Label(
                master = self._error_window,
                text = 'Please enter a valid city and state.',
                font = ('Impact', 15))

            error_message.grid(
                row = 0, column = 0, padx = 10, pady = 10,
                sticky = tkinter.N+tkinter.S+tkinter.W+tkinter.E)

            self._error_window.grab_set()
            self._error_window.wait_window()
            return
        else:
            result = mapwriter.newScript(location.latitude, location.longitude)
            #print(location.latitude, location.longitude)
            mapwriter.writeToFile(result, "travel.html")
            mapwriter.openHTMLInBrowser("travel.html")
        
    def run(self) -> None:
        '''
        Run the DontTrip application
        '''
        self._main_menu.mainloop()

class InvalidDestinationError(Exception):
    ''' Raised when user does not input valid travel destination '''
        

if __name__ == '__main__':
    DT = DontTripUI()
    DT.run()
