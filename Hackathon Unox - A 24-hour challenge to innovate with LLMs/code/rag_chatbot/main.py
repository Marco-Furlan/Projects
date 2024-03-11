import sys
import json
import json_lib as glib

pdf_path = 'rag_input.pdf'

if __name__ == '__main__':

    question = sys.argv[1]
    # json = sys.argv[2]

    print('INPUT:',question)
    ############
    ### JSON ###
    ############
    
    pre_prompt = '\n\nContext: You are the assistent of a smart oven, taking informations from a human.\n\nHuman: '
    post_prompt = '''\n
    Based on the above text, please don't answer, but encode the question in JSON format:
    Question: Temperature, Set_timer, or Stop_timer (else Not_Valid)
    Value: integer if Set_timer (else 0)
    Unit: Minutes or Seconds if Set_timer (else None).
    '''

    post_prompt = '''\n
    Based on the above text, please don't answer, but encode the question in JSON format:
    Question: On_or_Off, Mode, Working_Time, Humidity, Set_Humidity, Set_Preheat, Temperature, Set_Temperature, Set_timer, or Stop_timer (else Not_Valid)
    (Hours)
    (Minutes)
    (Seconds)
    (Value: value with unit)
    (Holding Time: for set preheat)
    (other parameters if set).
    '''

    if not question.lower().startswith("hey oven"):
        response_content = {"Command": "Not_Valid", "Value": 0, "Unit": "None"}
        has_error = False
    else:
        has_error, response_content, err = glib.get_json_response(input_content=pre_prompt + question + post_prompt) #call the model through the supporting library

    # debug answer
    if isinstance(response_content, dict):
        json_data = str(json.dumps(response_content))
    else:
        if "```json" in response_content:
            start_index = response_content.find('{')
            end_index = response_content.find('}') + 1
            json_data = response_content[start_index: end_index]
        else:
            raise ValueError('No json generated, the input may be unclear or incorrect.')
    
    json_dict = eval(json_data.lower())
    
    if json_dict['question'] == 'temperature':
        json_dict['temperature'] = 25
    if json_dict['question'] == 'humidity':
        json_dict['humidity'] = 20
    if json_dict['question'] == 'on_or_off':
        json_dict['on_or_off'] = 'on'

    # print('JSON:',json_dict)

    #####

    json = str(json_dict)




    import rag_chatbot_lib as clib #reference to local lib script

    memory = clib.get_memory() #initialize the memory

    vector_index = clib.get_index(pdf_path) #retrieve the index through the supporting library and store in the app's session cache
    
    prompt_input = f'''
    Context: you are a virtual assistant for an oven. You need to answer based on the example answers you have. Make sure to update the parameters in the answers based on the JSON file information.    
    Question: {question},
    JSON: {json},
    Answer:'''

    chat_response = clib.get_rag_chat_response(input_text=prompt_input, memory=memory, index=vector_index) #call the model through the supporting library

    print('OUTPUT:',chat_response)