#image manipulation
from PIL import Image
import pathlib
#random value generation
import random
#time for seeding random generation
import time
#start timing execution of code
begin_time = time.time()
# Set quantity of traits to be used
background_quantity = 0
background_back_extra_quantity = 0
back_hair_quantity = 10
right_arm_quantity = 5
outfit_quantity = 0
base_quantity = 6
eyes_quantity = 5
front_hair_quantity = 6
left_arm_quantity = 5
face_extra_quantity = 0
background_front_extra_quantity = 0

#filename list to be filled with each trait and value for final file name to be saved to disk and ensure no duplicates
filename_list = []
#global variable for linked traits
background_value = 0
outfit_value = 0
hair_value = 0
#receive input for amount of images to generate
generation_quantity = int(input("Enter amount of images you want to create:"))

#image combination function for each trait - file prefix of trait file, amount of traits, whether it is linked and to what, if its the first instance of that linked trait, list of weight values for each trait rarity
def image_paste(prefix,quantity,link = 'No', initial = 0, weight = []):
    #seed number generation with current time
    random.seed(time.time())
    #if a trait is independent or the first instance of the link, will generate a random value to be used to determine which trait is used
    if ((link == 'No') or (link != 'No' and initial == 1)):
        #if there is no given weight values, picks trait with equal chances
        if weight == []:
            temp_value = random.randint(1, 10000000) % quantity + 1
        else:
            #else sums up weights, forms a list of values based on weights for random value to be compared against
            weight_manipulated = []
            for i in range(0,len(weight)):
                sum += weight[i]
                temp_weight += weight[i]
                weight_manipulated[i] = temp_weight
            #generates a random value between 0 and sum of weights -1
            random_value = random.rantint(1, 1000000) % sum
            #iterates through list of weight values, comparing generated value to list until it falls within a range, sets trait value to that
            for weight_manipulated_index in range(0,len(weight_manipulated)):
                 if random_value < weight_manipulated[weight_manipulated_index]:
                     temp_value = weight_manipulated_index + 1
    #if trait is linked, will either set that trait value as the generated value if it is the initial instance, or will set trait value to previously determined linked trait value
    if link != 'No':
        if link == "background":
             if initial == 1:
                print("link background")
                background_value = temp_value
             else:
                temp_value = background_value
        elif link == "outfit":
            if initial == 1:
                print("link outfit")
                outfit_value = temp_value
            else:
                temp_value = outfit_value
        elif link == "hair":
            if initial == 1:
                print("link hair")
                hair_value = temp_value
            else:
                temp_value = hair_value

    #creates filename based on trait and random value
    temp_filename= prefix + str(temp_value)
    #puts together file path to be opened and added to image
    temp_path = "Images\\" + prefix + str(temp_value) + '.png'
    #adds filename to list to be combined all together later
    filename_list.append(temp_filename)
    #opens specified image and pastes layer onto working image
    temp = Image.open(temp_path).convert("RGBA")
    image.paste(temp,(0,0),temp)

#loops for however many images were specified to be created
for generation_quantity in range(0,generation_quantity):
    #begins timing generation of image
    generation_begin_time = time.time()
    #seeds random generation
    random.seed(time.time())
    #generates random value for base
    base_value = random.randint(1,1000000) % base_quantity +1
    #creates filename and path to be referred to
    base_filename = "BASE_" + str(base_value)
    base_path = "Images\\BASE_" + str(base_value) + '.png'
    #opens image
    image = Image.open(base_path).convert("RGBA")

    #runs image_paste function for each layer
    image_paste("Back_H_",back_hair_quantity)
    image_paste("Brazoder_",right_arm_quantity)
    image_paste("BASEyes_",eyes_quantity)
    image_paste("Brazoizq_",left_arm_quantity)
    image_paste("Front_H_",front_hair_quantity)

    #Create final filename to be saved
    raw_directory = "Images\\Done\\"
    outfile = raw_directory + str(base_filename)
    for i in range(0,len(filename_list)):
        outfile += filename_list[i]
    outfile += '.png'
    print(outfile)
    generation_end_time = time.time()
    print("Generation loop time:", generation_end_time - generation_begin_time)
    file_write_begin = time.time()
    image.save(outfile)
    file_write_end = time.time()
    print("File write time:", file_write_end -  file_write_begin )
    print(filename_list)
    filename_list = []

#Time Execution
end_time = time.time()
print("Total run time: ", end_time-begin_time)




