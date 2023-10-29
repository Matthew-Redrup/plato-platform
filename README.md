# Plato Platform
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Python Versions](https://img.shields.io/pypi/pyversions/poetry-core)](https://pypi.org/project/poetry-core/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The Plato Platform is a proof of concept, learner centered, open education platform. It is designed to be a tool for both learners and education facilitators. Funtionally it's aim is to create educational content specific to each individual learner, measure their progress, provide feedback and finally certify their knowledge.

## A Learning Model for the Modern Era

**Problem**

The 'factory model of education' does not sufficiently account for the differences in individual learners. This model neglects the periphery of both ends of the bell curve, leaving behind those who cannot keep up and holding back those who could progress faster. The current curriculum-based content also fails to adapt to a learner's situation, goals, abilities, and interests. Furthermore, the certification-style output gives only a limited indication of a learner's final competence, retention, or overall ability and does not map the learner's strengths and weaknesses to assist in future decisions.

**Solution**

We propose an architecture implementing a combination of task-specific agents in conjunction with a persistent model of individual learners. The agents will draw on language models to execute varied tasks beneficial for the learner. This ranges from initial content creation, gathering and processing external information, structuring tailored education content, to evaluating the learner's understanding and producing actionable reports. The persistent model will keep track of contextual details to shape the learning experience. A scheduling mechanism will implement a spaced, interleaved retrieval process. Removing some of the difficult scheduling and management tasks of learning and freeing the learner to focus on the difficult task of processing the content and incorporating it into their own knowledge base. 

**Rabbit Holes**

The main potential complexity is the scale of the solution. We could limit our scope for the proof-of-concept project, starting with the first three agents to avoid over-complication that may slow down progress or harm feasibility.

**No-gos**

For the scope of this project, we're limiting the implementation to pure text and image-based content while excluding audio and video content. Functionality in other languages outside of Python will also be considered outside our scope due to existing toolset compatibility.

## Initial Architecture Requirements

### Basic Outline of Agent Tasks 
- **Host**: an agent that will utilize something similar to "The Fisherman's Prompt" that takes an initial request from the learner to produce content on a particular topic including proposed sub-topics the learner wishes to cover. The Host then attempts to make a plan for what the structure of the learning will be and creates some of the initial content based on existing knowledge already existing in the LLMs cognitive structure. The host will attempt to flag areas where it does not have existing knowledge of content or where their existing content may be inaccurate or incorrect in some form.

- **Researcher**: The researcher will take the content produced by the host and attempt to improve on the existing plan. In particular the researchers aim is to find conflicting or contrasting information on the topic, as well as attempting to find relating topics that may overlap with interests of the learner, as well as other contextual information from the model.  This agent will have access to functions that allow it to search for external information such as some limited form of web search. This agent is aiming to pull in as much of the information space as possible related to the topics requested by the learner.

- **Educator**: The educator takes the content from the host and researcher and will attempt to synthesize it into a form that is appropriate for the learner's level (e.g. if the learner asked a physics question, the response should be very different for a learner that is learning high school physics compared to a post graduate researcher with many years of experience). If there are conflicting opinions in the field of study the educator should still present all sides. Additionally, the educator is not simplifying the content or creating crib notes as it is necessary for the learner to struggle with the concepts and decide for themselves what is important and how the information fits together.

-  **Examiner**: Agent that takes in what the learner has previously learnt and periodically converses with the learner to ask about the topics. This could be simple questions, or difficult interactive tasks such as providing a dynamic coding problem that incorporates multiple things the learner has studied previously and asking the user to write code that solves the problem.

- **Reporter**: Agent takes the record of learning and creates an ongoing report that outlines what the learner has learnt. Their strengths and weaknesses. Maps this to their goals and career (this may include mapping to well-known formal certifications) and outlines proposed next steps or topics to investigate. It could also generate a resume style report that only contains the good parts.

### Persistent Model of Learner - Contextual Information
- current position (e.g. if in formal schooling what level, if in some form of work what type of work is it and what level are they in in that role)
- Personal and professional goals
- Interests 
- Previous learning

### Diagram of Initial Proposed Architecture
![plato_project_diagram1](https://github.com/Matthew-Redrup/plato-platform/assets/16837301/96bee611-9044-4043-95c9-10eb0b22d117)

## Installation and usage

### Installation
Clone the repository and then move into the directory:
```bash
git clone git@github.com:Matthew-Redrup/plato-platform.git
cd plato-platform
```
Then install using poetry:
```bash
poetry install
```

### Usage
You will need to create a .env file in the root directory of the project. This file should contain the following variables:
```bash
OPENAI_API_KEY=""
```
Then to start the program run the following command with a prompt detailing the topic you wish to learn about:
```bash
poetry run start --prompt "Teach me about the history of the world"
```
