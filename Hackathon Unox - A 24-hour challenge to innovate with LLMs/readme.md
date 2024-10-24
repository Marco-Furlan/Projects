# Hackathon Unox & AWS - A 24-hour challenge to innovate with LLMs

<p align="center">
  <img src="images/hackathon.jpg" width="400"/>
</p>

The Hackathon by [Unox](https://www.unox.com/) (in collaboration with [Amazon Web Services](https://aws.amazon.com)) is a 24-hour coding challenge focused on utilizing LLMs to discover feasible technical innovations for the company's user interfaces. The LLMs we used, such as [Anthropic Claude](https://www.anthropic.com/claude), [Amazon Titan](https://aws.amazon.com/it/bedrock/titan/) and [Stability AI](https://stability.ai/) were provided to us by Amazon Web Services.

Given the upcoming era of AR, me and my team came up with the idea of connecting AR smart glasses and the advanced Unox ovens to allow for a hands-free, fully voice-based control. The pipeline works as follows:

<p align="center">
  <img src="images/our_code.png" width="550"/>
</p>

So we needed:

1) A speech-to-text generator,

2) A text-to-command algorithm,

3) A text-to-text algorithm,

4) A functioning 3d renderer.

I was in charge of points 2 and 3. Ultimately, we succeeded in completing everything during the given 24 hours, managing to create a single model that, from a spoken command, generates an appropriate answer, a command, and initializes a timer which is displayed real-time through the camera input of the laptop or the phone!

<p align="center">
  <img src="images/phone_video.gif" height="300"/>
  <img src="images/pc_video.gif" height="300"/>
</p>

## Generative AI

My role in the team as the only Data Scientist in the group was to design and realise the pipeline which would've levered the LLM language capabilities to understand the input, correctly send the required command to the smart oven, and return a proper output.

So I needed to engineer two separate LLMs:

- **LLM beta**, which would be responsible for the convertion input text --> command,
- **LLM alpha**, which would be responsible for the communication with the user (communicating whether the command was understood and what action was taken)

A basic graph of the pipeline designed is shown below:

<p align="center">
  <img src="images/llm_pipeline.png" height="400"/>
</p>

Since this competition was in partnership with Amazon Web Services, we were enabled to use the most powerful LLMs developed that far by Amazon, Antropic Claude and Amazon Bedrock.

### LLM beta

The first Foundational Model that was called after the vocal command was registered was LLM beta. This model had the objective of converting the vocal command into a json file with the essentials of the order given to the oven. We checked the oven's API and settled for the following commands as examples of use:

| Command         | Description                      |
| --------------- | -------------------------------- |
| On_or_Off       | Turns the oven on or off         |
| Mode            | Selects oven mode                |
| Working_Time    | Asks for the current timer       |
| Humidity        | Asks for the current humidity    |
| Set_Humidity    | Sets humidity                    |
| Set_Preheat     | Sets preheat temperature         |
| Temperature     | Asks temperature                 |
| Set_Temperature | Sets current temperature         |
| Set_timer       | Sets timer                       |
| Stop_timer      | Stops timer                      |
| Not_Valid       | Command was not one of the above |

The importance of using a foundational model other than a more primitive language processing neural network or algorithm is that the same command can be phrased in countless ways, and a deeper understanding of the language is needed to make sure the command is properly processed. Futhermore, this model potentially can understand multiple commands at once.

*Example: "Hey Oven, turn off!"; "Hey Oven, you can stop now"; "Hey Oven, end of the day for you, see you tomorrow!"* --> `{Command: On_or_Off, Value: Off}`

This is the prompt I came up with:

`Context: You are the assistent of a smart oven, taking informations from a human. \\ \\ Human: Based on the above text, please don't answer, but encode the question in JSON format: Question: On_or_Off, Mode, Working_Time, Humidity, Set_Humidity, Set_Preheat, Temperature, Set_Temperature, Set_timer, or Stop_timer (else Not_Valid) \ (Hours) \ (Minutes) \ (Seconds) \ (Value: value with unit) \ (Holding Time: for set preheat) \ (other parameters if set).`

