# AI Innovations in Web Marketing

<p align="center">
  <!--  style="max-width: 100%; height: auto;" height="400" -->
  <img src="images/covers.gif"/>
  <br>
  <i>same prompt, different images with OpenAI's Dall-E 3</i>
</p>

From May to October 2024, I was awarded a scholarship from the **University of Padua**, during which I worked as a researcher for **[SiteBySite](https://www.sitebysite.it/)**, a leading **web marketing company** with offices in Padua and Milan. My primary focus was contributing to a region-funded project aimed at integrating **advanced AI innovations** across various aspects of the company's operations. The scholarship was funded by the **Human Inspired Technologies Research Centre (HIT)**, under the guidance of professors [Alessandro Sperduti](https://www.math.unipd.it/~sperduti/) and [Marco Zorzi](https://www.dpg.unipd.it/en/marco-zorzi/).

<!-- <p align="center">
  <img src="images/cover_8.jpg" height="350"/>
</p> -->

## The 3 applications of AI in Web Marketing

With [Alberto Narenti](https://www.sitebysite.it/noi/adv-team/alberto-narenti/) and [Riccardo Coni](https://www.sitebysite.it/noi/pm-team/riccardo-coni/), respectively ADV Manager and Project Manager at SiteBySite, we settled on three case studies to test the effectiveness of AI in different work areas of the company:

1. **Creation of Buyer Personas**

<p align="center">
  <img src="images/GPT_Buyer_Personas_8.jpg" width = 250 style="max-width: 100%; height: auto;"/>
  <br>
</p>

Developing buyer personas is a critical step for a company to understand its target audience. These semi-fictional representations, based on market research and real customer data, help marketers identify the preferences, behaviors, and challenges of their ideal customers. Buyer personas serve as a foundation for creating personalized and effective marketing campaigns.

2. **Generation of web blogs and Instagram posts**

<p align="center">
  <img src="images/GPT_Blog_post_3.jpg" width = 250 style="max-width: 100%; height: auto;"/>
  <br>
</p>

Creating web blogs and Instagram posts is essential for building a strong online presence and engaging target audiences. By consistently generating high-quality, audience-focused content for both platforms, businesses can boost brand awareness, establish credibility, and encourage meaningful engagement, turning followers into loyal customers.

3. **Generation of infographics**

<p align="center">
  <img src="images/GPT_Infographics.jpg" width = 250 style="max-width: 100%; height: auto;"/>
  <br>
</p>

Infographics combine concise text, striking visuals, and data-driven insights to capture attention and enhance understanding. For a company, they serve as an effective tool to engage audiences by simplifying concepts and telling compelling stories through design.


# Work in progress...

<p align="center">
  <img src="images/GPT building the future.jpg" width = 500 style="max-width: 100%; height: auto;"/>
  <br>
  <i>I'm in the process of writing the following of this page! Will be done soon!</i>
</p>

## Creation of Buyer Personas

<p align="center">
  <img src="images/GPT_Buyer_Personas.gif" width = 400 style="max-width: 100%; height: auto;"/>
  <br>
</p>

Creating buyer personas requires combining **informations about the company** and a solid **marketing knowledge**.
We researched the most popular prompts for Buyer Personas generations and settled on 3 casistisc:


| Prompt Baseline | Prompt "Dalla Bona" | Prompt KE |
|- | -| -|
| A minimalist baseline prompt | A 3-step prompt, providing 1. Segmentation, 2. Details per persona, 3. Specialist programs and topics | A complete prompt requiring demographic and psicographic details about the buyer persona |
| - | [link](https://www.linkedin.com/posts/giovannidallabona_3-prompt-per-il-marketing-ugcPost-7217823801663770624-SkR0/?utm_source=share&utm_medium=member_desktop) | [link1](https://www.youtube.com/watch?v=GwUhlpe1ri8), [link2](https://www.youtube.com/watch?v=FGF8RusTIQ0) *(they likely both found the prompt, the original source is unknown)* |

A quick commentary on each:

1. **Prompt Baseline**: will give a lot of insightful details but in a random, non-repeatable way: we have no control over the output and it will creatively decide what to include and what not to;

2. **Prompt "Dalla Bona"**: much more detailed and complete prompt. The segmentation step is clean and gives satisfying results. The profilation is nice but not as much as the one given by the 3rd prompt;

3. **Prompt KE**: a fully organized and exact prompt, which will give the same output structure at every iteration. The demographic and psicographic profilation is rich of facts and details and can be personalized freely.

### Steps to get Segmentation and Profilation of Buyer Personas through GPT

Here's the process you can follow to get a Segmentation and Profilation of a Buyer Persona for any company. 

**Step 1: Segmentation**

Below the prompt and an example of use:

```md
You are a Marketing expert, specialized in market segmentation, targeting, and defining buyer personas. Help me identify potential buyer personas for my business "*Business name and location*". Suggest possible Buyer Personas based on the theories of the Business Model Canvas by Alexander Osterwalder & Yves Pigneur and their segmentation methods. For each buyer persona, provide only the key elements to identify them, such as a category and a few demographic and descriptive elements.

You can look up the following websites for informations:
- *http://www.example.com/index.html*
- *url 2*
- ...
```

<p align="center">
  <!--  style="max-width: 100%; height: auto;" height="400" -->
  <img src="images/GPT_Screenshot_01.png"/>
  <br>
  <i>same prompt, different images with OpenAI's Dall-E 3</i>
</p>



```md
asdasd
```


The process of creating Buyer Personas was fully automated through a **Google Spreadsheet** and **Google Apps Script**, which of course I can't share here.


## Generation of web blogs and Instagram posts

<p align="center">
  <img src="images/GPT_Blog_post.gif" width = 400 style="max-width: 100%; height: auto;"/>
  <br>
</p>

[...]

## Generation of infographics

<p align="center">
  <img src="images/GPT_Infographics.jpg" width = 400 style="max-width: 100%; height: auto;"/>
  <br>
</p>

[...]

### GPT: A quick introduction

In the past few years, GPT and other large language models based on the **transformer architecture** have become fundamental tools in many applications, revolutionizing natural language processing with unparalleled performance in tasks like **text generation, translation, and coding**. In fact, both the text you're reading and the images you're seeing were generated by GPT. Fascinating, isn’t it?


GPT, or **Generative Pre-trained Transformer**, uses massive training data to predict and generate human-like text, building on the encoder-decoder attention mechanisms from the influential "Attention Is All You Need" paper. Each GPT iteration has shown significant improvements, enabling nuanced prompt understanding and **few-shot learning**. Despite its strengths, GPT outputs may need fine-tuning or validation for accuracy. Success stories highlight combining **prompt engineering** with collaborative expertise for optimal results.

<p align="center">
  <img src="images/transformer.jpg" width = 300 style="max-width: 100%; height: auto;"/>
  <br>
  <i>The transformer architecture from the paper "Attention Is All You Need"</i>
</p>
