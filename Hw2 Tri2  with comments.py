#Sasha G and Manar A
#CSCE 160 
#Prof. Kim 
#Feb, 8th 2024 

import math



#Find Area 
def getArea(Side1, Side2, angle): 
     area = (Side1 * Side2 * math.sin(angle))/2 
     return area; 
 
#Convert angles to degress 
def convertRad(rad):
    deg = rad * (180 / math.pi)
    return deg


#Find Angles and Radians
def getAngl(Side1, Side2, Side3):
     numerator = (Side1 **2) + (Side2 **2) - (Side3 ** 2);
     denominator = (2 * Side1 * Side2)
     angle =numerator/denominator; 
     angle = math.acos(angle)
     return angle

#Valid Triangle 

def validTri(Side1, Side2, Side3): 
    
     # If the sides are not in increasing order,
     # rearrange them so that they are in increasing order.
     
     # If Side2 is the largest,
     # reassign each variable so that they're in increasing order.
     if(Side2 > Side3 and Side2 > Side1):
        SideBig = Side3;
        Side3 = Side2;
        Side2 = SideBig;
            
        if(Side2 < Side1):
            SideSmall = Side2;
            Side1 = Side2; 
            Side2 = SideSmall; 
            
     # If Side1 is the largest,
     # reassign each variable so that they're in increasing order.
     elif(Side1 > Side3 and Side1 > Side2):
        SideBigBig =Side3;
        Side3 = Side1;
        Side1 = SideBigBig;
    
        if(Side1 < Side2):
            SideSmallest = Side1;
            Side1 = Side2; 
            Side1 = SideSmallest; 
            
     # We've guaranteed above that the sides are in increasing order.
     # Now we can check if the sides make a valid triangle.
     elif(Side3 > Side2 and Side3 > Side1 and Side1 + Side2 > Side3):
        
        if (Side2 == Side1):
            return True
                        
        elif (Side2 != Side1):
            return True
                        
        elif(Side1 == Side2 == Side3):
            return True
                    
        else:
            return False 


#--------------------------------------------------------------------------------

while(True):
    print("Program Modes: \n (1) Enter Sides \n (2) Quit");
    menu = input("Enter Your number choice: ");
    print("-------------------------------------------------------------------------")
    menu = float(menu);
    
    
    # If user picks 1 
    
    if(menu==1):
        
        #Ask for all sides 
        Side1 = float( input("Enter the first side of the triangle: ") );
        Side2 = float( input("Enter the second side of the trangle: ") );
        Side3 = float( input("Enter the last side of the triangle: ") );
        print("-------------------------------------------------------------------------")
        
        # We determine if the triangle is valid ONCE and save it to variable a.
        a = validTri(Side1, Side2, Side3); 
        
        # Make the user pick proper side lengths.
        if(a == False):
            print("Ya numbers are lame, pick new ones");
            continue; 
       
        # Grab all the angles and convert them from radians to degrees.
        # For Angl1, we will wait until after we calculate area to convert it to degrees.
        Angl1 = getAngl(Side2, Side3, Side1);
        Angl2 = convertRad(getAngl(Side3, Side1, Side2));
        Angl3 = convertRad(getAngl(Side1, Side2, Side3));
        
        # Calculate area.
        Area= getArea(Side2, Side3, Angl1); 
        
        # Convert Angl1 from radians to degrees.
        Angl1 = convertRad(getAngl(Side2, Side3, Side1));
        
        # Print out everything: area and angles 1, 2, 3
        print("The Area is: ", Area); 
        print("-------------------------------------------------------------------------")
        print("The Angles are: ", Angl1, Angl2, Angl3);
        print("-------------------------------------------------------------------------")
        print("WHOOOO UR DONEEE");
        print("-------------------------------------------------------------------------")
    
    # Done with the program. Say bye bye
    elif(menu==2):
        print("Bye Bye (>0<)"); 
        break
    
    # Make the user pick a proper menu option
    else: 
        print("You have picked an invalid option, avoid negatives!"); 
        
        
            