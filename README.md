# Complete Beginner's Guide to LangChain: Build AI Agents and Chatbots

The [LangChain](https://www.langchain.com/) Crash Course repository serves as a comprehensive resource for beginners who are ready to learn LangChain, a programming framework designed for creating **AI agents**, building **RAG (Retrieval-Augmented Generation) chatbots**, and **automating tasks** using artificial intelligence.

## Learning Objectives

* Creating AI Agents: Understand and implement agent-based programming principles using LangChain.
* Building RAG Chatbots: Develop RAG chatbots integrating retrieval-based and generative AI techniques.
* Automating Tasks with AI: Use LangChain for automating repetitive tasks and improving workflow efficiency.

## Course Outline

1. [Chat Models](1_chat_models): Learn how to interact with models like ChatGPT, Claude, and Gemini.
    * `1_chat_model_basic.py`
    * `2_chat_model_basic_conversation.py`
    * `3_chat_model_conversation_with_user.py`
2. [Prompt Templates](2_prompt_templates): Understand the basics of prompt templates and how to use them effectively.
    * `1_prompt_template_basic.py`
    * `2_prompt_template_with_chat_model.py`

3. [Chains](3_chains): Learn how to create chains using Chat Models and Prompts to automate tasks.
    * `1_chains_basics.py`
    * `2_chains_under_the_hood.py`
    * `3_chains_extended.py`
    * `4_chains_parallel.py`
    * `5_chains_branching.py`

4. [RAG (Retrieval-Augmented Generation)](4_rag): Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.
    * `1a_rag_basics.py`
    * `1b_rag_basics.py`
    * `2a_rag_basics_metadata.py`
    * `2b_rag_basics_metadata.py`
    * `3_rag_text_splitting_deep_dive.py`
    * `4_rag_embedding_deep_dive.py`
    * `5_rag_retriever_deep_dive.py`
    * `6_rag_one_off_question.py`
    * `7_rag_conversational.py`
    * `8_rag_web_scrape_firecrawl.py`
    * `8_rag_web_scrape.py`

5. [Agents & Tools](5_agents_tools): Learn about agents, how they work, and how to build custom tools to enhance their capabilities.
    * `1_agent_and_tools_basics.py`
    * `agent_deep_dive/`
        * `1_agent_react_chat.py`
        * `2_react_docstore.py`
    * `tools_deep_dive/`
        * `1_tool_constructor.py`
        * `2_tool_decorator.py`
        * `3_tool_base_tool.py`

## Set up your environment variables:

* Rename the `.env.example` file to `.env` and update the variables inside with your own values. Example:

   ```bash
   cp .env.example .env
   ```  

* Add all api keys to the `.env` file.

   ```bash
    OPENAI_API_KEY="Enter the OPENAI api key"
    GOOGLE_API_KEY="Enter the GOOGLE api key"
    FIRECRAWL_API_KEY="Enter the FIRECRAWL api key"
    TAVILY_API_KEY="Enter the TAVILY api key"
    OPENAI_MODEL_NAME="gpt-3.5-turbo"
   ```

## Follow

* Linkedin Link: <https://www.linkedin.com/in/bhavikjikadara>
* Github Link: <https://github.com/Bhavik-Jikadara>
* Facebook Link: <https://www.facebook.com/Bhavikjikadara07>
* Instagram Link: <https://www.instagram.com/bhavikjikadara/>
* twitter Link: <https://twitter.com/BhavikJikadara1>

## Subscribe

* <https://www.youtube.com/channel/UC7Bp_sYQmAryrrPqvUp6PwQ>

## Donate & Support us

* <https://www.paypal.com/paypalme/bhavikjikadara>

## License

The Multiple PDFs QueryBot is released under the [Apache License 2.0](https://github.com/Bhavik-Jikadara/langchain-course/blob/main/LICENSE).
