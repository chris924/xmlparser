import xml.etree.ElementTree as Xet

def parse(user_inputs, file_name):
    cols = user_inputs  

    tree = Xet.parse(file_name + '.xml') 
    root = tree.getroot()

   
    with open(file_name + '_output.csv', 'w') as csv_file:
        
        csv_file.write(','.join(cols) + '\n')

        for element in root.iter():
            row_data = []
            for input_tag in user_inputs:
                if input_tag in element.tag:  
                    row_data.append(element.text if element.text else '')  
            if row_data: 
                
                csv_file.write(','.join(row_data) + '\n')