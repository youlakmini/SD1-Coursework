#I declare that my work contains no examples of misconduct, such as plaigiarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student_ID: 20230200 / w2051583
#Date: 13/12/2023

from graphics import* 

#Initializing the variables to zero
progress = 0
exclude = 0
trailer = 0
retriever = 0

conclude = 'y'
total_outcomes = progress + exclude + retriever + trailer

#Function to define credit and credit type
def audit_range(credit, credit_type):
    while credit not in range(0, 140, 20):
        print('Out of range')
        credit = int(input(f'Enter your {credit_type}: '))
    return credit

while conclude.lower()=='y':
    try:
        credit_pass = int(input('Please enter your credits at pass: '))
        credit_type = 'credit pass'
        credit_pass = audit_range(credit_pass, credit_type)

        credit_defer = int(input('Please enter your credit at defer: '))
        credit_type = 'credits defer'
        credit_defer = audit_range(credit_defer, credit_type)

        credit_fail = int(input('Please enter your credit at fail: '))
        credit_type = 'credits fail'
        credit_fail = audit_range(credit_fail, credit_type)
        
        # Update counts based on the entered data
        if credit_pass == 120:
            print('Progress')
            progress += 1
        elif (credit_pass == 100 and credit_defer == 20 and credit_fail == 0) or (credit_pass == 100 and credit_defer == 0 and credit_fail == 20):
            print('Progress-module trailer')
            trailer += 1
        elif credit_fail >= 80 and credit_pass <= 40:
            print('Exclude')
            exclude += 1
        else:
            print('Do not progress-module retriever')
            retriever += 1

            
            
        conclude = input('Would you like to enter another set of data? (yes/quit): ')
        assessment_marks = credit_pass + credit_defer + credit_fail

        if assessment_marks != 120:
            print('Total incorrect')
            print('Invalid credits')
            continue
       

        # Add total count
        total_outcomes += 1
        
        if conclude.lower() == 'q':
            break
        else:
            print('Enter other marks')

        
    except ValueError:
        print('Integer required')


#Anon, (n.d.). Available at: https://chat.openai.com/c/aa9569b3-d411-4a58-9239-5fb6743b6ad8.
# Function to display histogram
def display_histogram(data):
    num_categories = len(data)
    win = GraphWin("Histogram Results", 400, 500)
    win.setBackground("mint cream")#set background color

    # Draw bars 
    for i, (label, count) in enumerate(data, start=1):
        bar_height = count * 20  # Scale the bars
        bar = Rectangle(Point(i * 80 - 20, 300), Point(i * 80 + 20, 300 - bar_height))
        bar.setFill("pink")
        bar.draw(win)

    

        # Label the x-axis
        x_label = Text(Point((num_categories + 1) * 40, 410), 'Progression Outcome')
        x_label.draw(win)

    # Draw x-axis line
    pt1 = Point(40, 300)
    pt2 = Point(570, 300)
    line = Line(pt1, pt2)
    line.setOutline('black')
    line.draw(win)

     # Label the bars with counts
    bar_label = Text(Point(i * 80, 400 - bar_height - 5), str(count))
    bar_label.setTextColor('black')
    bar_label.setSize(10)
    bar_label.draw(win)

    txt_progress= Text(Point(100,310), 'Progress')
    txt_progress.draw(win)

    txt_exclude=Text(Point(170,310),'Exclude')
    txt_exclude.draw(win)

    txt_trailer=Text(Point(240,310),'Trailer')
    txt_trailer.draw(win)

    txt_retriever=Text(Point(310,310),'Retriever')
    txt_retriever.draw(win)

    # Display count above each bar
    for i, (label, count) in enumerate(data, start=1):
        count_label = Text(Point(i * 80, 300 - bar_height - 30), str(count))
        count_label.setTextColor('black')
        count_label.setSize(10)
        count_label.setStyle('bold')
        count_label.draw(win)

     
    # Set the main heading with the total number outcomes
    heading_text = f'Histogram Results\nTotal Outcomes: {total_outcomes}'
    heading = Text(Point((num_categories + 1) * 40, 30), heading_text)
    heading.setTextColor('grey')
    heading.setSize(14)
    heading.setStyle('bold')
    heading.setFace('helvetica')
    heading.draw(win)

    win.getMouse()
    win.close()

# Prepare data for histogram with customized labels
histogram_data = [
    ("Progress", progress),
    ("Exclude", exclude),
    ("Trailer", trailer),
    ("Retriever", retriever),
]

# Display the histogram using user-defined functions
display_histogram(histogram_data)

