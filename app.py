"""The Ugly Duckling-Mad libs alternate program by Emily Reinhardt """


"""
Mother Duck lived on a farm. In her nest, she had (number_1) (color_1) eggs
and one (adjective_1) egg. One day, the (Number_1)(color_1) eggs started to crack.
(noise_1), (noise_1), (noise_1)! (Number_1) (positive description), (color) baby ducklings came out.
Then the (adjective_1) egg started to crack. (Dramatic noise), (Dramatic noise), (Dramatic noise)! One big,
ugly duckling came out. ‘(Shocked/disgusted expression)’ thought Mother Duck.
Nobody wanted him. ‘(Mean expression 1)’ said his brothers and sisters. ‘You’re ugly!’
The ugly duckling was sad. So he went to find some new friends.
‘(Mean expression 2)!’ said the (animal 1).
‘((Mean expression 3)!’ said the (Animal 2)).
‘((Mean expression  4)!’ said the (Animal 3).
‘( (Mean expression 5)’ said the (Animal 4).
No one wanted to be his friend. It started to get cold. It started to snow! The ugly duckling
found an empty barn and lived there. He was cold, sad and alone.
Then spring came. The ugly duckling left the barn and went back to the pond. He was very
thirsty and put his beak into the water. He saw a stunning , white bird! ‘Wow!’ he said. ‘Who’s
that?’
‘It’s you,’ said another beautiful, white bird.
‘Me? But I’m an ugly duckling.’
‘Not any more. You’re a beautiful swan, like me. Do you want to be my friend?’
‘(yes/no responce)’ he (facial expression).
All the other animals watched as the two swans (ed verb).
"""

number_1 = input("Choose a number: ")
color_1 = input("Choose a color: ")
adjective_1 = input("Choose and adjective (Description word; ex: ugly): ")
noise_1 = input("Choose a noise: ")
positive_description = input("Choose a positive description: ")
color_2 = input("Choose a color: ")
Dramatic_noise = ("Choose a dramatic noise: ")
Shocked_disgusted_expression = ("Enter a shocked/disgusted expression. ")
mean_expression_1 = ("Choose a mean expression: ")
mean_expression_2 = ("Choose another mean expression: ")
mean_expression_3 = ("Choose another mean expression: ")
mean_expression_4 = ("Choose another mean expression: ")
mean_expression_5 = ("Choose another mean expression: ")
animal_1 =("Choose an animal: ")
animal_2 =("choose another animal: ")
animal_3 =("choose another animal: ")
animal_4 =("choose another animal: ")
yes_no_responce = ("Choose a yes/no responce: ")
facial_expression = ("Choose a facial_ expression: ")
verb =("Choose a past tense verb (Action word; ex:Ran,swam,etc.): ")

print("Printing your mad libs......")

mad_libs_1 = "Mother Duck lived on a farm. In her nest, she had " + number_1 + " " + color_1 + " eggs and one " + adjective_1 + " egg. One day, the " + number_1 + color_1 + "eggs started to crack."
mad_libs_2 = noise_1 + "," + noise_1 + "," + noise_1 + "!" + number_1 + positive_description + "," + color_2 + "baby ducklings came out."
mad_libs_3 = "Then the " + adjective_1 + "egg started to crack." + Dramatic_noise +  "," + Dramatic_noise + "," + Dramatic_noise + "!" + "One big, ugly duckling came out." + Shocked_disgusted_expression + "thought Mother Duck."
mad_libs_4 = "Nobody wanted him. " + mean_expression_1 + "said his brothers and sisters. ‘You’re ugly!’ The ugly duckling was sad. So he went to find some new friends."

print("Printing your mad libs......")
print(mad_libs_1)
