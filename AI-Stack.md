## Building AI for the Real World: A Deep Dive into AI Stacks

The world of Artificial Intelligence is booming, with possibilities ranging from conversational chatbots to robots that can (almost) make you dinner. But building and deploying real-world AI applications requires more than just a theoretical understanding of AI algorithms. It requires a deep dive into the technologies that power these systems, especially the cloud infrastructure that makes AI scalable and accessible. 

This blog post delves into a comprehensive AI course curriculum, designed to equip you with the knowledge and skills to build, deploy, and manage AI applications using the latest cloud-native technologies. The core of this curriculum revolves around five distinct "AI Stacks," each representing a different level of complexity and control. 

### Demystifying AI: Key Concepts & Definitions

Before we explore the five stacks, let's establish a common language:

* **AGI (Artificial General Intelligence):**  The holy grail of AI research, AGI represents an AI system capable of performing any intellectual task a human can. While not yet achieved, it's the ultimate ambition.
* **5 Levels of AGI:** To understand where we are on the path to AGI, it helps to break it down into five levels:
    * **Chatbots:**  These conversational AI systems, like ChatGPT, are already commonplace.
    * **Reasoners:**  AI systems capable of advanced problem-solving across various topics are currently under development. 
    * **Agents:**  Imagine AI systems taking actions independently, even coordinating with other AI agents - that's the vision for future agents.
    * **Innovators:**  This futuristic level envisions AI that can generate new ideas, contribute to human knowledge, and even create better AI systems.
    * **Organizations:**  The highest and most futuristic level imagines AI capable of independently managing entire organizations.
* **API (Application Programming Interface):** APIs are the connectors that allow different software applications to communicate and interact.
* **Open API Specification:** A standard format ensures consistency and eases integration when defining APIs for AI services.
* **Cloud Native Microservices:**  Modern cloud applications often use microservices, which are small, independent services that run in containers. 
* **Docker:** Docker is the technology that makes containers possible, ensuring your applications run consistently across different environments.
* **Kubernetes (K8s):** When it comes to orchestrating and managing containerized applications at scale, Kubernetes is the industry standard.
* **Serverless:**  This cloud computing model removes the burden of managing server infrastructure. Cloud providers handle the servers, leaving you to focus solely on your code.
* **LLM (Large Language Model):** Think ChatGPT and LaMDA. These powerful AI models are trained on vast text datasets, enabling them to understand and generate human-like language.
* **Fine-tuning:** Adapting a pre-trained LLM, like LaMDA, to perform specific tasks within your particular domain is known as fine-tuning.
* **Agentic Framework:**  Frameworks designed to build AI agents that can take actions and collaborate with other agents.
* **Physical AI:** This refers to AI systems interacting with the physical world, often in the form of robots.
* **NVIDIA Jetson:**  NVIDIA Jetson devices are small, powerful computers with GPUs specifically designed for AI and robotics applications.
* **ROS 2 (Robot Operating System 2):** An open-source framework for building robot applications.

### The 5 AI Stacks: Building Blocks for AI Development

The course utilizes a stack-based approach, starting with fundamental concepts and progressively moving toward advanced topics. Here's a breakdown of the five AI stacks:

#### Stack Zero: Local AI Microservice Development Stack

* **Focus:** Building foundational AI microservices on your local machine (your laptop or PC).
* **Technologies:** You'll learn to use Docker, Docker Compose, FastAPI (a Python web framework), Python programming language, PostgreSQL database, Kafka (a messaging system), basic inference APIs, open-source LLMs, and NVIDIA NeMo (a toolkit for running LLMs).
* **Action:**  Get started by installing Docker and other necessary tools on your laptop.

#### Stack One: Serverless with OpenAI APIs

* **Focus:** Rapid development leveraging pre-built AI functions from OpenAI, delivered as serverless services.
* **Benefits:** Quickly build applications using powerful existing AI features without managing server infrastructure.
* **Technologies:** Learn to use the OpenAI API (for chat, image generation, and other tasks), FastAPI, Python, Docker, PostgreSQL database, and cloud serverless platforms. 

#### Stack Two: Custom AI Stack with PyTorch, LaMDA, and Kubernetes

* **Focus:**  Building and deploying AI applications tailored to specific needs, using open-source LLMs like LaMDA.
* **Key Actions:** This stack focuses on customization (adapting existing LLMs to your domain), integration (connecting your AI system to other applications), and innovation (developing specialized solutions). 
* **Technologies:**  Master PyTorch (a deep learning framework) for working with LLMs, LaMDA (an open-source LLM), Kubernetes for container orchestration, and NVIDIA NeMo.

#### Stack Three: OpenAI ChatGPT Stack with Conversational Interface

* **Focus:** Building conversational user interfaces (CUIs) powered by OpenAI's ChatGPT.
* **Key Concepts:** Understand the difference between traditional GUIs (graphical user interfaces) and CUIs, and the unique advantages of conversational interactions.
* **Tools:** Learn to leverage ChatGPT and OpenAI's marketplace for custom GPT development.

#### Stack Four: The Rise of Agentic AI (A New Era of Intelligence & Collaboration)

* **Focus:** Building autonomous AI agents that can perform tasks, interact with other agents, and potentially operate continuously.
* **Current Frameworks:**  Explore frameworks like LangChain (with its LangGraph) and Cru AI, designed for building sophisticated agents.
* **Future:**  Expect deeper integration of agnetic frameworks into OpenAI and other major AI platforms.

#### Stack Five: Physical AI Robotics (powered by NVIDIA Jetson)

* **Focus:**  Bringing AI into the physical world by building robots that can interact with their environment.
* **Hardware:**  Work with NVIDIA Jetson computers, compact yet powerful devices with GPUs specifically for AI and robotics.
* **Software:** Learn to use ROS 2 (Robot Operating System 2) and explore the potential of using LLMs like ChatGPT for robot interaction and intelligence.
* **Companies:** NVIDIA is heavily investing in this space, while Boston Dynamics continues to be a leading company in the robotics field.

### Course Materials & Resources

The materials for this course can be found in the following GitHub repository:

[https://github.com/panaversity/learn-applied-generative-ai-fundamentals](https://github.com/panaversity/learn-applied-generative-ai-fundamentals)


Here are some key platforms and tools you'll encounter in this course:

* **Cloud Platforms:**
    * **Google Cloud Platform (GCP)**
    * **Amazon Web Services (AWS)**
    * **Microsoft Azure**
* **Managed Kubernetes Services:**
    * **Google Kubernetes Engine (GKE)**
    * **Amazon Elastic Kubernetes Service (EKS)**
    * **Azure Kubernetes Service (AKS)**
* **Serverless Container Platforms:**
    * **Google Cloud Run**
    * **Amazon Fargate**
    * **Azure Container Apps**
* **OpenShift:**  A robust enterprise Kubernetes platform.
* **Github:**  The go-to platform for managing and collaborating on code.


### The Miscalculated Bet: Blockchain Over AI

In the past year, a common mistake many made was prioritizing blockchain technologies over AI.  This misjudgment can be traced back to misinterpretations of the Gartner Hype Cycle, a graphical representation of the maturity and adoption of emerging technologies.

<br>

<img src="https://www.gartner.com/ngw/globalassets/en/articles/images/hype-cycle-for-emerging-tech-2022.png" alt="Gartner Hype Cycle"/>

<br>

The hype cycle shows how new technologies progress through various stages:

* **Innovation Trigger:** Initial enthusiasm and media hype.
* **Peak of Inflated Expectations:**  Unrealistic projections and hype-driven investment.
* **Trough of Disillusionment:** As expectations fail to meet reality, interest wanes.
* **Slope of Enlightenment:** The technology's practical value becomes clearer, leading to gradual adoption.
* **Plateau of Productivity:** Mainstream adoption and widespread use.

Many wrongly assumed that blockchain technology was closer to the "Plateau of Productivity" than AI.  They anticipated faster mainstream adoption and potentially quicker returns on investment. However, the reality is that blockchain, while offering significant potential for certain applications, is still navigating the "Trough of Disillusionment." Its complexity, scalability challenges, and regulatory uncertainties have hindered its wider adoption.

On the other hand, AI, particularly generative AI driven by LLMs, has surged ahead.  OpenAI's ChatGPT, launched in late 2022, has demonstrated the transformative power of AI, capturing both public imagination and driving substantial investment in AI research and development. This unexpected acceleration has caught many off guard. 

**Lessons Learned:**

* **Don't Misread the Hype:** The Gartner Hype Cycle is a useful tool, but it's not a crystal ball.  It's crucial to assess the practical applications and real-world challenges of any emerging technology beyond the hype.
* **Adaptability is Key:** The tech landscape is constantly evolving. Be flexible and adapt your strategies based on emerging trends and technological advancements.
* **Focus on Value, Not Hype:** Instead of chasing the hype, prioritize technologies that offer tangible value and address real-world needs. 

### Key Takeaways & Advice

* **Focus and Pace Yourself:**  Don't try to learn everything at once. Follow the course structure, master each stack, and build your knowledge progressively.
* **Hands-on Experience is Key:**  AI and cloud technologies are best learned by doing. Practice, experiment, and build your own projects.
* **Don't Give Up:**  AI is a complex field. It's natural to feel overwhelmed at times. Keep learning, reviewing, and practicing. Perseverance will pay off!
* **Think about the Future:**  AI is evolving rapidly. Think about how these technologies can be applied to solve real-world problems and build innovative solutions.
* **Embrace Serverless:** Serverless computing simplifies development and deployment, making it a valuable skill for AI developers.
* **Understand Open Source vs. Closed Source:** Open-source LLMs offer greater control but require more expertise. Closed-source AI services, like OpenAI APIs, are easier to use but have limitations. Choose the approach that best suits your project and skill level.

By grasping the fundamental concepts, mastering the tools, and completing hands-on projects, you'll be well-prepared to enter the exciting world of AI development.  This course is a stepping stone to building AI applications that can impact the real world.  


