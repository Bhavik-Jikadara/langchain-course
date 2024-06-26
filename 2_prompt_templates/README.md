# [Prompt Templates](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/quick_start/)

Prompt templates are predefined recipes for generating prompts for language models.

* A template may include instructions, few-shot examples, and specific context and questions appropriate for a given task.
* LangChain provides tooling to create and work with prompt templates.
* LangChain strives to create model agnostic templates to make it easy to reuse existing templates across different language models.
* Typically, language models expect the prompt to either be a string or else a list of chat messages.

ChatModels take a list of messages as input and return a message. There are a few different types of messages. All messages have a role and a content property. The role describes WHO is saying the message. LangChain has different message classes for different roles. The content property describes the content of the message. This can be a few different things:

* A string (most models deal this type of content)
* A List of dictionaries (this is used for multi-modal input, where the dictionary contains information about that input type and that input location)

In addition, messages have an additional_kwargs property. This is where additional information about messages can be passed. This is largely used for input parameters that are provider specific and not general. The best known example of this is function_call from OpenAI.

* **HumanMessage**: This represents a message from the user. Generally consists only of content.

* **AIMessage**: This represents a message from the model. This may have additional_kwargs in it - for example tool_calls if using OpenAI tool calling.

* **SystemMessage**: This represents a system message, which tells the model how to behave. This generally only consists of content. Not every model supports this.

* **FunctionMessage**: This represents the result of a function call. In addition to role and content, this message has a name parameter which conveys the name of the function that was called to produce this result.

* **ToolMessage**: This represents the result of a tool call. This is distinct from a FunctionMessage in order to match OpenAI's function and tool message types. In addition to role and content, this message has a tool_call_id parameter which conveys the id of the call to the tool that was called to produce this result.

Here is API reference for the PromptTemplate class:

* [PromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.prompt.PromptTemplate.html) to create a template for a string prompt.
* [ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html) for chat models.
* [ChatMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatMessagePromptTemplate.html) for messages with arbitrary roles;
* [AIMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.AIMessagePromptTemplate.html) for AI assistant messages;
* [SystemMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.SystemMessagePromptTemplate.html) for system messages;
* [HumanMessagePromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.HumanMessagePromptTemplate.html) for user messages;
