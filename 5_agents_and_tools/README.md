# Agents & Tools

## [Agents](https://python.langchain.com/v0.1/docs/modules/agents/quick_start/)

The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

### Agent Type

Agents are categorized based on key features:

- **Intended Model Type**: Either for Chat Models (conversational) or LLMs (general language tasks).
- **Supports Chat History**: Yes for chatbots, no for single-task agents.
- **Supports Multi-Input Tools**: Yes allows for handling multiple inputs.
- **Supports Parallel Function Calling**: Yes for multitasking capabilities.
- **Required Model Params**: Some use extra parameters for specific functions.

### When to Use

Our commentary on when you should consider using this agent type.

<table><thead><tr><th>Agent Type</th><th>Intended Model Type</th><th>Supports Chat History</th><th>Supports Multi-Input Tools</th><th>Supports Parallel Function Calling</th><th>Required Model Params</th><th>When to Use</th><th>API</th></tr></thead><tbody><tr><td><a href="/v0.1/docs/modules/agents/agent_types/tool_calling/">Tool Calling</a></td><td>Chat</td><td>✅</td><td>✅</td><td>✅</td><td><code>tools</code></td><td>If you are using a tool-calling model</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.tool_calling_agent.base.create_tool_calling_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/openai_tools/">OpenAI Tools</a></td><td>Chat</td><td>✅</td><td>✅</td><td>✅</td><td><code>tools</code></td><td>[Legacy]<!-- --> If you are using a recent OpenAI model (<code>1106</code> onwards). Generic Tool Calling agent recommended instead.</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.openai_tools.base.create_openai_tools_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/openai_functions_agent/">OpenAI Functions</a></td><td>Chat</td><td>✅</td><td>✅</td><td></td><td><code>functions</code></td><td>[Legacy]<!-- --> If you are using an OpenAI model, or an open-source model that has been finetuned for function calling and exposes the same <code>functions</code> parameters as OpenAI. Generic Tool Calling agent recommended instead</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.openai_functions_agent.base.create_openai_functions_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/xml_agent/">XML</a></td><td>LLM</td><td>✅</td><td></td><td></td><td></td><td>If you are using Anthropic models, or other models good at XML</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.xml.base.create_xml_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/structured_chat/">Structured Chat</a></td><td>Chat</td><td>✅</td><td>✅</td><td></td><td></td><td>If you need to support tools with multiple inputs</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.structured_chat.base.create_structured_chat_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/json_agent/">JSON Chat</a></td><td>Chat</td><td>✅</td><td></td><td></td><td></td><td>If you are using a model good at JSON</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.json_chat.base.create_json_chat_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/react/">ReAct</a></td><td>LLM</td><td>✅</td><td></td><td></td><td></td><td>If you are using a simple model</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.react.agent.create_react_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr><tr><td><a href="/v0.1/docs/modules/agents/agent_types/self_ask_with_search/">Self Ask With Search</a></td><td>LLM</td><td></td><td></td><td></td><td></td><td>If you are using a simple model and only have one search tool</td><td><a href="https://api.python.langchain.com/en/latest/agents/langchain.agents.self_ask_with_search.base.create_self_ask_with_search_agent.html" target="_blank" rel="noopener noreferrer">Ref</a></td></tr></tbody></table>

## [Tools](https://python.langchain.com/v0.1/docs/modules/tools/)

Tools are interfaces that an agent, chain, or LLM can use to interact with the world. They combine a few things:

- The name of the tool
- A description of what the tool is
- JSON schema of what the inputs to the tool are
- The function to call
- Whether the result of a tool should be returned directly to the user

It is useful to have all this information because this information can be used to build action-taking systems! The name, description, and JSON schema can be used to prompt the LLM so it knows how to specify what action to take, and then the function to call is equivalent to taking that action.

The simpler the input to a tool is, the easier it is for an LLM to be able to use it. Many agents will only work with tools that have a single string input. For a list of agent types and which ones work with more complicated inputs, please see this documentation

Importantly, the name, description, and JSON schema (if used) are all used in the prompt. Therefore, it is really important that they are clear and describe exactly how the tool should be used. You may need to change the default name, description, or JSON schema if the LLM is not understanding how to use the tool.

- [Default tool](https://python.langchain.com/v0.1/docs/modules/tools/#default-tools)

- [Customizing Default Tools](https://python.langchain.com/v0.1/docs/modules/tools/#customizing-default-tools)

This was a quick introduction to tools in LangChain, but there is a lot more to learn

- [Built-In Tools](https://python.langchain.com/v0.1/docs/integrations/tools/): For a list of all built-in tools, see [this page](https://python.langchain.com/v0.1/docs/integrations/tools/)
- [Custom Tools](https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/): Although built-in tools are useful, it's highly likely that you'll have to define your own tools. See [this guide](https://python.langchain.com/v0.1/docs/modules/tools/custom_tools/) for instructions on how to do so.
- [Toolkits](https://python.langchain.com/v0.1/docs/modules/tools/toolkits/): Toolkits are collections of tools that work well together. For a more in depth description as well as a list of all built-in toolkits, see [this page](https://python.langchain.com/v0.1/docs/modules/tools/toolkits/)
- [Tools as OpenAI Functions](https://python.langchain.com/v0.1/docs/modules/tools/tools_as_openai_functions/): Tools are very similar to OpenAI Functions, and can easily be converted to that format. See [this notebook](https://python.langchain.com/v0.1/docs/modules/tools/tools_as_openai_functions/) for instructions on how to do that.
