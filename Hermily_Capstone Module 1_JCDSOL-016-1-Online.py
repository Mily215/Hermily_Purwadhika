#Employee Database (ver02)
#Stakeholder/users: Human Resource Department and Employer

#Columns are: ['Employee ID', 'Nama Karyawan','Departemen','Gaji','Grade']

empDB = [
    {
        'Employee ID':'PWR01',
        'Employee Name': 'Hermily',
        'Department': 'Marketing',
        'Salary':8000000,
        'Grade':4
     },
    {
        'Employee ID':'PWR02',
        'Employee Name': 'Trisna',
        'Department': 'Marketing',
        'Salary':8500000,
        'Grade':3
     },
    {
        'Employee ID':'PWR03',
        'Employee Name': 'Roni',
        'Department': 'Security',
        'Salary':6500000,
        'Grade':7
    },
    {
        'Employee ID':'PWR04',
        'Employee Name': 'Riky',
        'Department': 'Management',
        'Salary':15000000,
        'Grade':9
    },
    {
        'Employee ID':'PWR05',
        'Employee Name': 'Elena',
        'Department': 'Intern',
        'Salary':5000000,
        'Grade':1
    }
]

empSelect = []

#Functions:

# Show Emp Database #OK
def showEmpDB():
    print('Employee Directory\n')
    print('Employee ID  \t| Employee Name\t| Department\t\t| Salary\t| Grade')
    for i in range(len(empDB)) :
        print(f"{empDB[i]['Employee ID']}\t\t| {empDB[i]['Employee Name']}  \t| {empDB[i]['Department']}\t\t| {empDB[i]['Salary']} \t| {empDB[i]['Grade']}")

#Create Function #OK
def empAdd(): 
    global empDB
    empID = input('Insert Employee ID:  ')
    for emp in empDB:
        if emp['Employee ID'] == empID:
            print('Duplicate data. An employee with the same Employee ID already exist.')
            return
    empName = (input('Insert Employee Name: '))
    empDept = (input('Insert Employee Department:   '))
    empSalary = int(input('Insert Employee Salary:  '))
    empGr = int(input('Insert Employee Grade:   '))
    newEmp = {
        'Employee ID': empID,
        'Employee Name': empName,
        'Department': empDept,
        'Salary': empSalary,
        'Grade': empGr
    }
    duplicateFound = False
    for emp in empDB:
        if (emp['Employee Name']== empName and
             emp['Department']== empDept and
            emp['Salary']== empSalary and
            emp['Grade']== empGr):
            userConfirmation = input('Duplicate data. An employee with the exact same data already exist. Are you sure you want to add this employee? (Y/N):    ')
            duplicateFound = True
            if userConfirmation.upper() == 'Y':
                empDB.append(newEmp) 
                print('New employee successfully added.')
                showEmpDB()
                if userConfirmation.upper() != 'Y':
                    print('Employee Addition cancelled.')
            break
               
               
    if not duplicateFound:     
        userConfirmation = input('Do you want to save this employee as a new employee? (Y/N):   ')
        if userConfirmation.upper() == 'Y':
            empDB.append(newEmp) 
            print('New employee data successfully added.')
            showEmpDB()
        elif userConfirmation.upper() == 'N':
            print('Employee Addition cancelled.')
            
        else:
            print('Employee addition cancelled. Please confirm the data addition with \'Y\'.')

# Update Function #OK
def updateEmp():
    empid_toupdate = input('Enter the employee ID of the dta you want to update:    ') 
    global empDB
    Found = False
    for emp in empDB:
        if emp['Employee ID'] == empid_toupdate:
            print(f"Employee ID\t: {emp['Employee ID']}\nEmployee Name\t: {emp['Employee Name']}\nDepartment\t: {emp['Department']}\nSalary\t\t: {emp['Salary']}\nGrade\t\t: {emp['Grade']}")
            userConfirmation = input('Data found. Continue data update? (Type Y to confirm):    ')
            if userConfirmation == 'Y':
                    keyUpdate = input('What data of this employee do you want to update? Ans:   ')
                    if keyUpdate == 'Salary':
                        newSalary = int(input('Enter new Salary for this employee:  '))
                        emp['Salary'] = newSalary
                        print(f'Salary for {emp["Employee Name"]} has been updated to {newSalary}')
                        showEmpDB()
                        return
                    elif keyUpdate == 'Department':
                        newDept = input('Enter new Department for this employee:    ')
                        emp['Department'] = newDept
                        print(f'{emp["Employee Name"]} is now in the {newDept} department.')
                        showEmpDB()
                        return
                    elif keyUpdate == 'Grade':
                        newGrade = int(input('Enter new Grade for this employee:    '))
                        emp['Grade'] = newGrade
                        print(f'{emp["Employee Name"]} is {newGrade} Grade.')
                        showEmpDB()   
                        return
                    else:
                        print('You can only update the Salary, Department, and Grade of an employee. Employee ID and Name can not be changed')
                        return
            elif userConfirmation != 'Y':
                print('Data update cancelled')
                return
            Found = True
    if not Found:
        print('Employee not found. Please re-enter the correct employee ID')
        updateEmp()
        return           

# Delete Function #OK
def delEmp():
    global empDB
    empDel_id = input('Which employee do you want to delete? (Enter Employee ID):   ')
    for emp in empDB:
        if emp['Employee ID'] == empDel_id:
            userConfirmation = input('Data found. Continue data deletion? (Type Y to confirm):  ')
            if userConfirmation == 'Y':   
                empDB.remove(emp)
                print(f'This employee has been successfully deleted from the directory: {emp["Employee Name"]} (Employee ID: {empDel_id}).')
                showEmpDB()
                return
            elif userConfirmation != 'Y':
                    print('Data deletion cancelled')
                    return   
    if empDel_id not in empDB:
        print('Employee not found')

#Read/Search Function #OK
def dataSearch(empDB):
    empSearch = input('Which employee data are you looking for? (Enter employee ID): ')
    for emp in empDB:
        if emp['Employee ID'] == empSearch:
            print("Employee found")
            print(f"Employee ID\t: {emp['Employee ID']}\nEmployee Name\t: {emp['Employee Name']}\nDepartment\t: {emp['Department']}\nSalary\t\t:{emp['Salary']}\nGrade\t\t:{emp['Grade']}")
            return
        elif emp['Employee Name'] == empSearch:
            print("Employee found")
            print(f"Employee ID\t: {emp['Employee ID']}\nEmployee Name\t: {emp['Employee Name']}\nDepartment\t: {emp['Department']}\nSalary\t\t:{emp['Salary']}\nGrade\t\t:{emp['Grade']}")
            return

    if empSearch not in empDB:
        print('Employee not found')
        dataSearch(empDB)
        return

while True :
    menuOptions = input('''
        Employee Directory of PeopleFirst Company.

        Menu Options :\n
        1. Show All Employee Data\n
        2. Search an Employee's Data\n
        3. Add New Employee\n
        4. Update Employee Salary\n
        5. Delete an Employee\n
        6. Exit Program\n
        \n
        Enter the menu option you want to run :     ''')

    if(menuOptions == '1') :
        showEmpDB()
    elif(menuOptions == '2') :
        dataSearch(empDB)
    elif(menuOptions == '3') :
        empAdd()
    elif(menuOptions == '4') :
        updateEmp()
    elif(menuOptions == '5') :
        delEmp()
    elif(menuOptions == '6') :
        break
    else:
        print('Please choose one of the menu options available')
