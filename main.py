import cohere
import time
import pandas as pd
co = cohere.Client('d4ZDgfMbd8H2ywZYysLLeFJH3bH9fUEe50OM3tL7')


# Add a new piece of training data to the training_data list.
def add_new_training_data(training_data: list, passage: str, question: str, answer: str) -> None:
  id = len(training_data)
  data = 'Passage:' + passage + '\n\nQuestion:' + question + '\n\nAnswer:' + answer + '\n--\n'
  training_data.append({'id': id, 'data': data})

  
# Generate all the training data and add it to the training_data list.
def generate_training_data(training_data: list) -> None:
  # 'Who' questions
  add_new_training_data(training_data,
                       passage='Steve Jobs was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company\'s board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT.',
                       question='Who was Steve Jobs?',
                       answer='Steve Jobs was most well-known for being the co-founder and CEO of Apple.')
  add_new_training_data(training_data,
                       passage='On 28 June 1914, Franz Ferdinand and his wife were assassinated in Sarajevo by the 19-year-old Gavrilo Princip, a member of Young Bosnia. Franz Ferdinand\'s assassination led to the July Crisis and precipitated Austria-Hungary\'s declaration of war against Serbia, which in turn triggered a series of events that eventually led to Austria-Hungary\'s allies and Serbia\'s allies declaring war on each other, starting World War I.',
                       question='Who\'s assassination led to World War I?',
                       answer='Franz Ferdinand')
  # 'What' questions
  add_new_training_data(training_data,
                        passage='The processes to transform DNA into proteins are known as transcription and translation, and happen in different compartments within the cell.',
                        question='What processes transform DNA intro proteins?',
                       answer='Transcription and translation.')
  add_new_training_data(training_data,
                        passage='A membrane called the nuclear envelope surrounds the nucleus, and its job is to create a room within the cell to both protect the genetic information and to house all the molecules that are involved in processing and protecting that info.',
                        question='What is the job of the nuclear envelope?',
                       answer='The nuclear envelope creates a room within the cell to protect the genetic information.')
  add_new_training_data(training_data,
                        passage='The space between the two bilayers is known as the perinuclear space.',
                        question='What is the space between the two bilayers called?',
                       answer='The perinuclear space.')
  add_new_training_data(training_data,
                        passage='When a program runs, millions of instructions need to be executed. First, the processor fetches the instruction. Then, it decodes it (figures out what the instruction is supposed to do). Finally, it executes the instruction.',
                        question='What is the role of the processor in running a program?',
                       answer='The processor fetches an instruction, decodes it, and then executes it.')
  add_new_training_data(training_data,
                       passage='The Japanese government decided to attack Pearl Harbor after the United States cut off US oil exports to Japan in the summer of 1941. Japan relied on the United States for eighty percent of its oil, and without US oil supplies its navy would be unable to function. In attacking Pearl Harbor the Japanese hoped to cripple or destroy the US Pacific fleet so that the Japanese navy would have free reign in the Pacific.',
                       question='What motives did Japan have in attacking the US naval base at Pearl Harbor?',
                       answer='Japan hoped to destroy the US Pacific fleet so that they could control the Pacific.')
  add_new_training_data(training_data,
                       passage='The number of electrons in the outermost shell of a particular atom determines its reactivity, or tendency to form chemical bonds with other atoms. This outermost shell is known as the valence shell, and the electrons found in it are called valence electrons. In general, atoms are most stable, least reactive, when their outermost electron shell is full.',
                       question='What determines the reactivity of an atom?',
                       answer='The number of valence electrons.')
  add_new_training_data(training_data,
                       passage='A participatory democracy is a model of democracy in which citizens have the power to make policy decisions. Participatory democracy emphasizes the broad participation of people in politics.',
                       question='What is a participatory democracy?',
                       answer='A participatory democracy is a model of democracy in which citizens have the power to make policy decisions.')

  # 'Where' questions
  add_new_training_data(training_data,
                       passage='The number of electrons in the outermost shell of a particular atom determines its reactivity, or tendency to form chemical bonds with other atoms. This outermost shell is known as the valence shell, and the electrons found in it are called valence electrons. In general, atoms are most stable, least reactive, when their outermost electron shell is full.',
                       question='Where are the valence electrons located in an atom?',
                       answer='Valence electrons are located in the outermost shell (valence shell) of the atom.')
  
  # 'When' questions
  add_new_training_data(training_data,
                       passage='On 28 June 1914, Franz Ferdinand and his wife were assassinated in Sarajevo by the 19-year-old Gavrilo Princip, a member of Young Bosnia. Franz Ferdinand\'s assassination led to the July Crisis and precipitated Austria-Hungary\'s declaration of war against Serbia, which in turn triggered a series of events that eventually led to Austria-Hungary\'s allies and Serbia\'s allies declaring war on each other, starting World War I.',
                       question='On what date was Franz Ferdinand assinated?',
                       answer='June 28, 1914')
  add_new_training_data(training_data,
                       passage='The Japanese surprise attack on Pearl Harbor began just before 8 a.m. local time Sunday morning, December 7, 1941. For over an hour, in two waves, some 350 Japanese aircraft—having taken off from six aircraft carriers 230 miles north of Oahu—attacked the naval base.',
                       question='When did the Pearl Harbor attack happen?',
                       answer='On December 7, 1941')

  # 'Why' questions
  add_new_training_data(training_data,
                       passage='The Japanese government decided to attack Pearl Harbor after the United States cut off US oil exports to Japan in the summer of 1941. Japan relied on the United States for eighty percent of its oil, and without US oil supplies its navy would be unable to function. In attacking Pearl Harbor the Japanese hoped to cripple or destroy the US Pacific fleet so that the Japanese navy would have free reign in the Pacific.',
                       question='Why did Japan attack Pearl Harbor?',
                       answer='Because the United States cut off oil exports to Japan.')
  
  
  return training_data

def train_summary():
    response = co.generate(
      model='large',
      prompt='Passage: Criminal behavior is not, itself, indicative of mental illness. If it were, perhaps it could be treated medically. However, some criminals are motivated to engage in illegal and antisocial behavior by underlying psychiatric conditions, especially those conditions that manifest themselves in symptoms such as lack of impulse control and lack of inhibition, hallucinations and delusions, paranoia, hyper-activity, and inability to concentrate or possession of impaired communication skills. Persons suffering from personality disorders, schizophrenia, bipolar affective disorder, aggression, depression, adjustment disorders, and sexual disorders such as paraphilias are prone to criminal behavior, according to “Psychiatric Illness Associated with Criminality,” by William H. Wilson, MD, and Kathleen A. Trott, MD (www.emedicine.com/med/topic3485.htm). Illegal conduct can also stem from drug- or alcohol-induced psychosis or conditions caused by traumatic brain injury. It might be easier for such persons to hide their mental illness in the online community, where they don\'t have to come into physical contact with others, than in the offline world.\nCybercrime that is motivated by psychiatric illness can be difficult to investigate and solve, precisely because the criminal\'s motivations don\'t seem logical or rational. We can understand why a money-motivated offender commits crimes, even though we don\'t approve of the behavior. However, we might not be able to easily understand the actions of a mentally ill person.\n\nTLDR: Criminal behavior is not indicative of mental illness. However, some criminals are motivated to engage in illegal and antisocial behavior by underlying psychiatric conditions, such as personality disorders, schizophrenia, bipolar affective disorder, aggression, depression, adjustment disorders, and sexual disorders.\n--\nPassage: Startups are companies or ventures that are focused on a single product or service that the founders want to bring to market. These companies typically don\'t have a fully developed business model and, more crucially, lack adequate capital to move onto the next phase of business. Most of these companies are initially funded by their founders. Many startups turn to others for more funding, including family, friends, and venture capitalists. Silicon Valley is known for its strong venture capitalist community and is a popular destination for startups, but is also widely considered the most demanding arena.\nStartups can use seed capital to invest in research and to develop their business plans. Market research helps determine the demand for a product or service, while a comprehensive business plan outlines the company\'s mission statement, vision, and goals, as well as management and marketing strategies.\n\n\nTLDR: Startups are companies that are focused on a single product or service that the founders want to bring to market. They typically lack adequate capital to move on to the next phase of business, so they use seed capital to invest in and expand their business plans.\n--\nPassage: Western Alaska was struck by strong winds, heavy rain and significant coastal flooding on Friday and Saturday in a storm that meteorologists said could be one of the worst to hit Alaska in half a century. Remnants of a tropical cyclone, Typhoon Merbok, were forecast to move north through the Bering Sea region from Friday through Sunday, according to the National Weather Service. Coastal flood warnings and high wind warnings were issued for Nome, Stebbins to the south, Point Hope to the north and other areas. Forecasters warned that the storm could cause flooding to homes, businesses and critical infrastructure. “This continues to be a dangerous storm as it is producing water levels above higher than any seen over at least 50 years,” forecasters at the Weather Service in Fairbanks, Alaska, wrote early on Saturday morning. As of 9 a.m. Eastern on Saturday, water levels were seven to nine feet above normal in Nome, where the population is less than 10,000, said the National Ocean Service, a division of the National Oceanic and Atmospheric Administration. Waves north of the Aleutian Islands were reported at or above 35 feet for 12 hours straight on Friday and peaked at more than 50 feet, forecasters said.\n\nTLDR:',
      max_tokens=50,
      temperature=0.7,
      k=0,
      p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop_sequences=["--"],
      return_likelihoods='NONE')
    summary = format(response.generations[0].text)
    return summary 
# Concatenate all elements of lst into a string and return it
def convert_list_to_string(lst: list) -> str:
  str = ''
  for data in lst:
    str += data['data']
  return str


# Generate and return a question and answer for the given passage.
def generate_question_and_answer(training_data_str: str, passage: str) -> str:
  prompt = training_data_str + passage + 'Question:'

  prediction = co.generate(model='xlarge',
                           prompt=prompt,
                          max_tokens=50, 
                          temperature=0.8, 
                          k=0, 
                          p=1, 
                          frequency_penalty=0, 
                          presence_penalty=0, 
                          stop_sequences=["--"], 
                          return_likelihoods='NONE')
  generation = prediction.generations[0].text
  
  lst = generation.split('?')
  lst[0] += '?'  # Question
  lst[1] = lst[1].lstrip()  # Answer
  return [generation, lst[0], lst[1]]


# Get the user feedback about the generated flashcard and handle it appropriately.
# If the flashcard is useful, add it to the training_dataset and training_data_str.
# Otherwise, ask for better suggestions.
def get_user_feedback(generation: str, passage: str, question: str, answer: str, training_data: list, training_data_str: str) -> None:
  feedback = input('Was the generated flashcard useful? (y/n)')
  if feedback.lower() == 'y':
    # Add to training dataset
    add_new_training_data(training_data, passage, question, answer)
    training_data_str += 'Passage:' + passage + '\n\nQuestion:' + question + '\n\n' + answer + '\n'
    return training_data_str
    
  elif feedback.lower() == 'n':
    # Ask for better sugestions (helper method)
    print('Please provide what a better flashcard would look like')
    return ''
    # user_question = input('Please type the question should have been generated from this passage:')
    # print()
    # user_answer = input('Please type the answer to the above question:')
    # print()

    # # Add the user inputted flashcard to the training dataset
    # add_new_training_data
    # print()
    
  else:
    print('Error: Incorrect input detected!')
    return ''
      

def passageToQandA(passage):
  training_data = []
  generate_training_data(training_data)
  training_data_str = convert_list_to_string(training_data)
  return [generate_question_and_answer(training_data_str, passage)[1], generate_question_and_answer(training_data_str, passage)[2]]

def main():
  training_data = []
  generate_training_data(training_data)
  training_data_str = convert_list_to_string(training_data)

  while(True):
    # print(training_data_str)
    # print(len(training_data))
    passage = input('Please enter the passage you would like to generate a flash card for:\n')
    print()
    generation, question, answer = generate_question_and_answer(training_data_str, passage)
    print(question)
    print(answer)
    print()
    training_data_str += get_user_feedback(generation, passage, question, answer, training_data, training_data_str)
    print()

if __name__ == '__main__':
  main()
