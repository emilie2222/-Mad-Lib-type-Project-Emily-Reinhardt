"""The Ugly Duckling-Mad libs alternate program by Emily Reinhardt """


number_1 = input("Choose a number: ")
color_1 = input("Choose a color: ")
adjective_1 = input("Choose and adjective (Description word; ex: ugly): ")
noise_1 = input("Choose a noise: ")
positive_description = input("Choose a positive description: ")
color_2 = input("Choose a color: ")
Dramatic_noise = input("Choose a dramatic noise: ")
Shocked_disgusted_expression = input("Enter a shocked/disgusted expression. ")
mean_expression_1 = input("Choose a mean expression: ")
mean_expression_2 = input("Choose another mean expression: ")
mean_expression_3 = input("Choose another mean expression: ")
mean_expression_4 = input("Choose another mean expression: ")
mean_expression_5 = input("Choose another mean expression: ")
animal_1 =input("Choose an animal: ")
animal_2 =input("choose another animal: ")
animal_3 =input("choose another animal: ")
animal_4 =input("choose another animal: ")
yes_no_responce = input("Choose a yes/no responce: ")
facial_expression = input("Choose a facial_ expression: ")
verb =input("Choose a past tense verb (Action word; ex:Ran,swam,etc.): ")



mad_libs = "Mother Duck lived on a farm. In her nest, she had " + number_1 + " " + color_1 + " eggs and one \n"
mad_libs += adjective_1 + " egg. One day, the " + number_1 + " " + color_1 + " eggs started to crack.\n"
mad_libs += noise_1 + ", " + noise_1 + ", " + noise_1 + "! " + number_1 + " " + positive_description + ",\n"
mad_libs += color_2 + " baby ducklings came out. Then the " + adjective_1 + " egg started to crack. \n"
mad_libs += Dramatic_noise +  ", " + Dramatic_noise + ", " + Dramatic_noise + "!" + " One big, ugly duckling\n"
mad_libs += "came out. " + Shocked_disgusted_expression + " thought Mother Duck. Nobody wanted him. \n"
mad_libs += mean_expression_1 + " said his brothers and sisters. ‘You’re ugly!’ The ugly duckling was sad.\n"
mad_libs += "So he went to find some new friends."+ mean_expression_2 + " said the " + animal_1 + ". \n"
mad_libs += mean_expression_3 + " said the " + animal_2 + ". " + mean_expression_4 + " said the \n"
mad_libs += animal_3 + ". " + mean_expression_5 + " said the " + animal_4 + ". No one wanted to be his\n"
mad_libs += "friend. It started to get cold. It started to snow! The ugly duckling found an empty barn and \n"
mad_libs += "lived there. He was cold, sad and alone. Then spring came. The ugly duckling left the barn and went \n"
mad_libs += "back to the pond. He was very thirsty and put his beak into the water. He saw a stunning , white bird! \n"
mad_libs += " ‘Wow!’ he said. ‘Who’s that?’ ‘It’s you,’ said another beautiful, white bird.‘Me? But I’m an ugly \n"
mad_libs += " duckling.’‘Not any more. You’re a beautiful swan, like me. Do you want to be my friend?’ \n"
mad_libs += yes_no_responce + " he " + facial_expression + " . All the other animals watched as the two swans " + verb + "." 


input("Press enter to get your mad libs results")

print("Printing your mad libs......")
print(mad_libs)
