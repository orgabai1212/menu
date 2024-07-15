#welcome the user and tell them the path to the recipes folder directory
#tell how many recopes is inside the folder 
# then the user have 6 options to choose 
# [1] - read recipe -choose category (meats,salad,pasta,desert) after choosing category what recipe you want to read ? and show the content of the recipe
# [2] - create recipe -choose category , then create a name , create a content
# [3] - create category- category name? , create the category
# [4] - delete recipe-hoose category (meats,salad,pasta,desert) after choosing category what recipe you want to delet ? delete the recipe
# [5] - delete category- choose category and delete it
# [6] - end the program .
# --------------------------------------------------------------------------------------
# need to be in while loop until the user dont coose 6
# use "system" to clean the console 
import os
import time
import shutil
print("welcome to the menu ")
print("the path to the recipe folder is /home/orgabay/Desktop/python_task/recipes/")
# path_recipes ='/home/orgabay/Desktop/python_task/recipes/'

# how_many_recipes(path_recipes)
def amount_of_recipes(recipes_count):
    total_amount = 0
    for key, value in recipes_count.items():  # Use .items() to get key-value pairs
        print(f"In the '{key}' category, there are {value} recipes.")
        total_amount += value
    print(f"Total number of recipes is {total_amount}.")
    
def list_subdirectories(directory):
    subdirs = []
    try:
        # List only subdirectories
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                subdirs.append(entry)
    except Exception as e:
        print(f"Error accessing {directory}: {e}")
    
    return subdirs

def count_txt_files_in_subdirectories(base_directory, subdirectories):
    recipes_count = {}
    for subdir in subdirectories:
        full_path = os.path.join(base_directory, subdir)
        try:
            if os.path.isdir(full_path):
                txt_count = 0  # Initialize count to 0
                for file in os.listdir(full_path):  # Iterate over each file in the directory
                    if file.endswith('.txt'):  # Check if the file ends with '.txt'
                        txt_count += 1  # Increment count if it's a .txt file
                recipes_count[subdir] = txt_count  # Store the count in the dictionary
            else:
                print(f"Warning: {full_path} is not a directory.")
        except Exception as e:
            print(f"Error accessing {full_path}: {e}")
    
    return recipes_count

def invalid_option(num):
    while num <'0' or num >'9':
        print("wrong char!")
        num=input("please enter a number")
    num = int(num)  # Convert num to an integer 
    while num <0 or num > 9:
        print(" invalid option please choose between 1-6")
        num=input("enter a number")

    
    if num < 1 or num > 6:
        return False  # Return False if num is invalid (outside the range 1 to 6)
    else:
        return True  # Return True  if num is valid (within the range 1 to 6)
    
def choose_option():
    print("you have a 6 options")
    print("[1] - read recipe")
    print("[2] - create recipe")
    print("[3] - create category")
    print("[4] - delete recipe")
    print("[5] - delete category")
    print("[6] - end the program")
    print(" please choose the number of the option you want")

def read_recipe(directory,category):
    category=str(category)+"/"
    counter=0
    recipe_list=[]
    full_path = os.path.join(directory,category)
    for file in os.listdir(full_path):
        if file.endswith('.txt'):
            recipe_list.append(file)
            counter+=1
    if counter ==0:
        print("no recipes in this category")
    else :
        clean_list=[]

        for recipe in recipe_list:
            temp=recipe
            clean_list.append(temp.replace(".txt",""))
            print(temp.replace(".txt",""))
        print("")
        choosen_recipe=input("please choose the resipe ")
        while choosen_recipe not in clean_list:
            print("no such recipe please choose recipe from the list ")
            choosen_recipe=input("please choose the resipe ")
        file_path=str(directory)+str(category)+str(choosen_recipe)+".txt"
        file=open(file_path,'r')
        print(file.read())

def create_category(dir,subdir):
    subdirs = []
    for entry in os.listdir(dir):
        full_path = os.path.join(dir, entry)
        if os.path.isdir(full_path):
            subdirs.append(entry)
    while subdir in subdirs :
        print("the category allredy exist please \n please enter a new category ")
        subdir =input("enter a new category ")
    full_path=os.path.join(dir,subdir)
    os.makedirs(full_path)
    print(f"category {subdir} added ")

def create_recipe (directory,category,recipe_name):
    recipes_list=[]
    category=str(category)+"/"
    file_name=str(recipe_name)+".txt"
    sub_path=os.path.join(directory,category)
    file_path=os.path.join(directory,category,file_name)
    #checking if the file alredy exist
    for file in os.listdir(sub_path):  # Iterate over each file in the directory
        if file.endswith('.txt'):  # Check if the file ends with '.txt'
            recipes_list.append(file)
    while file_name in recipes_list:
        print("this recipe allready exist")
        recipe_name=input("please enter recipe name ")
        file_name=str(recipe_name)+".txt"
    new_file=open(file_path,'a')
    print("Enter text to write to the file (type 'exit' to finish):")
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break
        new_file.write(user_input + '\n')
    print(f"recipe {recipe_name} created ")
    new_file.close

def delete_recipe(directory,category):
    category=str(category)+"/"
    counter=0
    recipe_list=[]
    full_path = os.path.join(directory,category)
    for file in os.listdir(full_path):
        if file.endswith('.txt'):
            recipe_list.append(file)
            counter+=1
    if counter ==0:
        print("no recipes in this category")
    else :
        clean_list=[]

        for recipe in recipe_list:
            temp=recipe
            clean_list.append(temp.replace(".txt",""))
            print(temp.replace(".txt",""))
        print("")
        choosen_recipe=input("please choose the resipe you wish to delete ")
        while choosen_recipe not in clean_list:
            print("no such recipe please choose recipe from the list ")
            choosen_recipe=input("please choose the resipe ")
        file_path=str(directory)+str(category)+str(choosen_recipe)+".txt"
        os.remove(file_path)
        print(f"the recipe {choosen_recipe} deleted")

def delete_category(dir,subdir):
    subdirs = []
    for entry in os.listdir(dir):
        full_path = os.path.join(dir, entry)
        if os.path.isdir(full_path):
            subdirs.append(entry)
    while subdir not in subdirs :
        print("the category dosent exist please \n please enter a category you want to delete ")
        subdir =input("enter a category ")
    full_path=os.path.join(dir,subdir)
    shutil.rmtree(os.path.join(dir,subdir))
    print(f"Category '{subdir}' and all its contents have been deleted.")    






        




    




if __name__ == "__main__":
    print("welcome to the menu ")
    print("the path to the recipe folder is /home/orgabay/Desktop/python_task/recipes/")
    # Replace 'your_directory_path' with the path to the directory you want to check
    directory = '/home/orgabay/Desktop/python_task/recipes/'
    subdirectories = list_subdirectories(directory)
    recipes_count = count_txt_files_in_subdirectories(directory, subdirectories)
    amount_of_recipes(recipes_count)
    time.sleep(4)
    #os.system('clear')
    choose_option()
    option=(input("choose number "))
    
    while option !=6:
        if option == 1:
            print(" the categorys are ")
            for a in subdirectories:
                print(a)
            category=input("please choose a category of the recipe you wish to read  ")
            while category not in subdirectories:
                print("invalid category!")
                category=input("please choose a category ")
                print()
            read_recipe(directory, category)
            print("choose another option")
            time.sleep(3)
            os.system('clear')
        
        if option == 2:
            print(" the categorys are ")
            for a in subdirectories:
                print(a)
            category=input("please choose a category of the recipe you want to creat ")
            while category not in subdirectories:
                print("invalid category!")
                category=input("please choose a category ")
                print()
            recipe_name=input("please enter the name of the recipe ")
            create_recipe(directory,category,recipe_name)
            time.sleep(3)
            os.system('clear')

        if option == 3:
            print(" the categorys are ")
            for a in subdirectories:
                print(a)
            category=input("please enter a category you want to creat ")
            create_category(directory,category)
            subdirectories = list_subdirectories(directory)
            time.sleep(3)
            os.system('clear')
        
        if option == 4:
            print(" the categorys are ")
            for a in subdirectories:
                print(a)
            category=input("please choose a category of the recipe you wish to delete  ")
            while category not in subdirectories:
                print("invalid category!")
                category=input("please choose a category ")
                print()
            delete_recipe(directory, category)
            print("choose another option")
            time.sleep(3)
            os.system('clear')

        if option == 5:
            print(" the categorys are ")
            for a in subdirectories:
                print(a)
            category=input("please choose a category you wish to delete  ")
            delete_category(directory,category)
            print("choose another option")
            subdirectories = list_subdirectories(directory)
            time.sleep(3)
            os.system('clear')
        
        










        
        choose_option()
        option=int(input("choose number "))
            


    print("thank you the progran end")






        

        


