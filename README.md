# Smart Spreadsheet

## Runninng the project locally

Follow these steps to run the project locally!

1. **Get the Project Files:**:

   ```sh
   git clone https://github.com/jackReacher1234/Smart-Spreadsheet-Skanda.git
   cd Smart-Spreadsheet-Skanda
   ```

2. **Prepare Your Environment**:
   Developed in Python 3.12.3
   ```sh
   python -m venv .venv
   source ./.venv/bin/activate  # On Mac and Linux
   source .venv\Scripts\activate # On Windows
   ```

3. **Install Dependencies**:
   Install the required Python packages using `pip`:

   ```sh
   pip install -r requirement.txt
   ```
4. **Execute code**:
   ```sh
   python main.py
   ```
5. **Clone frontend:**
   ```sh
   git clone https://github.com/jackReacher1234/smart-spreadsheet-next.git
   ```

6. **Run frontend locally**
   
   Follow the instructions mentioned in frontend repository to run it locally! You can also find the hosted frontend available at https://www.nextify.dev/

Happy hacking!

## Introduction

As a **Founding Senior Engineer** at Capix you will lead the the development of the Company’s technical vision and strategy, oversee all the technological development, and help develop and implement the product. This is a very critical role. It is paramount that you are a master of engineering able to ship great software fast. We’re looking for the 10Xers and this project helps us evaluate if you can get the job done. 

The project is open-ended. There is no single right answer, and you have complete creative freedom to solve the problem in whatever way you want.

## Scenario

You are an engineer leading product development at Capix. We just received a request from a key client to build a system that can answer questions from Excel files. The timeline is tight. We have two days to develop this feature. How should we deliver this to our client?


In the repo, there are example Excel files that the client has shared with us. There are also some functions we developed to give you a head start, which you may or may not choose to use.  

## Goals

1. The algorithm should be able to parse and serialize each individual table in the Excel sheet `example_0.xlsx`.
2. An AI chat function that should be able to answer basic question about the excel sheet, e.g. "What is the Total Cash and Cash Equivalent of Nov. 2023?" (No UI is needed)
3. Let's broaden the functionality of the algorithm. Can you make it parse `example_1.xlsx` and `example_2.xlsx`?
4. Let's make the AI more intelligent. Can you make it answer questions that need to be inferred like "What is the Total Cash and Cash Equivalent of Oct. AND Nov. of 2023 combined?"
5. Now that we have a Smart Spreadsheet AI. Let's deploy it for our user to use!

## FAQ
* **How long do I have to solve the problem?** 

  * You have two days to sovle the problem. 

* **What tools, tech stack should I use?**

  * Whatever tools you want. There are no particular requirements. And yes, you can use ChatGPT or nay other open source model and we encourage it.

* **Is building a full-fledged frontend required?** 
  * Would be great, but it's not required. Focus on your strengths.

* **Do I have to achieve all the goals?** 

  * We will be very impressed if you can! Do your best!

* **How to submit?**

  * Please fork the repo, and submit your solution in a branch of your own repo and share the link of your repo with us via email.

## Evaluation Criteria

1. **Functionality**: Ability to parse and serialize tables from provided Excel files, including generalizing the solution to handle multiple examples. The AI should answer both basic questions; advanced generalization and AI inference are considered a bonus.

2. **Problem Solving and Creativity**: Systematic and effective approach to breaking down and addressing each part of the problem. Novel or creative solutions with innovative use of tools and techniques.
  
3. **Code Quality and Readability**: Clear, readable, and well-structured code with consistent naming conventions.

4. **Algorithm Design and Efficiency**: Thoughtful and effective algorithm design, considering edge cases and using appropriate data structures. Efficient implementation in terms of time and space complexity.

5. **Deployment and Usability**: Successful deployment of the solution with clear and detailed setup instructions. Consideration of user experience, ensuring the solution is user-friendly and accessible.

## Remarks

We appreicate the time you will devote to this project. We hope you enjoy this exercise!

