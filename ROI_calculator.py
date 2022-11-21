class Roi_calculator():
    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.total_investment = 0

    def income(self): # income box
        rental_income = input('rental income')
        laundry = input('laundry')
        storage = input('storage')
        misc = input('misc')
        self.total_income = sum(rental_income, laundry, storage, misc)
        return f'{self.total_income} is you Total Monthly Income'

    def expenses(self): #expenses box
        tax = input('taxes')
        insurance = input('insurance')
        util = [] # might turn into a dictionary with the key = item and value = cost
        electric = util.append(input('electric'))
        water = util.append(input('water'))
        sewer = util.append(input('sewer'))
        garbage = util.append(input('garbage'))
        gas = util.append(input('gas'))
        utilities = sum(util)
        hoa_fees = input('hoa fees')
        lawn_snow_care = input('lawn / snow care')
        vacancy = input('vacancy')
        repairs = input('repairs')
        capex = input('capital expenditures')
        property_management = input('property management')
        mortgage = input('mortgage')
        self.total_expenses = sum(tax, insurance, utilities, hoa_fees, lawn_snow_care, vacancy, repairs, capex, property_management, mortgage)
        return f'{self.total_expenses} is your Total Monthly Expenses'

    def cash_flow(self):
        self.total_cash_flow = self.total_income - self.total_expenses

    def investment(self):
        down_payment = input('down payment')
        closing_costs = input('closing costs')
        rehab_budget = input('rehab budget')
        misc_other = input('misc other')
        self.total_investment = sum(down_payment, closing_costs, rehab_budget, misc_other)

    def roi(self):
        annual_cash_flow = self.total_investment * 12
        cash_on_cash_roi = round((annual_cash_flow / self.total_investment) * 100)
        return f'{cash_on_cash_roi} is your Cash on Cash ROI.'
    
    def runner(self):
        while True:
            user_ = input('Please fill in the following sections to the best of your ability. [S] to get started or [Q] to quit.').lower()
            if user_ == 's':
                self.income
            elif user_ == 'q':
                break
            else:
                'I\'m sorry. That is an invail input. Please try again.'

user_ = Roi_calculator()

user_.runner()
