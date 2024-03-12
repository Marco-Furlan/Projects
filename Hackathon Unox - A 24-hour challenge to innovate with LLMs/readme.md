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

2) A text-to-text algorithm,

3) A text-to-command algorithm,

4) A functioning 3d renderer.

We did everything during the 24 hours we were given, managing to create a single model that, from a spoken command, generates an appropriate answer, a command, and initializes a timer which is displayed real-time through the camera input of the laptop or the phone!

<p align="center">
  <img src="images/phone_video.gif" height="300"/>
  <img src="images/pc_video.gif" height="300"/>
</p>
